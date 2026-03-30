from searching_framework.utils import Problem
from searching_framework.informed_search import astar_search

"""
Даден е лавиринт NxN во кој се движи човече. Во лавиринтот има ѕидови кои се поставени 
на случајни позиции и истите НЕ може да се прескокнуваат. Потребно е човечето да 
стигне до куќичката без притоа да удри во некој ѕид или да излезе надвор од 
лавиринтот. Човечето во четири насоки: горе, долу, лево и десно. Со еден потег 
човечето може да се помести за онолку позиции колку му се потребни се додека не удри во 
ѕид или во границите на просторот.

За сите тест примери големината на таблата n се чита од стандарден влез. Потоа се 
чита бројот на ѕидови и позициите на секој ѕид. На крај се читаат позициите на 
човечето и куќичката. Ваша задача е да го имплементирате движењето на човечето во 
successor функцијата. Акциите се именуваат како „Desno X/Gore X/Dolu X/Levo X“. Потоа и
мплементирајте ја хевристичката функција h. Потребно е проблемот да се реши во 
најмал број на чекори со примена на информирано пребарување.

"""


class Lavirint(Problem):
    def __init__(self, initial,prostor,prepreki, goal=None):
        super().__init__(initial, goal)
        self.prostor = prostor
        self.prepreki = prepreki

    def successor(self,state):

        successors = {}

        covece = state

        # Desno
        x = covece[0]
        while True:
            if x + 1 >= self.prostor[0] or (x + 1, covece[1]) in self.prepreki:
                break
            x += 1
        if x != covece[0]:
            successors[f"Desno {x - covece[0]}"] = (x, covece[1])

        # Levo
        x = covece[0]
        while True:
            if x - 1 < 0 or (x - 1, covece[1]) in self.prepreki:
                break
            x -= 1
        if x != covece[0]:
            successors[f"Levo {covece[0] - x}"] = (x, covece[1])

        # Gore
        y = covece[1]
        while True:
            if y + 1 >= self.prostor[1] or (covece[0], y + 1) in self.prepreki:
                break
            y += 1
        if y != covece[1]:
            successors[f"Gore {y - covece[1]}"] = (covece[0], y)

        # Dole
        y = covece[1]
        while True:
            if y - 1 < 0 or (covece[0], y - 1) in self.prepreki:
                break
            y -= 1
        if y != covece[1]:
            successors[f"Dolu {covece[1] - y}"] = (covece[0], y)

        return successors
    

    def actions(self, state):
        return self.successor(state).keys()
    
    def result(self, state, action):
        return self.successor(state)[action]
    
    def h(self,node):
        covece=node.state
        kukja = self.goal

        return abs(covece[0]-kukja[0])+abs(covece[1]-kukja[1])
    
    def goal_test(self, state):
        return state==self.goal


if __name__ == '__main__':
    n = int(input())
    prostor = [n,n]
    m = int(input())
    prepreki = []
    for i in range(m):
        prepreka = tuple( map(int,input().split(",")))
        prepreki.append(prepreka)

    covece = tuple(map(int,input().split(",")))
    kukja = tuple(map(int,input().split(",")))

    lavirint = Lavirint(covece,prostor,prepreki,kukja)
    rezultat = astar_search(lavirint)

    if rezultat is not None:
        print(rezultat.solution())
    else:
        print("No Solution!")

