import dataclasses
import json

import humps
import pika

from constants import default_encoding, rabbit_mq_host, rabbit_mq_port
from settings import RabbitMqSettings


def publish(setting: RabbitMqSettings, value):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbit_mq_host, port=rabbit_mq_port))
    channel = connection.channel()
    value = humps.camelize(dataclasses.asdict(value))
    str_value = json.dumps(value).encode(encoding=default_encoding)
    channel.basic_publish(exchange=setting.exchange,
                          routing_key=setting.routing_key,
                          body=str_value)
    print("Sent message : \n [x] %s" % str_value)
