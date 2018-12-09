from InputReader import read_input
from collections import deque
import re


def solve(num_players, highest_marble):
    scores = [0] * num_players
    circle = deque([0])

    for marble in range(1, highest_marble + 1):
        if marble % 23:
            circle.rotate(-1)
            circle.append(marble)
        else:
            circle.rotate(7)
            scores[marble % num_players] += circle.pop() + marble
            circle.rotate(-1)

    return max(scores)


def a():
    inp = read_input(9)[0]
    n, m = map(int, re.findall(r"\d+", inp))
    return solve(n, m)


def b():
    inp = read_input(9)[0]
    n, m = map(int, re.findall(r"\d+", inp))
    return solve(n, m * 100)


if __name__ == "__main__":
    from advent import run_solution
    run_solution(a, True)
    run_solution(b, True)
