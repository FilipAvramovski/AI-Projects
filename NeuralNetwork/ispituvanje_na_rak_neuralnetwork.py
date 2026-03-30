from ispituvanje_na_rak_dataset import dataset
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler

"""
Дадено е податочноto множество Wisconsin Diagnostic Breast Cancer (WDBC). 
Карактеристиките се пресметани од дигитализирана слика на рак, со што се опишуваат 
карактеристиките на јадрото на клетката присутна на сликата. Потребно е да се направи 
модел на невронска мрежа кој ќе детектира малигнен рак (B = benign, M = malignant). 
Класата е дадена како прв елемент, по што следуваат карактеристиките. Направете 
мапирање на класите така што класата B ќе ја претставите како 0, а класата M како 1.

Поделете го податочното множество на тренирачко и тестирачко множество со односот 
70%:30% од секоја од класите (првите 70% од класата 'M' и првите 70% од класата 'B' се 
дел од тренирачкото множество, а останатите податочни примероци се дел од тестирачкото 
множество). При изградба на тренирачкото множество почнете од класата 'M'. 
Карактеристиките потребно е да се нормализираат со MinMaxScaler во ранг од -1 до 1. 
Изградете невронска мрежа чиј што број на неврони во скриениот слој се чита од 
стандарден влез. Моделот се тренира со рата на учење од 0.001, 20 епохи и ReLU 
активациска функција на невроните од скриениот слој.

Потребно е да се пресметаат прецизноста и одзивот кои се добиваат со тренирачкото 
множество и со тестирачкото множество.

прецизност = TP / (TP + FP)
одзив = TP / (TP + FN)

TP - број на точно предвидени малигни клетки
FP - број на грешно предвидени малигни клетки
TN - број на точно предвидени бенигни клетки
FN - број на грешно предвидени бенигни клетки

Напомена: За да се постави рангот на карактеристиките од -1 до 1, употребете го 
атрибутот feature_range од класата MinMaxScaler.
"""

if __name__ == '__main__':

    B_dataset = [row for row in dataset if row[0]=='B']
    M_dataset = [row for row in dataset if row[0]=='M']

    train_set = M_dataset[:int(0.7 * len(M_dataset))] \
              + B_dataset[:int(0.7 * len(B_dataset))]
    train_x = [row[1:] for row in train_set]
    train_y = [row[0] for row in train_set]

    test_set = M_dataset[int(0.7 * len(M_dataset)):] \
             + B_dataset[int(0.7 * len(B_dataset)):]
    test_x = [row[1:] for row in test_set]
    test_y = [row[0] for row in test_set]

    minmax_scaler = MinMaxScaler(feature_range=(-1,1))
    minmax_scaler.fit(train_x)

    train_x = minmax_scaler.transform(train_x)
    test_x = minmax_scaler.transform(test_x)

    n_hidden = int(input())
    classifier = MLPClassifier(hidden_layer_sizes=(n_hidden,),
                               activation='relu',
                               learning_rate_init=0.001,
                               max_iter=20,
                               random_state=0)
    
    classifier.fit(train_x,train_y)

    pred_train = classifier.predict(train_x)

    tp,tn,fp,fn = 0, 0, 0, 0
    for y_true,y_pred in zip(train_y,pred_train):
        if y_true == 'M':
            if y_pred == 'M':
                tp+=1
            else:
                fn+=1
        elif y_true == "B":
            if y_pred == 'B':
                tn+=1
            else:
                fp+=1

    preciznost = tp / (tp +fp)
    odziv = tp / (tp + fn)

    print(f"Preciznost so trenirachkoto mnozhestvo: {preciznost}")
    print(f"Odziv so trenirachkoto mnozhestvo: {odziv}")

    pred_test = classifier.predict(test_x)

    tp,tn,fp,fn = 0, 0, 0, 0
    for y_true,y_pred in zip(test_y,pred_test):
        if y_true == 'M':
            if y_pred == 'M':
                tp+=1
            else:
                fn+=1
        elif y_true == "B":
            if y_pred == 'B':
                tn+=1
            else:
                fp+=1

    preciznost = tp / (tp +fp)
    odziv = tp / (tp + fn)
    
    print(f"Preciznost so testirachkoto mnozhestvo: {preciznost}")
    print(f"Odziv so testirachkoto mnozhestvo: {odziv}")
