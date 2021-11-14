class RabbitMqSettings:
    def __init__(self, host: str, exchange, routing_key, port: int = 5672, exchange_type: str = '', username: str = '',
                 password: str = ''):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.exchange = exchange
        self.exchange_type = exchange_type
        self.routing_key = routing_key
