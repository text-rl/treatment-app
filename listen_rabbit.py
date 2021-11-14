#!/usr/bin/env python
import json
from typing import Callable

import humps
import pika

import constants
from settings import RabbitMqSettings


def start_listen(setting: RabbitMqSettings, callback: Callable):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=setting.host, port=setting.port))
    channel = connection.channel()

    channel.exchange_declare(exchange=setting.exchange, exchange_type=setting.exchange_type)

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange=setting.exchange, queue=queue_name, routing_key=setting.routing_key)

    print(' [*] Waiting for pending treatment messages. To exit press CTRL+C')

    def result_handler(ch, method, properties, body: bytes):
        print(" [x] %r" % body)
        str_body = body.decode(constants.default_encoding)
        obj_body = json.loads(str_body)
        callback(humps.decamelize(obj_body))

    channel.basic_consume(
        queue=queue_name, on_message_callback=result_handler, auto_ack=True)

    channel.start_consuming()
