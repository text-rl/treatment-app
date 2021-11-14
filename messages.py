from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserId:
    value: str


@dataclass
class RunTextTreatmentMessage:
    user_id: UserId
    content: str
    date_time: datetime


@dataclass
class TreatmentDoneMessage:
    user_id: UserId
    result: str
