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
    fabric = []
    for _ in range(1000):
        fabric.append([])

    for r in fabric:
        for _ in range(1000):
            r.append(0)

    for claim in claims:
        ident, _, xy, wl = claim.split()
        x, y = xy.strip(":").split(",")
        w, l = wl.split("x")

        x = int(x)
        y = int(y)
        w = int(w)
        l = int(l)

        for ix in range(w):
            for iy in range(l):
                fabric[x + ix][y + iy] += 1

    total = 0
    for row in fabric:
        for col in row:
            if col > 1:
                total += 1

    return total


def day03b():
    claims = read_input('input.03')
    fabric = []
    for _ in range(1000):
        fabric.append([])

    for r in fabric:
        for _ in range(1000):
            r.append([])

    idents = set()

    for claim in claims:
        ident, _, xy, wl = claim.split()
        x, y = xy.strip(":").split(",")
        w, l = wl.split("x")

        idents.add(ident)

        x = int(x)
        y = int(y)
        w = int(w)
        l = int(l)

        for ix in range(w):
            for iy in range(l):
                fabric[x + ix][y + iy].append(ident)

    for row in fabric:
        for col in row:
            if len(col) != 1:
                for ident in col:
                    idents.discard(ident)

    return idents


print()
print(day03a())
print(day03b())
