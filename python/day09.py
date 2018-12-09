from InputReader import read_input
from collections import deque
import re


def solve(num_players, highest_marble):
    scores = [0] * num_players
    player = 0
    circle = deque([0])

    for marble in range(1, highest_marble + 1):
        if marble % 23:
            circle.rotate(-1)
            circle.append(marble)
        else:
            circle.rotate(7)
            scores[player] += circle.pop() + marble
            circle.rotate(-1)

        player = (player + 1) % num_players

    return max(scores)


def a():
    inp = read_input(9)[0]
    n, m = map(int, re.match(r"(\d+)[^\d]+(\d+)", inp).groups())
    return solve(n, m)


def b():
    inp = read_input(9)[0]
    n, m = map(int, re.match(r"(\d+)[^\d]+(\d+)", inp).groups())
    return solve(n, m * 100)


if __name__ == "__main__":
    print(a())
    print(b())
