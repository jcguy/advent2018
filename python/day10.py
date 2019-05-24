import re
from InputReader import read_input


def a():
    inp = read_input(9)[0]
    n, m = map(int, re.findall(r"\d+", inp))
    return inp


def b():
    inp = read_input(9)[0]
    n, m = map(int, re.findall(r"\d+", inp))
    return inp


if __name__ == "__main__":
    from advent import run_solution
    run_solution(a, False)
    run_solution(b, False)
