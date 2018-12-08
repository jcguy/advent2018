from os.path import isfile
from requests import get


def read_input(day):
    filename = "../input/input.{:02d}".format(day)
    if not isfile(filename):
        with open("../.token") as f:
            session = f.readlines()[0].strip()

        url = "https://adventofcode.com/2018/day/{}/input".format(day)
        response = get(url, cookies={"session": session})

        if response.status_code != 200:
            return []

        with open(filename, "w") as f:
            f.write(response.content.decode("utf-8"))

    with open(filename) as f:
        return [line.strip("\n") for line in f.readlines()]
