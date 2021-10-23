from random import randint


class Environment:
    def __init__(self):
        self.environment = {1: randint(0, 1), 2: randint(0, 1),
                            3: randint(0, 1), 4: randint(0, 1),
                            5: randint(0, 1), 6: randint(0, 1)}

    def __repr__(self) -> str:
        """Environment Layout."""
        return (f"""
                ============================
                == [I] {self.environment[1]} == [2] {self.environment[2]} ==
                ============================
                == [3] {self.environment[3]} == [4] {self.environment[4]} ==
                ============================
                == [5] {self.environment[5]} == [6] {self.environment[6]} ==
                ============================
                """)

    def __str__(self) -> str:
        """Environment Layout with text."""
        return (self.__repr__().replace("0", "Clean").replace("1", "Dirty"))

