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

        time = []
        for i in range(num_cycles):
            time.append(int(shift[2 * i + 1].split(":")[1].split("]")[0]))
            time.append(int(shift[2 * i + 2].split(":")[1].split("]")[0]))

        try:
            guards[guard] += time
        except KeyError:
            guards[guard] = time

    sleep_lengths = {}
    for guard, times in guards.items():
        for i in range(len(times) // 2):
            try:
                sleep_lengths[guard] += times[2 * i + 1] - times[2 * i]
            except KeyError:
                sleep_lengths[guard] = times[2 * i + 1] - times[2 * i]

    sleepiest_guard = 0
    guard_minutes = 0

    for guard, length in sleep_lengths.items():
        if length > guard_minutes:
            sleepiest_guard = guard
            guard_minutes = length

    sleepiest_minute = 0
    days_slept = 0

    for minute in range(60):
        num_days = 0
        for i in range(len(guards[sleepiest_guard]) // 2):
            if minute in range(guards[sleepiest_guard][2 * i],
                               guards[sleepiest_guard][2 * i + 1]):
                num_days += 1
        if num_days > days_slept:
            days_slept = num_days
            sleepiest_minute = minute

    return sleepiest_minute * sleepiest_guard


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

        time = []
        for i in range(num_cycles):
            time.append(int(shift[2 * i + 1].split(":")[1].split("]")[0]))
            time.append(int(shift[2 * i + 2].split(":")[1].split("]")[0]))

        try:
            guards[guard] += time
        except KeyError:
            guards[guard] = time

    minutes_asleep = {}

    for guard, times in guards.items():
        for i in range(len(times) // 2):
            try:
                minutes_asleep[guard] += list(range(times[2 * i],
                                                    times[2 * i + 1]))
            except KeyError:
                minutes_asleep[guard] = list(range(times[2 * i],
                                                   times[2 * i + 1]))

    most_days = 0
    most_guard = 0
    most_minute = 0

    for guard, minutes in minutes_asleep.items():
        days = 0
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
