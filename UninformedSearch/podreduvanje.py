from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


class Squares(Problem):
    def __init__(self, initial, house):
        super().__init__(initial, house)

    def goal_test(self, state):
        return state == self.goal

    @staticmethod
    def check_valid(state):
        for x, y in state:
            if x < 0 or x > 4 or y < 0 or y > 4:
                return False
        return True

    def successor(self, state):
        succ = {}

        for i in range(5):
            x, y = state[i]  

            if y < 4: 
                new_state = list(state)
                new_state[i] = (x, y + 1) 
                if self.check_valid(new_state): 
                    succ[f"Pomesti kvadratche {i+1} gore"] = tuple(new_state)

            if y > 0:
                new_state = list(state)
                new_state[i] = (x, y - 1)
                if self.check_valid(new_state): 
                    succ[f"Pomesti kvadratche {i+1} dolu"] = tuple(new_state)

            if x > 0:
                new_state = list(state)
                new_state[i] = (x - 1, y)
                if self.check_valid(new_state):
                    succ[f"Pomesti kvadratche {i+1} levo"] = tuple(new_state)

            if x < 4:
                new_state = list(state)
                new_state[i] = (x + 1, y)
                if self.check_valid(new_state):
                    succ[f"Pomesti kvadratche {i+1} desno"] = tuple(new_state)

        return succ

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    # ((x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5))
    initial_state = tuple()
    for _ in range(5):
        initial_state += (tuple(map(int, input().split(','))), )

    goal_state = ((0, 4), (1, 3), (2, 2), (3, 1), (4, 0))

    squares = Squares(initial_state, goal_state)
    res=breadth_first_graph_search(squares)

    print(res.solution())