from searching_framework import Problem
from searching_framework.uninformed_search import breadth_first_graph_search

"""
Во серија се наредени N кружни столбови со иста висина. На почетокот, на само еден од 
столбовите наредени се M камени блокови во форма на крофни со различна големина. 
Блоковите се наредени како кула т.н. најголемиот блок е поставен најдоле на столбот, а 
секој блок после него е помал од својот претходник подолу.

Крајната цел е кулата од почетниот столб да се премести на некој друг столб т.ш. ќе 
биде запазен оригиналниот редослед на блоковите.
Ваша задача е преку техниката на неинформирано пребарување низ простор на состојби да 
одредите кој е најмалиот број на чекори потребни да се пресметат блоковите од почетниот 
столб до крајниот т.ш. важи правилото дека во секој чекор само еден блок од врвот на 
некој столб може да се помести на некој друг столб ако е помал од блокот на врвот на 
другиот столб или другиот столб е празен. Во почетниот код дадено ви е читањето од 
стандарден влез на почетната и целната состојба на столбовите, т.ш. секој столб е 
претставен со посебна торка а броевите ги означуваат големините на блоковите. На 
стандарден излез испечатете го минималниот број на потребни чекори да се реши проблемот 
како и редоследот на потребните акции кои се во форматот 
MOVE TOP BLOCK FROM PILLAR i TO PILLAR j.
"""

class Tower(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        successors={}

        num_towers=len(state)

        for i in range(num_towers):
            if len(state[i])==0:
                continue
            top_block=state[i][-1]
            for j in range(num_towers):
                if i==j:
                    continue
                if len(state[j])==0 or state[j][-1]>=top_block:
                    new_state=list(list(tower) for tower in state)
                    new_state[j].append(new_state[i].pop())
                    successors[f"MOVE TOP BLOCK FROM PILLAR {i+1} TO PILLAR {j+1}"] = tuple(tuple(tower) for tower in new_state)

        return successors

    def actions(self, state):
        return self.successor(state).keys()
    
    def result(self, state, action):
        return self.successor(state)[action]
    
    def goal_test(self, state):
        return state==self.goal
    
def parse_state(line):
    pillars = line.strip().split(";")
    return tuple(
        tuple(int(x) for x in pillar.strip().split(",") if x)
        for pillar in pillars
    )

if __name__ == "__main__":

    initial_input = input().strip()
    goal_input = input().strip()

    initial_state = parse_state(initial_input)
    goal_state = parse_state(goal_input)

    problem = Tower(initial_state, goal_state)
    result = breadth_first_graph_search(problem)

    if result:
        print("Number of action", len(result.solution()))
        print(result.solution())
    else:
        print("No solution found.")    