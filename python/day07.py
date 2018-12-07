from string import ascii_uppercase
from queue import PriorityQueue
from InputReader import read_input


def read_graph():
    edges = read_input(7)
    edges = [(edge[5], edge[36]) for edge in edges]

    nodes = set()

    for s, d in edges:
        nodes.add(s)
        nodes.add(d)

    graph = {node: [] for node in nodes}

    for edge in edges:
        graph[edge[1]].append(edge[0])

    return graph, nodes


def a():
    graph, _ = read_graph()
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


def get_time(step):
    return 60 + ascii_uppercase.index(step) + 1


def b():
    graph, nodes = read_graph()

    q = PriorityQueue()

    for node, inc in graph.items():
        if not inc:
            q.put(node)

    seconds = -1
    workers = [(0, None)] * 5

    while nodes or any(w[0] for w in workers):
        for i, (time, item) in enumerate(workers):
            if not time or not item:
                continue
            workers[i] = (time - 1, item)

        for i, (time, item) in enumerate(workers):
            if time or not item:
                continue
            for node, inc in graph.items():
                if item in inc:
                    inc.remove(item)
                    if not inc:
                        q.put(node)
            nodes.discard(item)
            workers[i] = (0, None)

        for i, (time, item) in enumerate(workers):
            if not item and not q.empty():
                next_item = q.get()
                workers[i] = (get_time(next_item), next_item)

        seconds += 1

    return seconds


if __name__ == "__main__":
    print(a())
    print(b())
