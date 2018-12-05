from InputReader import read_input


def a():
    claims = read_input(3)
    fabric = [[0 for _ in range(1000)] for _ in range(1000)]

    for claim in claims:
        ident, _, xy, wl = claim.split()
        x, y = map(int, xy.strip(":").split(","))
        w, l = map(int, wl.split("x"))

        for ix in range(x, x + w):
            for iy in range(y, y + l):
                fabric[ix][iy] += 1

    total = 0
    for row in fabric:
        for x in row:
            if x > 1:
                total += 1
    return total


def b():
    claims = read_input(3)
    fabric = [[[] for _ in range(1000)] for _ in range(1000)]

    idents = set()

    for claim in claims:
        ident, _, xy, wl = claim.split()
        x, y = map(int, xy.strip(":").split(","))
        w, l = map(int, wl.split("x"))

        idents.add(ident)

        for ix in range(x, x + w):
            for iy in range(y, y + l):
                if fabric[ix][iy]:
                    idents.discard(fabric[ix][iy][-1])
                    idents.discard(ident)
                    if len(idents) == 1:
                        return idents.pop()
                fabric[ix][iy].append(ident)

    return idents.pop()
