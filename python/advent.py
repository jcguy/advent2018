#!/usr/bin/env python3
import day01
import day02
import day03
import day04
import day05
import day06
import day07
import day08


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
        day06.a,
        day06.b,
        day07.a,
        day07.b,
        day08.a,
        day08.b,
    ]

    if len(argv) == 1:
        day = 1
        for solution in solutions:
            if solution.__name__ == "a":
                print("Day {}:".format(day))
            else:
                day += 1
            print("  Part {}: {}".format(solution.__name__, solution()))
    elif len(argv) == 2:
        day = int(argv[1])
        print("Day {}:".format(day))
        print("  Part {}: {}".format("a", solutions[2 * day - 2]()))
        print("  Part {}: {}".format("b", solutions[2 * day - 1]()))
    elif len(argv) == 3:
        day = int(argv[1])
        part = argv[2]
        print("Day {}:".format(day))
        print("  Part {}: ".format(part), end="")
        if part == "a":
            print(solutions[2 * day - 2]())
        elif part == "b":
            print(solutions[2 * day - 1]())


if __name__ == "__main__":
    import sys
    main(sys.argv)
    in_emacs = False
