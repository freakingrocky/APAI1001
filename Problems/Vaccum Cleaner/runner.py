from solution import Agent
from problem import Environment
from random import choice

agent = Agent(Environment())
actions = [agent.Up, agent.Down, agent.Right, agent.Left]
explored = set()

def get_actions(pos):
    actions = []
    if agent.pos not in [1, 3, 5]:
        actions.append(agent.Left)
    if agent.pos not in [1, 2]:
        actions.append(agent.Up)
    if agent.pos not in [2, 4, 6]:
        actions.append(agent.Right)
    if agent.pos not in [5, 6]:
        actions.append(agent.Down)
    return actions

while not agent.terminal():
    explored.add(agent.pos)
    if agent.pos not in [1, 3, 5] and (agent.pos + 1) not in explored:
        agent.Left()
    elif agent.pos not in [1, 2] and (agent.pos + 1) not in explored:
        agent.Up()
    elif agent.pos not in [2, 4, 6] and (agent.pos + 1) not in explored:
        agent.Right()
    elif agent.pos not in [5, 6] and (agent.pos + 1) not in explored:
        agent.Down()
    else:
        choice(get_actions(agent.pos))()
