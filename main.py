import os
import sys

import publish_rabbit
from constants import rabbit_mq_host, text_rl_exchange, treatment_pending_routing_key, text_rl_exchange_type, \
    treatment_done_routing_key

from listen_rabbit import start_listen
from messages import TreatmentDoneMessage, UserId, RunTextTreatmentMessage
from settings import RabbitMqSettings

response = TreatmentDoneMessage(user_id=UserId("id"), result="testResult")

if __name__ == '__main__':
    listen_setting = RabbitMqSettings(routing_key=treatment_pending_routing_key, host=rabbit_mq_host,
                                      exchange=text_rl_exchange, exchange_type=text_rl_exchange_type)
    publish_setting = RabbitMqSettings(routing_key=treatment_done_routing_key, host=rabbit_mq_host,
                                       exchange=text_rl_exchange)
    try:
        start_listen(listen_setting, lambda v: publish_rabbit.publish(publish_setting, TreatmentDoneMessage(
            user_id=UserId("5d5d2c21-2863-4a20-97c1-8356e2ae3ef6"), result="Tototo"))
                     )

    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


def map_run_message(m):
    return TreatmentDoneMessage(user_id=UserId(m.userId.value), result=m.result)
