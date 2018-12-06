from InputReader import read_input


def react(polymer):
    stack = []

    for unit in polymer:
        if not stack:
            stack.append(unit)
        elif (ord(unit) ^ ord(stack[-1])) == 32:
            stack.pop()
        else:
            stack.append(unit)

    return stack


def a():
    polymer = read_input(5)[0]
    return len(react(polymer))


def b():
    from string import ascii_lowercase
    polymer = react(read_input(5)[0])
    lengths = []

    for unit in ascii_lowercase:
        lengths.append(len(react([u for u in polymer if u.lower() != unit])))

    return min(lengths)
