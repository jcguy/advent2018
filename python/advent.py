#!/usr/bin/env python3
import day01
import day02
import day03
import day04
import day05
import day06
import day07
import day08


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


def run_solution(solution, time=False):
    if not time:
        print("Day {}, part {}:  {}"
              .format(solution.__module__[-2:],
                      solution.__name__,
                      solution()))
        return

    from statistics import mean, median, stdev
    from time import clock_gettime_ns, CLOCK_MONOTONIC

    run_times = []
    for _ in range(100):
        start_time = clock_gettime_ns(CLOCK_MONOTONIC)
        solution()
        end_time = clock_gettime_ns(CLOCK_MONOTONIC)
        run_times.append(end_time - start_time)

        if (sum(run_times) / 1e9) > 10:
            break

    print("Day {}, part {}:".format(solution.__module__[-2:],
                                    solution.__name__),
          end="  ")
    # print("Day {}, part {}:".format(solution.__module__[-2:],
    #                                 solution.__name__))

    # in ms
    mean_rt = mean(run_times) / 1e6
    # median_rt = median(run_times) / 1e6
    # stdev_rt = stdev(run_times) / 1e6

    print("{:6.2f} ms".format(mean_rt))
    # print("\tmedian:\t {:6.2f} ms".format(median_rt))
    # print("\tstdev: \t {:6.2f} ms".format(stdev_rt))


def get_solutions(argv):
    if len(argv) == 1:
        sols = solutions

    elif len(argv) == 2:
        day = int(argv[1])
        sols = solutions[2 * day - 2:2 * day]

    elif len(argv) == 3:
        day = int(argv[1])
        part = argv[2]
        sols = [solutions[2 * day - 2]
                if part == "a" else
                solutions[2 * day - 1]]

    return sols


def main(argv):
    if len(argv) > 1 and argv[1] == "time":
        _ = [run_solution(s, True) for s in get_solutions(argv[:1] + argv[2:])]
    else:
        _ = [run_solution(s) for s in get_solutions(argv)]


if __name__ == "__main__":
    import sys
    main(sys.argv)
