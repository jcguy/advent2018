from InputReader import read_input
import re


class Node:
    def __init__(self, value, pre=None, nex=None):
        self.value = value
        self.pre = pre
        self.nex = nex


class LinkedList:
    def __init__(self, starting_value):
        self.node = Node(starting_value)
        self.node.pre = self.node
        self.node.nex = self.node

    def cycle(self, n):
        if n == 0:
            return
        if n > 0:
            for _ in range(n):
                self.node = self.node.nex
            return
        if n < 0:
            for _ in range(-n):
                self.node = self.node.pre
            return

    def insert(self, value):
        new_node = Node(value, self.node, self.node.nex)
        self.node.nex.pre = new_node
        self.node.nex = new_node
        self.node = new_node

    def delete(self):
        deleted_node = self.node
        self.node.nex.pre = self.node.pre
        self.node.pre.nex = self.node.nex
        value = self.node.value
        self.node = self.node.nex
        del deleted_node
        return value


def solve(num_players, highest_marble):
    scores = [0] * num_players
    circle = LinkedList(0)
    player = 0

    for marble in range(1, highest_marble + 1):
        if marble % 23 == 0:
            scores[player] += marble
            circle.cycle(-7)
            scores[player] += circle.delete()
        else:
            circle.cycle(1)
            circle.insert(marble)

        player += 1
        player %= num_players

    return max(scores)


def a():
    inp = read_input(9)[0]
    n, m = map(int, re.match(r"(\d+)[^\d]+(\d+)", inp).groups())
    return solve(n, m)


def b():
    inp = read_input(9)[0]
    n, m = map(int, re.match(r"(\d+)[^\d]+(\d+)", inp).groups())
    return solve(n, m * 100)


if __name__ == "__main__":
    print(a())
    print(b())
