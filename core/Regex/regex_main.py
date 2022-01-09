import re

test_names = [
    ["Alexandre", True],
    ["ALEXANDRE", True],
    ["Davoine", True],
    ["DAVOINE", True],
    ["Étienne", True],
    ["Jean-Eude", True],
    ["Eloïse", True],
    ["8732170938", False],
    ["cheval", False],
    ["manutention", False],
    ["test", False],
    ["a@gmail.com", False],
    # ["Paris", False]
]

test_emails = [
    ["a@gmail.com", True],
    ["test-1.charles@free.fr", True],
    ["45668.2324@gmail.com", True],
    ["tatas@ass", False],
    ["adxsxasawdxawx.cw", False],
    ["awdawd@awd@awd.com", False],
    ["123456.com", False],
]


def test_regex(name, data, regex):
    for elem in data:
        res = re.findall(regex, elem[0])

        assert (len(res) == 1) == elem[1], "Error in regex of {} for '{}'".format(name, elem[0])


def main():
    # names
    test_regex("names", test_names, r"[A-ZÀ-ÖØ-ß][A-Za-zÀ-ÖØ-öø-ÿ-]+")

    # email
    test_regex("emails", test_emails, r"^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$")

    # date

    # time

    # value


if __name__ == "__main__":
    main()
