from InputReader import read_input


def a():
    from string import ascii_lowercase
    words = read_input(2)

    value = [0, 0]
    for w in words:
        counts = [w.count(c) for c in ascii_lowercase]
        value[0] += (2 in counts)
        value[1] += (3 in counts)

    return value[0] * value[1]


def b():
    words = read_input(2)

    possible_matches = set()
    for word in words:
        new_set = set()
        for i, _ in enumerate(word):
            new_word = word[:i] + word[i + 1:]
            if new_word in possible_matches:
                return new_word
            new_set.add(new_word)
        possible_matches |= new_set

    return None
