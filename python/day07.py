from string import ascii_uppercase
from queue import PriorityQueue
from InputReader import read_input


def a():
    edges = read_input(7)
    edges = [(edge[5], edge[36]) for edge in edges]

    nodes = set()

    for s, d in edges:
        nodes.add(s)
        nodes.add(d)

    graph = {node: [] for node in nodes}

    for edge in edges:
        graph[edge[1]].append(edge[0])

    q = PriorityQueue()

    for node, inc in graph.items():
        if not inc:
            q.put(node)

    process = ""

    while not q.empty():
        item = q.get()
        process += item
        for node, inc in graph.items():
            if item in inc:
                graph[node].remove(item)
                if not graph[node]:
                    q.put(node)

    return process


def b():
    steps = read_input(7)
    steps = [[step[5], step[36]] for step in steps]

    set_steps = set()

    for step in steps:
        set_steps.add(step[0])
        set_steps.add(step[1])

    graph = {step: [] for step in set_steps}

    for step in steps:
        graph[step[1]].append(step[0])

    start = [step for step in graph.keys() if not graph[step]]

    q = PriorityQueue()

    for step in start:
        q.put(step)

    workers = [0] * 5
    worker_items = [None] * 5

    remaining = set()
    for step0, step1 in graph.items():
        remaining.add(step0)
        for step in step1:
            remaining.add(step)

    for second in range(1000):
        for i, worker in enumerate(workers):
            if worker != 0:
                continue

            if worker_items[i]:
                for step in graph.keys():
                    if worker_items[i] in graph[step]:
                        graph[step].remove(worker_items[i])
                        if not graph[step]:
                            q.put(step)
                worker_items[i] = None

            if not q.empty():
                item = q.get()
                remaining.discard(item)
                workers[i] = 60 + 1 + ascii_uppercase.index(item)
                worker_items[i] = item

        for i, worker in enumerate(workers):
            if worker > 0:
                workers[i] -= 1

        if not remaining and all(not worker for worker in workers):
            break

    return second


if __name__ == "__main__":
    print(a())
    print(b())
