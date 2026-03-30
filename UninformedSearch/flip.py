from searching_framework.utils import Problem
from searching_framework.uninformed_search import breadth_first_graph_search

"""
Tабла со димензии N x N се состои од бели и црни полиња. Со избор (кликнување) на едно 
поле се прави промена на бојата на тоа поле и на сите негови непосредни соседи 
(горе, долу, лево и десно) во спротивната боја, како што е прикажано на Слика. 
Целта е сите полиња на таблата да бидат обоени во црна боја. Потребно е проблемот да се 
реши во најмал број на потези т.е. со избирање (кликнување) на најмал можен број на 
полиња.

За сите тест примери обликот на таблата е ист како на примерот даден на Слика. За секој 
тест пример се менува големината N на таблата, како и распоредот на црни и бели полиња 
на неа, соодветно.

Во рамки на почетниот код даден за задачата се вчитуваат влезните аргументи за секој 
тест пример. Во променливата n ја имате големината на таблата 
(бројот на редици односно колони); во променливата fields ја имате бојата на сите полиња
 на таблата (по редослед: одлево - надесно, редица по редица, ако таблата ја гледате 
 како матрица), каде 1 означува дека полето е обоено во црна, а 0 означува дека полето е 
 обоено во бела боја.

Изборот на полиња (потезите) потребно е да ги именувате на следниот начин:

x: redica, y: kolona

каде redica и kolona се редицата и колоната на избраното (кликнатото) поле 
(ако таблата ја гледате како матрица).

Вашиот код треба да има само еден повик на функција за приказ на стандарден излез 
(print) со кој ќе ја вратите секвенцата на потези која треба да се направи за да може 
сите полиња на таблата да бидат обоени во црна боја. Треба да примените неинформирано 
пребарување. Врз основа на тест примерите треба самите да определите кое пребарување ќе 
го користите.
"""

class FlipPuzzle(Problem):
    def __init__(self, initial, prostor, goal=None):
        super().__init__(initial, goal)
        self.prostor = prostor

    def successor(self, state):

        successors = {}

        for i in range(self.prostor[0]):
            for j in range(self.prostor[1]):
                new_state = [list(row) for row in state]  # Create a mutable copy

                # Flip the selected cell
                new_state[i][j] = 1 - new_state[i][j]

                # Flip the neighbors
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < self.prostor[0] and 0 <= nj < self.prostor[1]:
                        new_state[ni][nj] = 1 - new_state[ni][nj]

                # Convert back to tuple of tuples for immutability
                new_state_tuple = tuple(tuple(row) for row in new_state)
                action = f"x: {i}, y: {j}"
                successors[action] = new_state_tuple

        return successors
    
    def actions(self, state):
        return self.successor(state).keys()
    
    def result(self, state, action):
        return self.successor(state)[action]
    
    def goal_test(self, state):
        return all(cell == 1 for row in state for cell in row)
    
if __name__ == "__main__":
    n = int(input())
    fields = list(map(int, input().split(",")))
    initial_state = tuple(tuple(fields[i*n:(i+1)*n]) for i in range(n))

    puzzle = FlipPuzzle(initial_state, (n, n))
    solution = breadth_first_graph_search(puzzle)

    if solution:
        print(solution.solution())
    else:
        print("No solution found.")