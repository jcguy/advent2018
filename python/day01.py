from InputReader import read_input


def a():
    return sum(map(int, read_input(1)))


def b():
    from itertools import cycle
    deltas = map(int, read_input(1))
    freq = 0
    freqs = set()
    for delta in cycle(deltas):
        if freq in freqs:
            return freq
        freqs.add(freq)
        freq += delta

    return None
