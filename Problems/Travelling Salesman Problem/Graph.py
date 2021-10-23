class Graph:
    def __init__(self, file):
        self.options = set()
        self.graph = dict()
        with open(file, 'r') as file:
            for line in file.readlines():
                data = line.split(":")
                self.options.add(data[0])
                connections = data[1].split(',')
                list_conn = {}
                for connection in connections:
                    list_conn[connection.split(" ")[1]] = (int(connection.split(
                        " ")[2].replace("(", "").replace(")", "").replace("\n", "")))
                self.graph[data[0]] = list_conn
