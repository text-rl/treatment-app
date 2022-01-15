import os
import sys

import publish_rabbit
from constants import rabbit_mq_host, text_rl_exchange, treatment_pending_routing_key, text_rl_exchange_type, \
    treatment_done_routing_key
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


if __name__ == '__main__':

    try:
        start_listen(listen_setting, on_message_received)

    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
