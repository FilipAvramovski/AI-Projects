from searching_framework.utils import Problem
from searching_framework.uninformed_search import breadth_first_graph_search


"""
На табла со димензии N x N, каде N > 3 е непарен природен број, поставени се топчиња. 
Некои од полињата се неупотребливи т.е. во нив никогаш не може да се поставуваат 
топчиња (на Слика 1 ваквите полиња се обоени со црна боја). Топчињата не се разликуваат 
помеѓу себе. Со избор (кликнување) на кое било топче може да се направи преместување на 
тоа топче од полето во кое се наоѓа -> преку едно поле (во една од шесте насоки: 
горе-десно, горе-лево, долу-десно, долу-лево, лево или десно), 
но само ако „прескокнатото“ поле содржи друго топче и полето до „прескокнатото“ поле 
(во соодветната насока) е слободно. Притоа, „прескокнатото“ топче исчезнува т.е се 
отстранува од таблата. На пример, со кликнување на топчето кое се наоѓа во петтата 
редица и третата колона на таблата прикажана на Слика 1, топчето кое се наоѓа во полето 
горе-лево од него ќе исчезне, а кликнатото топче ќе се позиционира во полето што се 
наоѓа во третата редица и првата колона (види ја Слика 2!).

Не е дозволено топчињата да излегуваат од таблата. Целта е на таблата да остане точно 
едно топче кое ќе биде позиционирано во централното поле во првата редица, како што е 
прикажано на Слика 3. Потребно е проблемот да се реши во најмал број на потези т.е. со 
избирање (кликнување) на најмал можен број на топчиња.

За сите тест примери обликот на таблата е ист како на примерот даден на Слика 1. За 
секој тест пример се менува големината N на таблата, како и бројот и распоредот на 
топчиња и неупотребливи полиња, соодветно. На влез прво се чита должина и ширина на 
просторот. Потоа се чита бројот на топчиња. Во наредните линии се читаат позициите на 
топчињата. На крај се читаат бројот на препреките и во наредна линија позиција на 
препрека.

Движењата на топчињата (потезите) потребно е да ги именувате на следниот начин: 

-GoreLevo: (x: x_val, y: y_val) - за преместување во насока горе-лево на топчето кое се 
наоѓа во x координатата x_val и y координатата y_val (ако таблата ја гледате во 
стандардниот координатен систем) 

-GoreDesno: (x: x_val, y: y_val) - за преместување во насока горе-десно на топчето кое се 
наоѓа во x координатата x_val и y координатата y_val (ако таблата ја гледате во 
стандардниот координатен систем) 

-DoluLevo: (x: x_val, y: y_val) - за преместување во насока долу-лево на топчето кое се 
наоѓа во x координатата x_val и y координатата y_val (ако таблата ја гледате во 
стандардниот координатен систем) 

-DoluDesno: (x: x_val, y: y_val) - за преместување во насока долу-десно на топчето кое 
се наоѓа во x координатата x_val и y координатата y_val (ако таблата ја гледате во 
стандардниот координатен систем) 

-Levo: (x: x_val, y: y_val) - за преместување налево на топчето кое се наоѓа во 
x координатата x_val и y координатата y_val (ако таблата ја гледате во стандардниот 
координатен систем) 

-Desno: (x: x_val, y: y_val) - за преместување надесно на топчето кое се наоѓа во 
x координатата x_val и y координатата y_val (ако таблата ја гледате во стандардниот 
координатен систем).
"""

class BallsPuzzle(Problem):
    def __init__(self, balls, blocked, n, goal=None):
        super().__init__(frozenset(balls), goal)
        self.blocked = set(blocked)
        self.n = n
        
        # goal is center of first row if not given
        if goal is None:
            self.goal = frozenset([(n//2, 0)])

        # Six possible moves with their offsets
        self.directions = {
            "GoreLevo": (-2, 2),
            "GoreDesno": (2, 2),
            "DoluLevo": (-2, -2),
            "DoluDesno": (2, -2),
            "Levo": (-2, 0),
            "Desno": (2, 0),
        }

    def successor(self, state):
        successors = {}
        balls = set(state)  # convert frozenset to mutable set

        for (x, y) in balls:
            for name, (dx, dy) in self.directions.items():
                nx, ny = x + dx, y + dy
                mid = (x + dx // 2, y + dy // 2)

                # Check all constraints
                if 0 <= nx < self.n and 0 <= ny < self.n:
                    if mid in balls and (nx, ny) not in balls and (nx, ny) not in self.blocked:
                        new_balls = set(balls)
                        new_balls.remove((x, y))   # move the ball
                        new_balls.remove(mid)      # remove jumped ball
                        new_balls.add((nx, ny))    # new position
                        action_name = f"{name}: (x={x},y={y})"
                        successors[action_name] = frozenset(new_balls)
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal


if __name__ == "__main__":
    # Read input
    n = int(input())
    num_balls = int(input())
    balls = []
    for _ in range(num_balls):
        balls.append(tuple(map(int, input().split(','))))

    num_blocked = int(input())
    blocked = []
    for _ in range(num_blocked):
        blocked.append(tuple(map(int, input().split(','))))

    problem = BallsPuzzle(balls, blocked, n)
    result = breadth_first_graph_search(problem)

    if result:
        print(result.solution())
    else:
        print("No solution found.")
