from InputReader import read_input


def process_node(stack):
    num_children = stack.pop()
    num_meta = stack.pop()

    value = 0

    children_values = []
    for _ in range(num_children):
        children_values.append(process_node(stack))

    meta = []
    for _ in range(num_meta):
        meta.append(stack.pop())

    if not num_children:
        value = sum(meta)
    else:
        for m in meta:
            if m - 1 < len(children_values):
                value += children_values[m - 1][1]

    return sum(meta) + sum([c[0] for c in children_values]), value


def a():
    inp = read_input(8)[0]
    inp = list(map(int, inp.split()))
    stack = inp[::-1]

    meta_data_sum, _ = process_node(stack)

    return meta_data_sum


def b():
    inp = read_input(8)[0]
    inp = list(map(int, inp.split()))
    stack = inp[::-1]

    _, value = process_node(stack)

    return value


if __name__ == "__main__":
    print(a())
    print(b())
