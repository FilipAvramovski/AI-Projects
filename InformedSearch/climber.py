from searching_framework.utils import Problem
from searching_framework.informed_search import *

"""
Дадена е табла 5x9, каде што е поставено човече. Потребно е човечето со качување по 
ѕидот да стигне до врвот кој е означен со куќичка. 

Човечето може да се движи во три насоки: горе, горе-десно и горе-лево за една или 
две позиции (дијагонално, не е како фигурата коњ во шах). Човечето може и да остане 
на моменталното поле. Притоа човечето може да се наоѓа само на полињата на кои е 
поставен зелен осумаголник. Полињата кои не се означени со зелен осумаголник може да 
се прескокнуваат. Човечето исто така не смее да излезе од таблата. Куќичката е 
подвижна и се движи лево и десно за една позиција со секое поместување (или избор да 
не се помести) на човечето. Таа може да застане на било кое поле во редот во кој се 
наоѓа. Куќичката на почеток се движи во една насока, а кога ќе стигне до крајот на 
таблата ја менува насоката. Единственото поле во најгорниот ред на кое може да 
застане човечето е она на кое се наоѓа куќичката.

За сите тест примери големината на таблата е иста, а позицијата на човечето и 
куќичката се менуваат и се читаат од стандарден влез. Притоа куќичката секогаш се 
наоѓа во најгорниот ред. Почетната насока на куќичката исто така се чита од 
стандарден влез. Позицијата на дозволените полиња е иста за сите тест примери. 
Ваша задача е да го имплементирате поместувањето на човечето и куќичката во 
successor функцијата.

Акциите се именуваат како:
„Stoj/Gore 1/Gore 2/Gore-desno 1/Gore-desno 2/Gore-levo 1/Gore-levo 2“. 

Дополнително, потребно е да проверите дали сте стигнале до целта, односно да ја 
имплементирате функцијата goal_test и да проверите дали состојбата е валидна. 
Треба да примените информирано пребарување за да најдете решение со најмал број на 
чекори. 

"""

class Climber(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
        self.prostor = [5,9]
        self.dozvoleno = [(1,0), (2,0), (3,0), 
                          (1,1), (2,1), (0,2), 
                          (2,2), (4,2), (1,3), 
                          (3,3), (4,3), (0,4), 
                          (2,4), (2,5), (3,5), 
                          (0,6), (2,6), (1,7), (3,7)]
        
    def successor(self, state):
        
        successors = {}

        planinar_x, planinar_y = state[0],state[1]
        kukja_x,kukja_y,kukja_nasoka = state[2]

        #Dvizenje na kukja
        if kukja_nasoka=='desno':
            if kukja_x==self.prostor[0]-1:
                kukja_nasoka='levo'
                kukja_x-=1
            else:
                kukja_x+=1
        elif kukja_nasoka=='levo':
            if kukja_x==0:
                kukja_nasoka='desno'
                kukja_x+=1
            else:
                kukja_x-=1

        kukja_pos=(kukja_x,kukja_y,kukja_nasoka)
        

        successors["Stoj"] = (planinar_x,planinar_y,kukja_pos)
        
        if (planinar_y+2 < self.prostor[1] and (planinar_x,planinar_y+2)  in self.dozvoleno) or (planinar_x,planinar_y+2)==(kukja_x,kukja_y):
            successors["Gore 2"] = (planinar_x,planinar_y+2,kukja_pos)
        
        if (planinar_y+1 < self.prostor[1] and (planinar_x,planinar_y+1) in self.dozvoleno) or (planinar_x,planinar_y+1)==(kukja_x,kukja_y):
            successors["Gore 1"] = (planinar_x,planinar_y+1,kukja_pos)

        if (planinar_x+2<self.prostor[0] and planinar_y+2<self.prostor[1] and (planinar_x+2,planinar_y+2) in self.dozvoleno) or (planinar_x+2,planinar_y+2)==(kukja_x,kukja_y):
            successors["Gore-desno 2"] = (planinar_x+2,planinar_y+2,kukja_pos)

        if (planinar_x+1<self.prostor[0] and planinar_y+1<self.prostor[1] and (planinar_x+1,planinar_y+1) in self.dozvoleno) or (planinar_x+1,planinar_y+1)==(kukja_x,kukja_y):
            successors["Gore-desno 1"] = (planinar_x+1,planinar_y+1,kukja_pos)
        
        if (0<=planinar_x-2 and planinar_y+2<self.prostor[1] and (planinar_x-2,planinar_y+2) in self.dozvoleno) or (planinar_x-2,planinar_y+2)==(kukja_x,kukja_y):
            successors["Gore-levo 2"] = (planinar_x-2,planinar_y+2,kukja_pos)

        if (0<=planinar_x-1 and planinar_y+1<self.prostor[1] and (planinar_x-1,planinar_y+1) in self.dozvoleno) or (planinar_x-1,planinar_y+1)==(kukja_x,kukja_y):
            successors["Gore-levo 1"] = (planinar_x-1,planinar_y+1,kukja_pos)

        return successors
    
    def actions(self, state):
        return self.successor(state).keys()
    
    def result(self, state, action):
        return self.successor(state)[action]
    
    def h(self,node):
        planinar_x, planinar_y = node.state[0], node.state[1]
        kukja_x, kukja_y = node.state[2][0], node.state[2][1]
        
        return max(abs(planinar_x - kukja_x), abs(planinar_y - kukja_y)+1//2)
    
    def goal_test(self, state):
        return state[0]==state[2][0] and state[1]==state[2][1]
    

if __name__ == '__main__':
    planinar_x,planinar_y=map(int,input().split(","))
    kukja_x,kukja_y=map(int,input().split(","))
    dvizi_kukja=input()

    planinar=Climber((planinar_x,planinar_y,(kukja_x,kukja_y,dvizi_kukja)))

    rezultat=astar_search(planinar)
    if rezultat != None:
        print(rezultat.solution())
    else:
        print("Nema reshenie.")
