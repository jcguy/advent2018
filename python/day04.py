from InputReader import read_input


def a():
    times = sorted(read_input(4))

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

        for i in range(num_cycles):
            start_time = int(shift[2 * i + 1].split(":")[1].split("]")[0])
            end_time = int(shift[2 * i + 2].split(":")[1].split("]")[0])
            guards[guard] = guards.get(guard, []) + list(range(start_time, end_time))

    minutes_asleep = 0
    sleepiest_guard = 0
    sleepiest_minute = 0

    for guard, minutes in guards.items():
        if len(minutes) > minutes_asleep:
            minutes_asleep = len(minutes)
            sleepiest_guard = guard
            counts = [minutes.count(m) for m in range(60)]
            sleepiest_minute = counts.index(max(counts))

    return sleepiest_guard * sleepiest_minute


def b():
    times = sorted(read_input(4))

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

        for i in range(num_cycles):
            start_time = int(shift[2 * i + 1].split(":")[1].split("]")[0])
            end_time = int(shift[2 * i + 2].split(":")[1].split("]")[0])
            guards[guard] = guards.get(guard, []) + list(range(start_time, end_time))

    most_days = 0
    most_guard = 0
    most_minute = 0

    for guard, minutes in guards.items():
        for m in minutes:
            if minutes.count(m) > most_days:
                most_days = minutes.count(m)
                most_guard = guard
                most_minute = m

    return most_guard * most_minute
