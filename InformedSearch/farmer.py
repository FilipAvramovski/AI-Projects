
from searching_framework.utils import Problem
from searching_framework.informed_search import *

"""
Потребно е да се пренесат зелката, јарето, волкот и фармерот од 
источната страна на западната страна на реката. Само фармерот го 
вози чамецот. Во чамецот има простор за двајца патници: фармерот и 
уште еден патник.

Ограничувања: Доколку останат сами (без присуство на фармерот):

Јарето ја јаде зелката
Волкот го јаде јарето

Вашиот код треба да има само еден повик на функција за приказ на 
стандарден излез (print) со кој ќе ја вратите секвенцата од позиции 
на актерите која одговара на секвенцата на движења со која сите 
актери ќе бидат пренесени на западната страна на реката.

Треба да примените информирано пребарување. Дефинирајте соодветна 
хевристика која ќе биде прифатлива за проблемот.
"""
def valid(state):
    farmer,cabbage,goat,wolf = state

    if cabbage==goat and farmer!=goat:
        return False
    
    if goat==wolf and farmer!=wolf:
        return False
    
    return True


class Farmer(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = {}

        farmer,cabbage,goat,wolf = state

        #Farmer nosi farmer
        new_farmer='e' if farmer=='w' else 'w'
        new_state = (new_farmer,cabbage,goat,wolf)
        if valid(new_state):
            successors["Farmer nosi farmer"] = new_state

        #Farmer nosi zelka
        if cabbage==farmer:
            new_cabbage ='e' if cabbage=='w' else 'w'
            new_state = (new_farmer,new_cabbage,goat,wolf)
            if valid(new_state):
                successors["Farmer nosi zelka"] = new_state

        #Farmer nosi jare
        if goat==farmer:
            new_goat ='e' if goat=='w' else 'w'
            new_state = (new_farmer,cabbage,new_goat,wolf)
            if valid(new_state):
                successors["Farmer nosi jare"] = new_state

        #Farmer nosi volk
        if wolf==farmer:
            new_wolf ='e' if wolf=='w' else 'w'
            new_state = (new_farmer,cabbage,goat,new_wolf)
            if valid(new_state):
                successors["Farmer nosi volk"] = new_state


        return successors
    
    def actions(self, state):
        return self.successor(state).keys()
    
    def result(self, state, action):
        return self.successor(state)[action]

    def h(self,node):

        value = 0

        for x,y in zip(node.state,self.goal):
            if x!=y:
                value+=1

        return value
    
if __name__ == "__main__":
    initial_state = ('e', 'e', 'e', 'e')
    goal_state = ('w', 'w', 'w', 'w')

    farmer = Farmer(initial_state, goal_state)

    result = astar_search(farmer)
    print(result.solution())