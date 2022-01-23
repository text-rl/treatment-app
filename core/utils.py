

def loading_blacklist_db(filename_data, label):
    blacklist = {}
    count = 0
    with open(filename_data, "r", encoding="utf-8") as rf:
        for row in rf:
            name = row.strip("\n")
            if name not in blacklist:
                blacklist[name] = label
                count += 1
    print(count)
    return blacklist
