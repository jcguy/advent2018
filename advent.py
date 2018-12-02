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
    two_count = 0
    three_count = 0

    for word in words:
        counts = {char: word.count(char) for char in word}
        if 2 in counts.values():
            two_count += 1
        if 3 in counts.values():
            three_count += 1

    return two_count * three_count


def day02b():
    words = read_input('input.02')

    def num_different(word1, word2):
        diff_count = 0
        diff = []
        for a, b in zip(word1, word2):
            if a != b:
                diff_count += 1
                diff.append(a)
            if diff_count > 1:
                return diff_count, None

        if diff_count != 0:
            return diff_count, "".join(word1.split(diff[0]))
        else:
            return diff_count, None

    for word1 in words:
        for word2 in words:
            n, remaining = num_different(word1, word2)
            if n == 1:
                return remaining


print(day02a())
print(day02b())
