from problem import Problem
from utility import hash_function

def cost_function(env):
    """This is the heuristic essentially."""
    cost = 0
    queen_loc = env.get_queen_locations()
    added = set()
    for queen in queen_loc:
        for queen_2 in queen_loc:
            if queen == queen_2:
                continue

            # Checknig for same row
            if queen[1] == queen_2[1]:
                hash_v = hash_function(queen, queen_2)
                hash_v_2 = hash_function(queen_2, queen)
                if hash_v not in added and hash_v_2 not in added:
                    added.add(hash_v)
                    added.add(hash_v_2)
                    cost += 1

    return cost


def main():
    env = Problem()
    print(env)
    print(cost_function(env))


if __name__ == '__main__':
    main()
