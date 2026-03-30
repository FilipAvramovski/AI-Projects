from constraint import*

"""
Дадена ни е 8x8 табла за шах. Треба да се постават 8 топови на таблата така што ниеден топ 
да не се напаѓа. Топовите може да се постават на било која позиција која сметаме дека е 
најсоодветна. Единственото ограничување е дека не треба да се напаѓаат.
"""

#|Resenie 1 - variable tuples|

def notAttacking(rook1,rook2):
    row1,col1=rook1
    row2,col2=rook2
    return row1!=row2 and col1!=col2 # za kralici dodavame "and abs(row1-row2)!=abs(col1-col2)"

if __name__ == "__main__":
    problem=Problem(MinConflictsSolver())
    
    variables=["rook_"+str(i) for i in range(8)]
    domain=[(row,col) for row in range(8) for col in range(8)]

    problem.addVariables(variables,domain)

    for rook1 in variables:
        for rook2 in variables:
            if rook1!=rook2:
                problem.addConstraint(notAttacking,(rook1,rook2))

    res=problem.getSolution()
    print(res)

    for row in range(8):
        for col in range(8):
            print("T" if (row, col) in res.values() else "*", end="")
        print()


    
#  # |Resenie 2 - variable columns|

# if __name__ == "__main__":

#     problem = Problem(MinConflictsSolver())

#     variables = ["rook_" + str(i) for i in range(8)]
#     domain = range(8)

#     problem.addVariables(variables, domain)
#     problem.addConstraint(AllDifferentConstraint(), variables)

#     res = problem.getSolution()
#     print(res)

#     for row in range(8):
#         chosen_column = res["rook_" + str(row)]
#         for col in range(8):
#             print("T" if col == chosen_column else "*", end="")
#         print()



# # |Resenie 3 - ExactSumConstraint(64)|


# def notBothOne(a, b):
#     return not (a == 1 and b == 1)

# # eg:
# # 0 1 0 0 0 0 0 0
# # 1 0 0 0 0 0 0 0
# # 0 0 0 1 0 0 0 0
# # 0 0 1 0 0 0 0 0
# # 0 0 0 0 0 1 0 0
# # 0 0 0 0 1 0 0 0
# # 0 0 0 0 0 0 0 1
# # 0 0 0 0 0 0 1 0

# if __name__ == '__main__':
#     problem = Problem()

#     variables = [(x, y) for x in range(8) for y in range(8)]
#     domains = [1, 0]

#     problem.addVariables(variables, domains)

#     # for row in range(8):
#     #   for col1 in range(8):
#     #     for col2 in range(col1 + 1, 8):
#     #       problem.addConstraint(notBothOne, [(row, col1), (row, col2)])
#     # # or instead we can do this:
#     for row in range(8):
#         row_vars = [(row, col) for col in range(8)]
#         problem.addConstraint(ExactSumConstraint(1), row_vars)

#     # for col in range(8):
#     #   for row1 in range(8):
#     #     for row2 in range(row1 + 1, 8):
#     #       problem.addConstraint(notBothOne, [(row1, col), (row2, col)])
#     # # or instead we can do this:
#     for col in range(8):
#         col_vars = [(row, col) for row in range(8)]
#         problem.addConstraint(ExactSumConstraint(1), col_vars)

#     # problem.addConstraint(ExactSumConstraint(8), variables)

#     solution = problem.getSolution()
#     print(solution)

#     # for clearer output
#     for row in range(8):
#         for col in range(8):
#             print(solution[(row, col)], end="\t")
#         print()