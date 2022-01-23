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

test_dates = [
    ["11-22-11", True],
    ["11/11/1111", True],
    ["1111/11/11", True],
    ["11-22-11", True],
    ["11-11-1111", True],
    ["1111-11-11", True],
    ["11\\22\\11", True],
    ["11\\11\\1111", True],
    ["1111\\11\\11", True],
    ["1234/1234/1234", False],
    ["12345678", False],
    ["12/12", False],
    ["", False],
]

test_times = [
    ["01-11", True],
    ["11:02", True],
    ["23h34", True],
    ["29:11", False],
    ["01:1", False],
    ["de", False],
    ["3n23", False],
    ["3h79", False],
]


def test_regex(name, data, regex):
    for elem in data:
        res = re.findall(regex, elem[0])
        assert (len(res) == 1) == elem[1], "Error in regex of {} for '{}'".format(name, elem[0])


def main():
    # names
    # test_regex("names", test_names, r"[A-ZÀ-ÖØ-ß][A-Za-zÀ-ÖØ-öø-ÿ-]+")

    # email
    # test_regex("emails", test_emails, r"^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$")

    # date
    # test_regex("dates", test_dates, r"[0-9]{2}-[0-9]{2}-[0-9]{2}|"
    #                                 "[0-9]{4}-[0-9]{2}-[0-9]{2}|"
    #                                 "[0-9]{2}-[0-9]{2}-[0-9]{2}|"
    #                                 "[0-9]{2}\/[0-9]{2}\/[0-9]{4}|"
    #                                 "[0-9]{4}\/[0-9]{2}\/[0-9]{2}|"
    #                                 "[0-9]{2}\/[0-9]{2}\/[0-9]{2}|"
    #                                 "[0-9]{2}\\\\[0-9]{2}\\\\[0-9]{4}|"
    #                                 "[0-9]{4}\\\\[0-9]{2}\\\\[0-9]{2}|"
    #                                 "[0-9]{2}\\\\[0-9]{2}\\\\[0-9]{2}")

    # time
    test_regex("time", test_times, r"(?:[0][0-9]|[1][0-9]|2[0-3])[-:hH][0-5][0-9]")


if __name__ == "__main__":
    main()
