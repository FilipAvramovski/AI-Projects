from searching_framework.utils import Problem
from searching_framework.informed_search import *

"""
Потребно е човечето безбедно да дојде до куќичката. 
Човечето може да се придвижува на кое било соседно поле хоризонтално 
или вертикално. Пречките 1 и 2 се подвижни, при што и двете пречки се 
движат вертикално. Секоја од пречките се придвижува за едно поле во 
соодветниот правец и насока со секое придвижување на човечето.

Притоа, пречката 1 на почетокот се движи надолу, додека пречката 2 
на почетокот се движи нагоре.

Кога некоја пречка ќе дојде до крајот на таблата при што повеќе не 
може да се движи во насоката во која се движела, го менува движењето 
во спротивната насока. Доколку човечето и која било од пречките се 
најдат на исто поле човечето ќе биде уништено.

За сите тест примери изгледот и големината на таблата се исти како 
на примерот даден на сликите. За сите тест примери почетните положби, 
правец и насока на движење за препреките се исти. За секој тест пример почетната позиција на човечето се менува, а исто така се менува и позицијата на куќичката.

Во рамки на почетниот код даден за задачата се вчитуваат влезните 
аргументи за секој тест пример.

Движењата на човечето потребно е да ги именувате на следниот начин:

Right - за придвижување на човечето за едно поле надесно
Left - за придвижување на човечето за едно поле налево
Up - за придвижување на човечето за едно поле нагоре
Down - за придвижување на човечето за едно поле надолу

Вашиот код треба да има само еден повик на функција за приказ на 
стандарден излез (print) со кој ќе ја вратите секвенцата на движења 
која човечето треба да ја направи за да може од својата почетна 
позиција да стигне до позицијата на куќичката.

Треба да примените информирано пребарување. За имплементација на 
хевристичката функција треба да користите Менхетен растојание.


. . 1 . . . . .
. . . . . . . K
. . . . . . . .
C . . . . . . .
. . . . . . . .
. . . . . 2 . .

Posle 1 poteg:

. . . . . . . .
. . 1 . . . . K
. . . . . . . .
. C . . . . . .
. . . . . 2 . .
. . . . . . . .
"""


class Explorer(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
        self.grid_size = [8,6]

    def successor(self, state):
        
        successors = {}

        man_x,man_y = state[0],state[1]
        obstacle1 = [state[2], state[3], state[4]]
        obstacle2 = [state[5], state[6], state[7]]
        max_x = self.grid_size[0]
        max_y = self.grid_size[1]

        if obstacle1[2] == 0:  # up
            if obstacle1[1] == max_y - 1:
                obstacle1[2] = 1
                obstacle1[1] -= 1
            else:
                obstacle1[1] += 1
        else:  # down
            if obstacle1[1] == 0:
                obstacle1[2] = 0
                obstacle1[1] += 1
            else:
                obstacle1[1] -= 1

        if obstacle2[2] == 0:  # up
            if obstacle2[1] == max_y - 1:
                obstacle2[2] = 1
                obstacle2[1] -= 1
            else:
                obstacle2[1] += 1
        else:  # down
            if obstacle2[1] == 0:
                obstacle2[2] = 0
                obstacle2[1] += 1
            else:
                obstacle2[1] -= 1

        obstacles = [[obstacle1[0], obstacle1[1]], [obstacle2[0], obstacle2[1]]]

        if man_x < max_x - 1 and [man_x + 1, man_y] not in obstacles:  # right
            successors['Right'] = (man_x + 1, man_y,
                                   obstacle1[0], obstacle1[1], obstacle1[2],
                                   obstacle2[0], obstacle2[1], obstacle2[2])

        if man_x > 0 and [man_x - 1, man_y] not in obstacles:  # left
            successors['Left'] = (man_x - 1, man_y,
                                   obstacle1[0], obstacle1[1], obstacle1[2],
                                   obstacle2[0], obstacle2[1], obstacle2[2])

        if man_y < max_y - 1 and [man_x, man_y + 1] not in obstacles:  # up
            successors['Up'] = (man_x, man_y + 1,
                                   obstacle1[0], obstacle1[1], obstacle1[2],
                                   obstacle2[0], obstacle2[1], obstacle2[2])

        if man_y > 0 and [man_x, man_y - 1] not in obstacles:  # down
            successors['Down'] = (man_x, man_y - 1,
                                   obstacle1[0], obstacle1[1], obstacle1[2],
                                   obstacle2[0], obstacle2[1], obstacle2[2])

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        position = (state[0], state[1])
        return position == self.goal
    
    def h(self,node):
        man_x,man_y = node.state[0],node.state[1]
        house_x,house_y = self.goal[0],self.goal[1]

        return abs(man_x-house_x)+abs(man_y-house_y)
    

if __name__ == '__main__':
    init = (0,2)
    goal = (7,4)
    obstacle1 = (2,5,-1) #down
    obstacle2 = (5,0,1) # up

    explorer = Explorer((init[0], init[1], 
                         obstacle1[0],obstacle1[1],obstacle1[2],
                         obstacle2[0],obstacle2[1],obstacle2[2]), goal)

    result = astar_search(explorer)
    print(result.solution())