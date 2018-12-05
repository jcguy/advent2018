def read_input(day):
    filename = "../input/input.{:02d}".format(day)
    with open(filename) as f:
        return [line.strip("\n") for line in f.readlines()]
