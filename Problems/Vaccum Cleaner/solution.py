from random import randint
from os import get_terminal_size


class Agent:
    def __init__(self, environment):
        self.pos = randint(1, 6)
        self.env = environment
        self.cost = 0
        self._check()

    def _check(self):
        if self.env.environment[self.pos] == 1:
            self.env.environment[self.pos] = 0
            print(f"Cleaned at {self.pos}: \n {self.env}")
            self.cost += 0
            return True
        else:
            print(f"Current Position {self.pos} already clean: \n {self.env}")
            return False

    def terminal(self):
        if "1" not in repr(self.env):
            print("*" * get_terminal_size()[0])
            print("*" * get_terminal_size()[0], "COST =", self.cost, '\n', self.env)
            return True
        return False

    def Left(self):
        self._check()
        if self.pos in [1, 3, 5]:
            return False
        self.pos -= 1
        self.cost += 1
        print("GOING LEFT")

    def Right(self):
        self._check()
        if self.pos in [2, 4, 6]:
            return False
        self.pos += 1
        self.cost += 1
        print("GOING RIGHT")

    def Up(self):
        self._check()
        if self.pos in [1, 2]:
            return False
        self.pos -= 2
        self.cost += 1
        print("GOING UP")

    def Down(self):
        self._check()
        if self.pos in [5, 6]:
            return False
        self.pos += 2
        self.cost += 1
        print("GOING DOWN")
