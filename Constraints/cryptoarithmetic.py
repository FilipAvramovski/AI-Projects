from constraint import *

"""
SEND+MORE=MONEY е криптоаритметичка загатка, што значи дека станува збор за наоѓање 
цифри кои ги заменуваат буквите за да се направи математичкиот израз вистинит. Секоја 
буква во проблемот претставува една цифра (0–9). Две букви не можат да ја претставуваат 
истата цифра. Кога буквата се повторува, тоа значи дека цифрата се повторува во 
решението. 


S	E	N	D
+	M	O	R	E
M	O	N	E	Y

Даден е почетен код со кој е креирана класа за претставување на проблемот, на кој се 
додадени променливите со нивниот домен. Потоа се повикува наоѓање на решение со 
BacktrackingSolver. Ваша задача е да го/ги додадете ограничувањето/њата (условите) на 
проблемот."""

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(10))))
    
    problem.addConstraint(AllDifferentConstraint(),variables)
    
    def sum(S,E,N,D,M,O,R,Y):
        send = 1000*S + 100*E + 10*N + D
        more = 1000*M + 100*O + 10*R + E
        money = 10000*M + 1000*O + 100*N + 10*E + Y
        return send+more == money

    problem.addConstraint(sum, variables)

    print(problem.getSolution())