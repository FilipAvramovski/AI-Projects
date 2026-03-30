from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from solaren_odblesok_dataset import dataset

"""
Дадено е податочно множество за класификација на соларни сигнали, кое се состои од 15 
карактеристики и две класи.

Потребно е да направите 3 модели на класификација:

-Наивен баесов класификатор.

-Класификатор со колекција од 50 дрва на одлука со ентропија како критериум за избор на 
најдобар атрибут за поделба.

-Невронска мрежа со 50 неврони, ReLU активациска функција, 0.001 рата на учење.

Од стандарден влез прво се чита критериум (mode) за поделба на подмножества за 
тренирање и тестирање, а потоа и процент (split) за поделба. Ако критериумот за 
поделба е "balanced" тогаш потребно е да го поделите податочното множество така што за 
тренирање ќе ги користите првите split% од секоја класа, а останатите за тестирање. Во 
спротивно, ако критериумот за поделба не е "balanced" тогаш потребно е да го поделите 
податочното множество така што за тренирање ќе ги користите првите split% од множеството, 
а останатите за тестирање.

Да се испечати точноста на моделот кој има највисока прецизност.

прецизност = TP / (TP + FP)

одзив = TP / (TP + FN)

TP - број на точно предвидени позитивни класи

FP - број на грешно предвидени позитивни класи

TN - број на точно предвидени негативни класи

FN - број на грешно предвидени негативни класи

"""

if __name__ == '__main__':

    mode = input()
    split = int(input())

    dataset0 = [row for row in dataset if row[-1]==0]
    dataset1 = [row for row in dataset if row[-1]==1]

    if mode == 'balanced':
        threshold_0 = int(split/100 * len(dataset0))
        threshold_1 = int(split/100 * len(dataset1))
        train_set = dataset0[:threshold_0] + dataset1[:threshold_1]
        test_set = dataset0[threshold_0:] + dataset1[threshold_1:]
    else:
        threshold = int(split/100 * len(dataset))
        train_set = dataset[:threshold]
        test_set = dataset[threshold:]
    
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifierNB = GaussianNB()
    classifierRFC = RandomForestClassifier(n_estimators=50,
                                           criterion='entropy',
                                           random_state=0)
    classifierMLP = MLPClassifier(50,
                                  activation='relu',
                                  learning_rate_init=0.001,
                                  random_state=0)
    classifierNB.fit(train_x,train_y)
    classifierRFC.fit(train_x,train_y)
    classifierMLP.fit(train_x,train_y)

    pred_NB = classifierNB.predict(test_x)
    pred_RFC = classifierRFC.predict(test_x)
    pred_MLP = classifierMLP.predict(test_x)

    precision_NB = 0.0
    precision_RFC = 0.0
    precision_MLP = 0.0

    for i,pred in enumerate([pred_NB,pred_RFC,pred_MLP]):
        tp,fp,tn,fn = 0,0,0,0
        for gt_class,pred_class in zip(test_y,pred):
            if gt_class==1:
                if pred_class==1:
                    tp+=1
                else:
                    fn+=1
            else:
                if pred_class==0:
                    tn+=1
                else:
                    fp+=1

        if i == 0:
            accuracy_NB = (tp + tn) / (tp + tn + fp + fn)
            if tp+fp!=0:
                precision_NB = tp / (tp + fp)

        elif i == 1:
            accuracy_RFC = (tp + tn) / (tp + tn + fp + fn)
            if tp+fp!=0:
                precision_RFC = tp / (tp + fp)

        elif i == 2:
            accuracy_MLP = (tp + tn) / (tp + tn + fp + fn)
            if tp+fp!=0:
                precision_MLP = tp / (tp + fp)
            
    if precision_NB>=precision_RFC and precision_NB>=precision_MLP:
        print("Najvisoka preciznost ima prviot klasifikator")
        print(f"Negovata tochnost e: {accuracy_NB}")
            
    elif precision_RFC>=precision_NB and precision_RFC>=precision_MLP:
        print("Najvisoka preciznost ima vtoriot klasifikator")
        print(f"Negovata tochnost e: {accuracy_RFC}")
        
    elif precision_MLP>=precision_RFC and precision_MLP>=precision_NB:
        print("Najvisoka preciznost ima tretiot klasifikator")
        print(f"Negovata tochnost e: {accuracy_MLP}")
        