import random

import requests


def get_berries() -> dict:
    berry = dict()
    berry_list = requests.get(
        "https://pokeapi.co/api/v2/berry?limit=64"
    ).json()["results"]
    for i in berry_list:
        details = dict()
        berry_details = requests.get(i["url"]).json()
        details["firmness"] = berry_details["firmness"]["name"]
        details["flavors"] = [
            f'{x["flavor"]["name"]}: {x["potency"]}'
            for x in berry_details["flavors"]
        ]
        details["growth_time"] = berry_details["growth_time"]
        details["id"] = berry_details["id"]
        details["max_harvest"] = berry_details["max_harvest"]
        details["name"] = berry_details["name"]
        details["size"] = berry_details["size"]
        details["smoothness"] = berry_details["smoothness"]
        details["soil_dryness"] = berry_details["soil_dryness"]
        berry[i["name"]] = details

    return berry


def add_random_order(data: dict):
    regions = [
        "Kanto",
        "Johto",
        "Hoenn",
        "Sinnoh",
        "Unova",
        "Kalos",
        "Alola",
        "Galar",
        "Paldea",
    ]
    result = list()
    for region in regions:
        for y in data.values():
            copy = y.copy()
            copy["sales"] = random.randint(1, 999) * 1000
            copy["region"] = region
            result.append(copy)
    return result


def write_to_csv(data: list) -> None:
    with open("berries_sales.csv", "w") as fd:
        for line in data:
            """
            items = [x for x in y.items()]
            string = ""
            for i in items:
                string += f"{i}"
                string += ";"
            fd.write(f"{string}\n")
            """
            fd.write(f"{line}\n")
    return


def main() -> None:
    write_to_csv(add_random_order(get_berries()))


if __name__ == "__main__":
    main()
