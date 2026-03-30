from constraint import *

#|Resenie 1 - variable tuples|

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = [ (x,y) for x in range(4) for y in range(4) ]
    domain = range(1, 17)
    problem.addVariables(variables, domain)

    for row in range(4):
        row_vars = [(row, col) for col in range(4)]
        problem.addConstraint(ExactSumConstraint(34), row_vars)

    for col in range(4):
        col_vars = [(row, col) for row in range(4)]
        problem.addConstraint(ExactSumConstraint(34), col_vars)

    main_diag_vars = [(ind, ind) for ind in range(4)]
    minor_diag_vars = [(ind, 3 - ind) for ind in range(4)]
    problem.addConstraint(ExactSumConstraint(34), main_diag_vars)
    problem.addConstraint(ExactSumConstraint(34), minor_diag_vars)

    problem.addConstraint(AllDifferentConstraint(), variables)

    solution = problem.getSolution()
    # for clearer output
    print(solution)
    for row in range(4):
        for col in range(4):
            print(solution[(row, col)], end="\t")
        print()

"""
|Resenie 2 - indexed|

if __name__ == '__main__':
    # problem = Problem(MinConflictsSolver()) # this sometimes provides no solution due to an error in the MinConflictsSolver class
    problem = Problem(BacktrackingSolver())

    variables = range(16)
    domain = range(1, 17)
    problem.addVariables(variables, domain)

    suma = 34  # after analyzing the problem, we can see that the sum of each row, column and diagonal is 34

    for first in [0, 4, 8, 12]:  # in range(0, n*n, n)
        row_vars = [first + move for move in range(4)]
        problem.addConstraint(ExactSumConstraint(suma), row_vars)
    for first in [0, 1, 2, 3]:  # in range(0, n, 1)
        col_vars = [first + move for move in range(0, 16, 4)]  # in range(0, n*n, n)
        problem.addConstraint(ExactSumConstraint(suma), col_vars)

    main_diag_vars = [move for move in range(0, 16, 5)]  # in range(0, n*n, n+1)
    minor_diag_vars = [3 + move for move in range(0, 12, 3)]  # in range(n-1, n*n-1, n-1)
    problem.addConstraint(ExactSumConstraint(suma), main_diag_vars)
    problem.addConstraint(ExactSumConstraint(suma), minor_diag_vars)

    problem.addConstraint(AllDifferentConstraint(), variables)

    print(problem.getSolution())

"""



"""
|Resenie 3 - with extra sum variables|


def sumOf4EqualsVar(sum_var, a, b, c, d):
    return sum_var == sum([a, b, c, d])


if __name__ == '__main__':
    # problem = Problem(MinConflictsSolver()) # MinConflictsSolver() is not working, returns None although a solution exists
    problem = Problem(BacktrackingSolver())

    variables = [(i, j) for i in range(4) for j in range(4)]
    domains = range(1, 17)
    problem.addVariables(variables, domains)

    sum_vars = [f"sum_row_{ind}" for ind in range(4)] + \
               [f"sum_col_{ind}" for ind in range(4)] + \
               ["sum_diag_1", "sum_diag_2"]
    sums_domain = range(1, 65)
    # sums_domain = range(34, 35) # if we further analyze the problem, we can see that the sum of each row, column and diagonal is 34, then we won't need the sum_vars at all, which will speed up the computations
    problem.addVariables(sum_vars, sums_domain)

    # The print below will help you understand the tuples
    sums_4_tuples = \
        [[(row, col) for col in range(4)] for row in range(4)] + \
        [[(row, col) for row in range(4)] for col in range(4)] + \
        [[(ind, ind) for ind in range(4)]] + \
        [[(ind, 3 - ind) for ind in range(4)]]

    for sum_var, vars_4_tuple in zip(sum_vars, sums_4_tuples):
        print(sum_var, vars_4_tuple)
        problem.addConstraint(sumOf4EqualsVar, [sum_var] + vars_4_tuple)

    problem.addConstraint(AllDifferentConstraint(), variables)
    problem.addConstraint(AllEqualConstraint(), sum_vars)

    solution = problem.getSolution()
    print(solution)

    for row in range(4):
        for col in range(4):
            print(solution[(row, col)], end=" ")
        print()
        
"""