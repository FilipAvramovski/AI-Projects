from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


"""
Во табла со димензии 10x10 се наоѓаат змија, зелени јаболки и црвени јаболки. 
Потребно е змијата да ги изеде зелените јаболки, а да ги одбегнува црвените 
јаболки кои се отровни. Змијата на почетокот зафаќа три полиња од таблата, 
едно поле за главата и две полиња за телото. При секое јадење на зелена јаболка 
телото на змијата се издолжува на крајот за едно поле (пример Слика). 
Во даден момент можни се три акции на движење на змијата: продолжи право, сврти 
лево и сврти десно. При движењето на змијата треба да се внимава змијата да не се 
изеде сама себе (колизија на главата на змијата со некој дел од телото) и да не 
излезе надвор од таблата. Потребно е проблемот да се реши во најмал број на потези.

За сите тест примери изгледот и големината на таблата се исти како на примерот даден 
на сликата. За сите тест примери почетната позиција на змијата е иста. За секој тест 
пример се менува бројот и почетната позиција на зелените и црвените јаболки.

Во првата линија од влезот е даден бројот на зелени јаболки N, а во следните N редови 
се дадени координатите на зелените јаболки. Потоа е даден бројот на црвени јаболки M 
и нивните координати во наредните M редови. Табелата се претставува како координатен 
систем со координати x и y почнувајќи од нула, па соодветно, позициите се зададени 
како торка со прв елемент x и втор елемент y.

Движењата на змијата треба да ги именувате на следниот начин:

ProdolzhiPravo - змијата се придвижува за едно поле нанапред
SvrtiDesno - змијата се придвижува за едно поле на десно
SvrtiLevo - змијата се придвижува за едно поле на лево

Вашиот код треба да има само еден повик на функција за приказ на стандарден излез 
(print) со кој ќе ја вратите секвенцата на движења која змијата треба да ја направи 
за да може да ги изеде сите зелени јаболки. Да се најде решението со најмал број на 
преземени акции употребувајќи некој алгоритам за неинформирано пребарување. Врз 
основа на тест примерите треба самите да определите кое пребарување ќе го користите.

"""



class Zmija(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
        self.prostor = [10, 10]  

    def successor(self, state):
        successors = {}

        zmija = list(state[0])  
        glava_x, glava_y = zmija[0]  
        nasoka = state[1]
        zeleni_jabolka = set(state[2])
        crveni_jabolka = set(state[3])  

        svrti_levo = {
            'dole': 'desno',
            'desno': 'gore',
            'gore': 'levo',
            'levo': 'dole'
        }
        svrti_desno = {
            'dole': 'levo',
            'levo': 'gore',
            'gore': 'desno',
            'desno': 'dole'
        }

        dvizhenje = {
            'dole': (glava_x, glava_y - 1),
            'gore': (glava_x, glava_y + 1),
            'levo': (glava_x - 1, glava_y),
            'desno': (glava_x + 1, glava_y)
        }

        nov_x, nov_y = dvizhenje[nasoka]

        if (
            0 <= nov_x < self.prostor[0] and
            0 <= nov_y < self.prostor[1] and
            (nov_x, nov_y) not in zmija and
            (nov_x, nov_y) not in crveni_jabolka  
        ):
            nov_zmija = [(nov_x, nov_y)] + zmija[:-1]
            nov_zeleni_jabolka = set(zeleni_jabolka)

            if (nov_x, nov_y) in nov_zeleni_jabolka:
                nov_zmija.append(zmija[-1])  
                nov_zeleni_jabolka.remove((nov_x, nov_y))

            successors['ProdolziPravo'] = (tuple(nov_zmija), nasoka, tuple(nov_zeleni_jabolka), tuple(crveni_jabolka))

        successors['SvrtiLevo'] = (tuple(zmija), svrti_levo[nasoka], tuple(zeleni_jabolka), tuple(crveni_jabolka))
        successors['SvrtiDesno'] = (tuple(zmija), svrti_desno[nasoka], tuple(zeleni_jabolka), tuple(crveni_jabolka))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[2]) == 0  

if __name__ == '__main__':
    zmija = [(0,7), (0, 8), (0, 9)]
    nasoka = 'desno'

    zeleni_jabolka = []
    crveni_jabolka = []

    z = int(input())
    for _ in range(z):
        x, y = map(int, input().split(','))
        zeleni_jabolka.append((x, y))

    c = int(input())
    for _ in range(c):
        x, y = map(int, input().split(','))
        crveni_jabolka.append((x, y))

    initial_state = (tuple(zmija), nasoka, tuple(zeleni_jabolka), tuple(crveni_jabolka))
    problem = Zmija(initial_state)

    resenie = breadth_first_graph_search(problem)
    solution = resenie.solution()
    print(solution)

