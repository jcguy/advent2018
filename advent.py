def read_input(filename):
    with open(filename) as f:
        return [line.strip("\n") for line in f.readlines()]


def day01a():
    return sum(map(int, read_input("input.01")))


def day01b():
    from itertools import cycle
    deltas = map(int, read_input("input.01"))
    freq = 0
    freqs = set()
    for delta in cycle(deltas):
        if freq in freqs:
            return freq
        freqs.add(freq)
        freq += delta


def day02a():
    from string import ascii_lowercase
    words = read_input('input.02')

    value = [0, 0]
    for w in words:
        counts = [w.count(c) for c in ascii_lowercase]
        value[0] += (2 in counts)
        value[1] += (3 in counts)

    return value[0] * value[1]


def day02b():
    from itertools import product
    words = read_input('input.02')

    possible_matches = set()
    for word in words:
        new_set = set()
        for i, _ in enumerate(word):
            new_word = word[:i] + word[i+1:]
            if new_word in possible_matches:
                return new_word
            new_set.add(new_word)
        possible_matches |= new_set


def day03a():
    claims = read_input('input.03')
    fabric = {}

    for claim in claims:
        ident, _, xy, wl = claim.split()
        x, y = map(int, xy.strip(":").split(","))
        w, l = map(int, wl.split("x"))

        for ix in range(x, x + w):
            for iy in range(y, y + l):
                fabric[(ix, iy)] = fabric.get((ix, iy), 0) + 1

    return len(list(filter(lambda x: x > 1, fabric.values())))


def day03b():
    claims = read_input('input.03')
    fabric = {}

    idents = set()

    for claim in claims:
        ident, _, xy, wl = claim.split()
        x, y = map(int, xy.strip(":").split(","))
        w, l = map(int, wl.split("x"))

        idents.add(ident)

        for ix in range(x, x + w):
            for iy in range(y, y + l):
                fabric[(ix, iy)] = fabric.get((ix, iy), [])
                fabric[(ix, iy)].append(ident)

    for overlap in filter(lambda x: len(x) > 1, fabric.values()):
        for ident in overlap:
            idents.discard(ident)

    return idents.pop()



for _ in range(1000):
    day02b()
