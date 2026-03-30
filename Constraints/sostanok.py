from constraint import*

"""
Потребно е да се закаже состанок во петок за Марија, Петар и Симона. Симона како менаџер мора 
да присуствува на состанокот со најмалку уште една личност. Состанокот трае еден час, и може 
да се закаже во периодот од 12:00 до 20:00. Почетокот на состанокот може да биде на секој час, 
односно состанокот може да почне во 12:00, но не во 12:05, 12:10 итн. За секој од членовите 
дадени се времињата во кои се слободни:

Симона слободни термини: 13:00-15:00, 16:00-17:00, 19:00-20:00
Марија слободни термини: 14:00-16:00, 18:00-19:00
Петар слободни термини: 12:00-14:00, 16:00-20:00

Потребно е менаџерот Симона да ги добие сите можни почетни времиња за состанокот. Даден е 
почетен код со кој е креирана класа за претставување на проблемот, на кој се додадени 
променливите. Потоа се повикува наоѓање на решение со BacktrackingSolver. Ваша задача е да ги 
додадете домените на променливите, како и да ги додадете ограничувањата (условите) на проблемот.

"""

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    
    # ---Dadeni se promenlivite, dodadete gi domenite-----
    
    problem.addVariable("Marija_prisustvo", [0,1])
    problem.addVariable("Simona_prisustvo", [1])
    problem.addVariable("Petar_prisustvo", [0,1])
    problem.addVariable("vreme_sostanok", range(12,20))

    # ----------------------------------------------------
    
    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(MinSumConstraint(1),["Marija_prisustvo","Petar_prisustvo"])

    simona_vreminja = {13,14,16,19}
    marija_vreminja = {0,14,15,18}
    petar_vreminja = {0,12,13,16,17,18,19}

    problem.addConstraint(InSetConstraint(simona_vreminja),["vreme_sostanok"])
    problem.addConstraint(SomeInSetConstraint(marija_vreminja),["Marija_prisustvo", "vreme_sostanok"])
    problem.addConstraint(SomeInSetConstraint(petar_vreminja),["Petar_prisustvo", "vreme_sostanok"])
     # ----------------------------------------------------
    
    [print(solution) for solution in problem.getSolutions()]
