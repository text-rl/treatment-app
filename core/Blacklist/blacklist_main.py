from core.Blacklist.location.location_blacklist_main import loading_location_blacklist
from core.Blacklist.person.person_blacklist_main import loading_person_blacklist


def main():
    person_blacklist = loading_person_blacklist()

    location_blacklist = loading_location_blacklist()


if __name__ == "__main__":
    main()
