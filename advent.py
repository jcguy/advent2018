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
        try:
            return freqs[freq]
        except KeyError:
            freqs[freq] = freq
        freq += change


def day02a():
    words = read_input('input.02')

    value = [
        sum(2 in {c: w.count(c) for c in w}.values() for w in words),
        sum(3 in {c: w.count(c) for c in w}.values() for w in words)
    ]

    return value[0] * value[1]


def day02b():
    from itertools import product
    words = read_input('input.02')

    for word1, word2 in product(words, repeat=2):
        diffs = [i for i, (a, b) in enumerate(zip(word1, word2)) if a != b]
        if len(diffs) == 1:
            return word1[:diffs[0]] + word1[diffs[0]+1:]


def day03a():
    claims = read_input('input.03')
    fabric = [[0 for _ in range(1000)] for _ in range(1000)]

    for claim in claims:
        ident, _, xy, wl = claim.split()
        x, y = map(int, xy.strip(":").split(","))
        w, l = map(int, wl.split("x"))

        for ix in range(x, x + w):
            for iy in range(y, y + l):
                fabric[ix][iy] += 1

    return sum([sum([1 for x in row if x > 1]) for row in fabric])


def day03b():
    claims = read_input('input.03')
    fabric = [[[] for _ in range(1000)] for _ in range(1000)]
    idents = set()

    for claim in claims:
        ident, _, xy, wl = claim.split()
        x, y = map(int, xy.strip(":").split(","))
        w, l = map(int, wl.split("x"))
        ident = int(ident.strip("#"))

        idents.add(ident)

        for ix in range(x, x + w):
            for iy in range(y, y + l):
                fabric[ix][iy].append(ident)

    for row in fabric:
        for x in row:
            if len(x) > 1:
                for ident in x:
                    idents.discard(ident)

    return idents.pop()


print()
print(day03a())
print(day03b())
