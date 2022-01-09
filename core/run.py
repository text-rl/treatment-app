import py_compile as pyc
import os


# TODO identify and labelise Entity
def identify_entity(text):
    res = []

    # TODO blacklist

    # TODO regex

    # TODO patern matching

    # TODO NER

    return res


# TODO anonimyse entity
def anonymize(text):
    return text


def main():
    res = anonymize("test")
    print(res)


if __name__ == "__main__":
    main()

    # uid = UserId(value="1")
    # data = {
    #     "user_id": uid,
    #     "content": "test"
    # }
    #
    # new_message = TreatmentDoneMessage(user_id=data["user_id"], result=data['content'])
    # new_message.result = "test2"
    # print(new_message.result)
