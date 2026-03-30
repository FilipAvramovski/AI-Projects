from constraint import *

"""
Дадена ни е мапата на Австралија и треба да ја обоиме со три бои: сина, зелена и црвена. 
Соседните региони не смее да имаат иста боја. Секој регион може да има една од трите бои.


"""

def notEqualColors(color1,color2):
    return color1!=color2

if __name__=="__main__":
    problem=Problem()

    variables=["WA","NT","SA","Q","NSW","V","T"]
    domain=["Red","Green","Blue"]
    problem.addVariables(variables,domain)

    pairs = [("WA", "NT"), ("WA", "SA"), ("SA", "NT"), ("SA", "NSW"), ("SA", "Q"), ("SA", "V"), ("NT", "Q"), ("Q", "NSW"), ("NSW", "V")]
    
    for pair in pairs:
        problem.addConstraint(notEqualColors,pair)

    print(problem.getSolution())

    print()

    print(problem.getSolutions())

    print()

    res_iter = problem.getSolutionIter()
    for i in range(5):
        print(next(res_iter))

