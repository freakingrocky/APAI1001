
class Node:
    def __init__(self, destinations: dict):
        self.DS = destinations

    def __str__(self):
        return str(self.DS)

    def get_connections(self):
        return list(self.DS.keys())

    def get_distance(self, city: str) -> int:
        return self.DS[city]
