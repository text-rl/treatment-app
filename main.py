import os
import random
import sys
import threading
import time

import redis
from prometheus_client import start_http_server, Summary

import publish_rabbit
from constants import rabbit_mq_host, text_rl_exchange, treatment_pending_routing_key, text_rl_exchange_type, \
    treatment_done_routing_key, redis_host, redis_port, prometheus_http_port
from core.run import anonymize
from listen_rabbit import start_listen
from messages import TreatmentDoneMessage
from settings import RabbitMqSettings

listen_setting = RabbitMqSettings(routing_key=treatment_pending_routing_key, host=rabbit_mq_host,
                                  exchange=text_rl_exchange, exchange_type=text_rl_exchange_type)
publish_setting = RabbitMqSettings(routing_key=treatment_done_routing_key, host=rabbit_mq_host,
                                   exchange=text_rl_exchange)


def on_message_received(v: dict):
    new_message = TreatmentDoneMessage(user_id=v["user_id"], result=v['content'])
    new_message.result = anonymize(new_message)
    publish_rabbit.publish(publish_setting, new_message)


def test_redis():
    client = redis.Redis(host=redis_host, port=redis_port)
    client.set('mykey', 'Hello from Python!')
    value = client.get('mykey')
    print(value)
    client.zadd('vehicles', {'car': 0})
    client.zadd('vehicles', {'bike': 0})
    vehicles = client.zrange('vehicles', 0, -1)
    print(vehicles)


if __name__ == '__main__':
    test_redis()
    start_http_server(int(prometheus_http_port))
    try:
        start_listen(listen_setting, on_message_received)

    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
