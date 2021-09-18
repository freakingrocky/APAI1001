
class Node:
    def __init__(self, origin: str, destinations: dict):
        self.origin = origin
        self.DS = destinations

    def get_connections(self):
        return self.DS.keys()

    def get_distance(self, city: str) -> int:
        return self.DS[city]
