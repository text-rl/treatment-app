from core.utils import loading_blacklist_db


def extract_names(filename, outFile):
    count = 0
    with open(filename, "r", encoding="utf-8") as rf:
        with open(outFile, "w", encoding="utf-8") as wf:
            for row in rf:
                row = row.strip("\n").split("\t")
                names = [row[1], row[2]]
                for name in row[3].split(","):
                    if name:
                        names.append(name)
                count += len(names)
                wf.write("\n".join(names) + "\n")

    print(count)


def cleaning_location_db():
    extract_names("data/location/allCountries.txt", "data/location/locations.csv")


def loading_location_blacklist(cleaning=False):
    if cleaning:
        cleaning_location_db()
    location_blacklist = loading_blacklist_db("data/location/locations.csv", "geo")

    # testing
    assert "Port des Bareytes" in location_blacklist, "Error in person blacklist loading"
    assert "Sourohsbfuebfdncsifjdeep" not in location_blacklist, "Error in person blacklist loading"

    return location_blacklist
