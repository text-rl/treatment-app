from core.utils import loading_blacklist_db


def extract_names(filename, outFile):
    with open(filename, "r", encoding="utf-8") as rf:
        with open(outFile, "a", encoding="utf-8") as wf:
            for row in rf:
                wf.write(row.split(",")[0] + "\n")


def cleaning_name_db():
    extract_names("data/person/first_names.all.csv", "data/person/person_names_clean.csv")
    extract_names("data/person/last_names.all.csv", "data/person/person_names_clean.csv")


def loading_person_blacklist(cleaning=False):
    if cleaning:
        cleaning_name_db()

    name_blacklist = loading_blacklist_db("data/person/person_names_clean.csv", "per")

    # testing
    assert "Alahmrey" in name_blacklist, "Error in person blacklist loading"
    assert "Sourohsbfuebfdncsifjdeep" not in name_blacklist, "Error in person blacklist loading"

    return name_blacklist
