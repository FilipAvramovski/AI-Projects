from searching_framework import Problem,breadth_first_graph_search
"""
Дадена е табла 8x6, каде што се поставени човече и топка. Потребно е човечето со 
туркање на топката да ја доведе до голот кој е обележан со сива боја. На таблата 
дополнително има противници кои се обележани со сина боја. Противниците се статични и 
не се движат.

Човечето може да се движи во пет насоки: горе, долу, десно, горе-десно и долу-десно 
за една позиција. При движењето, доколку пред него се наоѓа топката, може да ја турне 
топката во насоката во која се движи. Човечето не може да се наоѓа на истото поле 
како топката или некој од противниците. Топката исто така не може да се наоѓа на поле 
кое е соседно со некој од противниците (хоризнотално, вертикално или дијагонално) или 
на исто поле со некој од противниците.

За сите тест примери големината на таблата е иста, а позицијата на човечето и топката 
се менуваат и се читаат од стандарден влез. Позицијата на противниците и голот е иста 
за сите тест примери. Ваша задача е да го имплементирате поместувањето на човечето 
(со тоа и туркањето на топката) во successor функцијата. Акциите се именуваат како 
„Pomesti coveche gore/dolu/desno/gore-desno/dolu-desno“ ако се поместува човечето, 
или како „Turni topka gore/dolu/desno/gore-desno/dolu-desno“ ако при поместувањето 
на чoвечето се турнува и топката. Дополнително, потребно е да проверите дали сте 
стигнале до целта, односно да ја имплементирате функцијата goal_test и да проверите 
дали состојбата е валидна, односно да ја дополните функцијата check_valid. Треба да 
примените неинформирано пребарување за да најдете решение со најмал број на чекори. 
"""

class Gol(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
        self.prostor = [8, 6]  
        self.gol=[(7,2),(7,3)]
        self.protivnici=[(3,3), (4,5)]

    def turni_topka(self, topka, direction):
        nasoka = {
            "gore": (0, -1),
            "dolu": (0, 1),
            "desno": (1, 0),
            "levo": (-1, 0),
            "gore-desno": (1, -1),
            "dolu-desno": (1, 1),
            "gore-levo": (-1, -1),
            "dolu-levo": (-1, 1)
        }
        dx, dy = nasoka[direction]
        return (topka[0] + dx, topka[1] + dy)

    def successor(self, state):
        successors = {}

        covece=state[0]
        topka=state[1]

        potezi = {
            "Pomesti coveche gore": (covece[0], covece[1] - 1),
            "Pomesti coveche dolu": (covece[0], covece[1] + 1),
            "Pomesti coveche desno": (covece[0] + 1, covece[1]),
            "Pomesti coveche levo": (covece[0] - 1, covece[1]),
            "Pomesti coveche gore-desno": (covece[0] + 1, covece[1] - 1),
            "Pomesti coveche dolu-desno": (covece[0] + 1, covece[1] + 1),
            "Pomesti coveche gore-levo": (covece[0] - 1, covece[1] - 1),
            "Pomesti coveche dolu-levo": (covece[0] - 1, covece[1] + 1)
        }

        for poteg, new_covece in potezi.items():
            new_topka = topka
            
            if new_covece == topka:
                direction = poteg.split()[-1] 
                new_topka = self.turni_topka(topka, direction)
            
            if self.check_valid((new_covece, new_topka)):
                successors[poteg] = (new_covece, new_topka)
        
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]
    
    def check_valid(self,state):

        covece, topka = state

        if not (0 <= covece[0] < self.prostor[0] and 0 <= covece[1] < self.prostor[1]):
            return False
        if not (0 <= topka[0] < self.prostor[0] and 0 <= topka[1] < self.prostor[1]):
            return False

        if covece in self.protivnici:
            return False

        if covece == topka:
            return False

        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if (topka[0] + i, topka[1] + j) in self.protivnici:
                    return False

        return True

    def goal_test(self, state):
        return state[1] in self.gol
    

if __name__ == "__main__":
    covece = tuple(map(int, input().split(",")))
    topka = tuple(map(int, input().split(",")))

    initial_state = (covece, topka)
    problem = Gol(initial_state)
    rez = breadth_first_graph_search(problem)
    
    if rez is not None:
        print(rez.solution())
    else:
        print("No Solution!")

