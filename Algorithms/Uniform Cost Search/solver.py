from utils import Node, PriorityFrontier
from problem import Environment
from sys import argv, exit


def main():
    if len(argv) != 4:
        exit("USAGE: python solver.py {origin} {destination} {map}")

    ENV = Environment(argv[1], argv[2], argv[3])

    path = graph_search(ENV)

    if not path:
        exit("There is no possible way to this destination.")
    else:
        step_c = 1
        print()
        for step in path[0]:
            ENV.current = step
            if step_c != len(path[0]):
                print(f'STEP {step_c}: {step} -> {path[0][step_c]} a distance of {ENV.Nodes[step].get_distance(path[0][step_c])}',
                      '\n', ENV)
            else:
                continue
            step_c += 1

        print("Overall Distance:", path[1])
        print(*path[0], sep=" -> ")
        print(f"Depth is {path[2]}")


def graph_search(ENV):
    # Starting witha  frontier with initial state
    start = Node(ENV.current, None, None, None)
    frontier = PriorityFrontier()
    frontier.add(start)

    # Set of all explored sets
    closed = set()

    # Keep on looping until solution is found.
    while True:
        # If fontier is empty, return failure essentially
        if frontier.empty():
            return None

        # Getting a node and removing it from frontier
        node = frontier.remove()

        print("\nCURRENT:", node.state)
        ENV.current = node.state
        print(ENV)

        # Goal Test
        for actions in ENV.Nodes[node.state].get_connections():
            print("AVAILABLE:", actions)
            # print("FRONTIER:", [x.state for x in frontier.frontier])
            # print("AVAILABLE:", node.state, " -> ", actions, "at", node.distance)
            if ENV.destination == actions:
                solution = [ENV.destination]
                depth = node.depth + 1
                distance = node.distance + \
                    ENV.Nodes[node.state].get_distance(ENV.destination)
                while node.parent is not None:
                    solution.append(node.state)
                    node = node.parent
                solution.append(argv[1])

                solution.reverse()
                return [solution, distance, depth]

        if node.state not in closed:
            closed.add(node.state)
            for connection in ENV.Nodes[node.state].get_connections():
                # print("ADDING:", node.state, connection,
                #     ENV.Nodes[node.state].get_distance(connection))
                frontier.add(
                    Node(connection, node, ENV.Nodes[connection].get_connections(),
                         ENV.Nodes[node.state].get_distance(connection)))


if __name__ == '__main__':
    main()
