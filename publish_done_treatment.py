import pika
import json
from constants import default_encoding, text_rl_exchange, treatment_done_routing_key, rabbit_mq_host

from messages import TreatmentDoneMessage, UserId

connection = pika.BlockingConnection(pika.ConnectionParameters(rabbit_mq_host))
channel = connection.channel()

response = TreatmentDoneMessage(user_id=UserId("id"), result="testResult")
channel.basic_publish(exchange=text_rl_exchange,
                      routing_key=treatment_done_routing_key,
                      body=json.dumps(response.__dict__).encode(encoding=default_encoding))
