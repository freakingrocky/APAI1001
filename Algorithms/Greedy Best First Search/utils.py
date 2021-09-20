from random import choice


class Node:
    """Node Data Structure for Search."""

    def __init__(self, state, parent, action, h):
        self.state = state
        self.parent = parent
        self.action = action
        self.heuristic = h
        self.depth = parent.depth + 1 if parent else 0


class PriorityFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        print("CALLED:", node.state)
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            min_cost = 9999
            node = None
            for x in self.frontier:
                if x.heuristic < min_cost and x.heuristic != 0:
                    min_cost = x.heuristic
                    node = x
                else:
                    continue
            self.frontier.remove(node)
            return node
