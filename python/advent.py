#!/usr/bin/env python3
import day01
import day02
import day03
import day04
import day05


def main(argv):
    solutions = [
        day01.a,
        day01.b,
        day02.a,
        day02.b,
        day03.a,
        day03.b,
        day04.a,
        day04.b,
        day05.a,
        day05.b,
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


if __name__ == "__main__":
    import sys
    main(sys.argv)
    in_emacs = False
