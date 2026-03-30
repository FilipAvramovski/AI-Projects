from searching_framework import Problem
from searching_framework.informed_search import astar_search

"""
Даден е лавиринт NxN во кој се движи Дух на ролери. Во лавиринтот има ѕидови кои се 
поставени на случајни позиции и истите може да се прескокнуваат. Потребно е Духот да 
стигне до Пакман без притоа да удри во некој ѕид или да излезе надвор од лавиринтот. 
Духот се движи со помош на ролери во две насоки: горе и десно. Со еден потег Духот 
може да се помести за една, две или три позиции горе или десно.

За сите тест примери големината на таблата n се чита од стандарден влез. Потоа се чита 
бројот на ѕидови и позициите на секој ѕид. Почетната позиција на Духот секогаш е (0, 0),
 додека позицијата на Пакман секогаш е (n-1, n-1). Ваша задача е да го имплементирате 
 движењето на Духот во successor функцијата, така што најпрво ќе се проба акцијата за 
 движење горе, а потоа десно. Акциите се именуваат како „Gore/desno X“. 
 Потоа имплементирајте ја хевристичката функција h. Состојбата на проблемот се чува во 
 торка каде што елементите се x и y позициите на Духот. На пример, почетната состојба за 
 дадената слика би била (0, 0). Потребно е проблемот да се реши во најмал број на 
 чекори со примена на информирано пребарување.
"""

class GhostOnSkates(Problem):
    def __init__(self, initial, n, prepreki, goal=None):
        super().__init__(initial, goal)
        self.prostor = [n,n]
        self.prepreki = prepreki
        self.pacman = (n-1,n-1)

    
    def successor(self, state):

        successors = {}

        ghost_x, ghost_y = state[0], state[1]

        if ghost_y<self.prostor[1] and (ghost_x,ghost_y+1) not in self.prepreki:
            successors["Gore 1"] = (ghost_x,ghost_y+1)

        if ghost_y+2<self.prostor[1] and (ghost_x,ghost_y+2) not in self.prepreki:
            successors["Gore 2"] = (ghost_x,ghost_y+2)

        if ghost_y+3<self.prostor[0] and (ghost_x,ghost_y+3) not in self.prepreki:
            successors["Gore 3"] = (ghost_x,ghost_y+3)

        if ghost_x+1<self.prostor[0] and (ghost_x+1,ghost_y) not in self.prepreki:
            successors["Desno 1"] = (ghost_x+1,ghost_y)
        
        if ghost_x+2<self.prostor[0] and (ghost_x+2,ghost_y) not in self.prepreki:
            successors["Desno 2"] = (ghost_x+2,ghost_y)

        if ghost_x+3<self.prostor[0] and (ghost_x+3,ghost_y) not in self.prepreki:
            successors["Desno 3"] = (ghost_x+3,ghost_y)

        return successors
    
    def actions(self, state):
        return self.successor(state).keys()
    
    def result(self, state, action):
        return self.successor(state)[action]
    
    def h(self,node):
        ghost_x,ghost_y = node.state
        pacman_x, pacman_y = self.goal

        return abs(ghost_x - pacman_x) + abs(ghost_y - pacman_y)
        
    def goal_test(self,state):
        return state == self.goal
    
if __name__ == '__main__':

    ghost = (0,0)
    n = int(input())
    pacman = (n-1,n-1)

    m = int(input())
    prepreki = []

    for i in range(m):
        prepreki.append(tuple(map(int,input().split(','))))
    
    problem = GhostOnSkates(ghost,n,prepreki,pacman)
    res = astar_search(problem)

    print(res.solution())