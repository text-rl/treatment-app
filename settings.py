import dataclasses


@dataclasses.dataclass
class RabbitMqSettings:
    host: str
    exchange: str
    routing_key: str
    port: int = 5672
    exchange_type: str = ''
    username: str = ''
    password: str = ''
