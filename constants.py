import os

default_encoding = os.getenv('DEFAULT_ENCODING', 'utf-8')
rabbit_mq_host = os.getenv('RABBIT_MQ_HOST', 'localhost')
rabbit_mq_port = os.getenv('RABBIT_MQ_PORT', 5672)
text_rl_exchange = os.getenv('TEXT_RL_EXCHANGE', 'text-rl.treatment')
text_rl_exchange_type = os.getenv('TEXT_RL_EXCHANGE_TYPE', 'topic')
treatment_done_routing_key = os.getenv('TREATMENT_DONE_ROUTING_KEY', 'text-rl.treatment.done')
treatment_pending_routing_key = os.getenv('TREATMENT_PENDING_ROUTING_KEY', 'text-rl.treatment.pending')

print('DEFAULT_ENCODING', default_encoding)
print('RABBIT_MQ_HOST', rabbit_mq_host)
print('RABBIT_MQ_PORT', rabbit_mq_port)
print('TEXT_RL_EXCHANGE', text_rl_exchange)
print('TEXT_RL_EXCHANGE_TYPE', text_rl_exchange_type)
print('TREATMENT_DONE_ROUTING_KEY', treatment_done_routing_key)
print('TREATMENT_PENDING_ROUTING_KEY', treatment_pending_routing_key)
