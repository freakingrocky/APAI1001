from random import choice

class Node:
    """Node Data Structure for Basic Search."""

    def __init__(self, state, parent, action, distance):
        self.state = state
        self.parent = parent
        self.action = action
        self.distance = parent.distance + distance if parent else 0
        self.depth = parent.depth + 1 if parent else 0


class RandomFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = choice(self.frontier)
            self.frontier.remove(node)
            return node
