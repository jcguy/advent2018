def read_input(filename):
    with open(filename) as f:
        return [line.strip("\n") for line in f.readlines()]


def day01a():
    changes = map(int, read_input("input.01"))
    return sum(changes)


def day01b():
    from itertools import cycle
    changes = map(int, read_input("input.01"))
    freq = 0
    freqs = {}
    for change in cycle(changes):
        freq += change
        try:
            return freqs[freq]
        except KeyError:
            freqs[freq] = freq


print(day01b())
