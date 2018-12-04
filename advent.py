#!/usr/bin/env python3


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


def day03b():
    claims = read_input('input.03')
    fabric = [[[] for _ in range(1000)] for _ in range(1000)]

    idents = set()

    for claim in claims:
        ident, _, xy, wl = claim.split()
        x, y = map(int, xy.strip(":").split(","))
        w, l = map(int, wl.split("x"))

        idents.add(ident)

        for ix in range(x, x + w):
            for iy in range(y, y + l):
                if len(fabric[ix][iy]) > 0:
                    idents.discard(fabric[ix][iy][-1])
                    idents.discard(ident)
                    if len(idents) == 1:
                        return idents.pop()
                fabric[ix][iy].append(ident)

    return idents.pop()


def day04a():
    times = sorted(read_input("input.04"))

    shifts = []

    for time in times:
        if "Guard" in time:
            shifts.append([time])
        elif "asleep" in time or "wakes" in time:
            shifts[-1].append(time)

    guards = {}

    for shift in shifts:
        guard = int(shift[0].split()[3][1:])
        num_cycles = len(shift) // 2

        for i in range(num_cycles):
            start_time = int(shift[2 * i + 1].split(":")[1].split("]")[0])
            end_time = int(shift[2 * i + 2].split(":")[1].split("]")[0])
            guards[guard] = guards.get(guard, []) + list(range(start_time, end_time))

    minutes_asleep = 0
    sleepiest_guard = 0
    sleepiest_minute = 0

    for guard, minutes in guards.items():
        if len(minutes) > minutes_asleep:
            minutes_asleep = len(minutes)
            sleepiest_guard = guard
            counts = [minutes.count(m) for m in range(60)]
            sleepiest_minute = counts.index(max(counts))

    return sleepiest_guard * sleepiest_minute


def day04b():
    times = sorted(read_input("input.04"))

    shifts = []

    for time in times:
        if "Guard" in time:
            shifts.append([time])
        elif "asleep" in time or "wakes" in time:
            shifts[-1].append(time)

    guards = {}

    for shift in shifts:
        guard = int(shift[0].split()[3][1:])
        num_cycles = len(shift) // 2

        for i in range(num_cycles):
            start_time = int(shift[2 * i + 1].split(":")[1].split("]")[0])
            end_time = int(shift[2 * i + 2].split(":")[1].split("]")[0])
            guards[guard] = guards.get(guard, []) + list(range(start_time, end_time))

    most_days = 0
    most_guard = 0
    most_minute = 0

    for guard, minutes in guards.items():
        for m in minutes:
            if minutes.count(m) > most_days:
                most_days = minutes.count(m)
                most_guard = guard
                most_minute = m

    return most_guard * most_minute


def main(argv):
    solutions = [
        day01a,
        day01b,
        day02a,
        day02b,
        day03a,
        day03b,
        day04a,
        day04b,
    ]

    if len(argv) == 1:
        for solution in solutions:
            print(solution())
    elif len(argv) == 2:
        day = int(argv[1])
        print(solutions[2 * day - 2]())
        print(solutions[2 * day - 1]())
    elif len(argv) == 3:
        day = int(argv[1])
        part = argv[2]
        if part == "a":
            print(solutions[2 * day - 2]())
        elif part == "b":
            print(solutions[2 * day - 1]())


main(["", 4])

# in_emacs = True
# if __name__ == "__main__":
#     import sys
#     main(sys.argv)
#     in_emacs = False

# if in_emacs:
#     print()
#     main(["", "3"])
