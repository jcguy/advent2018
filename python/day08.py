from InputReader import read_input


def process_node(stack):
    num_children = stack.pop()
    num_meta = stack.pop()

    child_values = [process_node(stack) for _ in range(num_children)]
    meta = [stack.pop() for _ in range(num_meta)]

    value = 0

    value = sum(child_values[m - 1][1]
                for m in meta
                if 0 <= m - 1 < len(child_values))

    if not child_values:
        value = sum(meta)

    return sum(meta) + sum(c[0] for c in child_values), value


def a():
    inp = read_input(8)[0]
    stack = list(map(int, inp.split()))[::-1]

    meta_sum, _ = process_node(stack)

    return meta_sum


def b():
    inp = read_input(8)[0]
    stack = list(map(int, inp.split()))[::-1]

    _, value = process_node(stack)

    return value


if __name__ == "__main__":
    print(a())
    print(b())
