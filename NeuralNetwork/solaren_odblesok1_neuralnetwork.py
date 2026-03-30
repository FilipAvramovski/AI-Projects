from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import OrdinalEncoder
from solaren_odblesok_dataset import dataset

"""
Дадено ни е податочно множество за соларен одблесок. Сите атрибути кои ги содржи се од 
нумерички тип. Ваша задача е да истренирате класификатор - невронска мрежа кој ќе 
предвидува класи на соларен одблесок. Од стандарден влез се чита бројот на примероци X 
за кои треба да се направи предвидувањето. Последните X примероци се земаат за тестирање, 
додека сите останати примероци се за тренирање (на пр. ако X=6, последните 6 примероци 
се тест примероци, а останатите примероци се дел од тренирачкото множество). 

Во почетниот код имате дадено податочно множество, како и објект од моделот MLPClassifier. 
Ваша задача е да го поделите првичното податочно множество на множество за тренирање и 
множество за тестирање. Потоа, истренирајте го моделот. Пресметајте прецизност и одзив 
на моделот со тестирачкото множество и вредностите испечатете ги на стандарден излез. 
Напомена: Освен тоа што се бара не е потребно да имплементирате ништо друго!

прецизност = TP / (TP + FP)

одзив = TP / (TP + FN)



TP - број на точно предвидени позитивни класи

FP - број на грешно предвидени позитивни класи

TN - број на точно предвидени негативни класи

FN - број на грешно предвидени негативни класи



ЗАБЕЛЕШКА: Ако TP + FP е 0, тогаш вредноста за прецизноста е 0. Ако TP + FN е 0, тогаш 
вредноста за одзив е 0.

За да ги добиете истите резултати како и во тест примерите, при креирање на 
класификаторот поставете random_state=0
"""

if __name__ == '__main__':
    
    x = int(input())
    
    train_set = dataset[:-x]
    train_x = [[float(val) for val in row[:-1]] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_set = dataset[-x:]
    test_x = [[float(val) for val in row[:-1]] for row in test_set]
    test_y = [row[-1] for row in test_set]


    classifier = MLPClassifier(3,
                               activation='relu',
                               learning_rate_init=0.003,
                               max_iter=200,
                               random_state=0)
    
    classifier.fit(train_x,train_y)
    pred = classifier.predict(test_x)

    tp,tn,fp,fn = 0,0,0,0
    for gt_class,pred_class in zip(test_y,pred):
        if gt_class == 1:
            if pred_class == 1:
                tp += 1
            else:
                fn += 1
        elif gt_class == 0:
            if pred_class == 1:
                fp += 1
            else:
                tn += 1

    if tp+fp == 0:
        precision = 0.0
    else:
        precision = tp / (tp + fp)

    if tp+fn==0:
        recall=0.0
    else:
        recall = tp / (tp + fn)

    print(f"Precision: {precision}")
    print(f"Recall: {recall}")