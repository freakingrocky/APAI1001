from random import choice

class Node:
    """Node Data Structure for Basic Search."""

    def __init__(self, state, parent, action, distance):
        self.state = state
        self.parent = parent
        self.action = action
        self.distance = parent.distance + distance if parent and distance else 0
        self.depth = parent.depth + 1 if parent else 0


class PriorityFrontier():
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
            min_cost = 99999
            node = self.frontier[0] if len(self.frontier) == 1 else None
            for x in self.frontier:
                if x.distance < min_cost and x.distance != 0:
                    min_cost = x.distance
                    node = x
                else:
                    continue
            # print("RETURNING:", node.state, node.distance)
            self.frontier.remove(node)
            return node
