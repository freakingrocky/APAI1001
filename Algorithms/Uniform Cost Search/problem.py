from DS import Node
from os import get_terminal_size

class Environment:

    def __init__(self, origin: str, destination: str, file: str):
        self.current = origin
        self.destination = destination
        self.Nodes = {}
        with open(file, 'r') as file:
            for city in file.readlines():
                data = city.split("-")
                data_2 = data[1].split(';')
                connections = dict()
                for connection in data_2:
                    data_3 = connection.split("(")
                    connections[data_3[0]] = int(data_3[1].replace(")", ""))
                self.Nodes[data[0]] = Node(connections)

    def __str__(self):
        size = get_terminal_size()
        return (f"{self.current}".center(size[0], " ") + '\n' +
             "||".center(size[0], " ") + '\n' +
               f"{self.Nodes[self.current].get_connections()}".center(size[0], " "))

