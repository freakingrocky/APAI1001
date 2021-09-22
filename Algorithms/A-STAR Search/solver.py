from utils import Node, PriorityFrontier
from game import Game
from copy import deepcopy


def main():
    ENV = Game()

    print("SOLVING...")
    path = best_first_search(ENV)

    if not path:
        exit("There is no possible way to this destination.")
    else:
        print("\nSOLVED\n\n")
        step_c = 0
        for step in path:
            print(f"STEP {step_c}")
            ENV.board = step
            print(ENV)
            step_c += 1
        print(f"IT TOOK {step_c} STEPS")


def best_first_search(ENV):
    # Starting with a frontier with initial state
    start = Node(ENV.board, None, None, heuristic(ENV.board))
    frontier = PriorityFrontier()
    frontier.add(start)

    # Set of all explored sets
    closed = []
    step = 1

    # Keep on looping until solution is found.
    while True:
        print(
            f"STEP: {step} | FRONTIER LENGTH: {len(frontier.frontier)} | CLOSED: {len(closed)}", end='\r')

        step += 1
        # If fontier is empty, return failure essentially
        if frontier.empty():
            return None

        # Getting a node and removing it from frontier
        node = frontier.remove()

        # Goal Test
        if ENV.terminal_board == node.state:
            solution = [ENV.terminal_board]
            while node.parent is not None:
                solution.append(node.state)
                node = node.parent
            solution.append(ENV.board)

            solution.reverse()
            return solution

        if node.state not in closed and not frontier.contains_state(node.state):
            closed.append(node.state)
            for action in available_moves(node.state):
                child = transition_state(action, node.state)
                frontier.add(Node(child[:], node,
                                  available_moves(child), heuristic(child)))



def heuristic(board):
    """Return Mannhattan Distance Heuristic."""
    h = 0
    terminal_board = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                      4: (1, 0), 5: (1, 1), 6: (1, 2),
                      7: (2, 0), 8: (2, 1), "X": (2, 2)}
    for row in range(0, 3):
        for column in range(0, 3):
            num = board[row][column]
            if num == terminal_board[num]:
                continue
            else:
                r, c = terminal_board[num]
                h += abs(row - r) + abs(column - c)

    return h


def available_moves(board):
    """Return available moves based on a board."""
    r, c = pos(board)
    moves = set()
    if r != 2:
        moves.add('DOWN')
    if r != 0:
        moves.add('UP')
    if c != 0:
        moves.add('LEFT')
    if c != 2:
        moves.add('RIGHT')
    return moves


def pos(board):
    for row in range(0, 3):
        for column in range(0, 3):
            if board[row][column] == "X":
                return row, column


def transition_state(move, board):
    r, c = pos(board)
    tmp = deepcopy(board)
    if move == "UP":
        tmp_val = board[r - 1][c]
        tmp[r][c] = tmp_val
        tmp[r - 1][c] = "X"
    if move == "DOWN":
        tmp_val = board[r + 1][c]
        tmp[r][c] = tmp_val
        tmp[r + 1][c] = "X"
    if move == "RIGHT":
        tmp_val = board[r][c + 1]
        tmp[r][c] = tmp_val
        tmp[r][c + 1] = "X"
    if move == "LEFT":
        tmp_val = board[r][c - 1]
        tmp[r][c] = tmp_val
        tmp[r][c - 1] = "X"
    return tmp


if __name__ == '__main__':
    main()
