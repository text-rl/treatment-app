#!/usr/bin/env python

import pika

from constants import rabbit_mq_host, text_rl_exchange, treatment_pending_routing_key, text_rl_exchange_type


def start_listen():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=rabbit_mq_host))
    channel = connection.channel()

    channel.exchange_declare(exchange=text_rl_exchange, exchange_type=text_rl_exchange_type)

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange=text_rl_exchange, queue=queue_name, routing_key=treatment_pending_routing_key)

    print(' [*] Waiting for pending treatment messages. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(" [x] %r" % body)

    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()
