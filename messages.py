class UserId:
    def __init__(self, value: str):
        self.value = value


class TreatmentDoneMessage:
    def __init__(self, user_id: UserId, result: str):
        self.result = result
        self.id = user_id
