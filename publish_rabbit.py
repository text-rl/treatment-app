import dataclasses

import humps
import pika
import json

from constants import default_encoding, text_rl_exchange, treatment_done_routing_key, rabbit_mq_host

from settings import RabbitMqSettings


def publish(setting: RabbitMqSettings, value):
    connection = pika.BlockingConnection(pika.ConnectionParameters(rabbit_mq_host))
    channel = connection.channel()
    value = humps.camelize(dataclasses.asdict(value))
    channel.basic_publish(exchange=setting.exchange,
                          routing_key=setting.routing_key,
                          body=json.dumps(value).encode(encoding=default_encoding))
