from solaren_odblesok_dataset import dataset
from sklearn.neural_network import MLPClassifier

"""
Преголемо прилагодување (overfitting) претставува грешка на моделирање која се случува 
кога дадена функција е премногу прилагодена на лимитирано множество на податочни 
инстанци. Преголемото прилагодување на моделот најчесто се појавува кога имаме 
изградено прекомплексен модел за да се моделираат податоците кои ги проучуваме.

Дадено е податочно множество за класификација на соларните сигнали. Задачата е да се 
истренира невронска мрежа која ќе ги разликува соларните сигнали одбиени од метален 
цилиндар и оние одбиени од цилиндрични карпи. Податочното множество се состои од 15 
карактеристики и две класи. Невронската мрежа потребно е да содржи 6 неврони во 
скриениот слој, активирани со tanh активациската функција. Ратата на учење (learning_rate)
и бројот на епохи (epoch_num) потребни за тренирање на мрежата се читаат од 
стандарден влез.

Податочното множество поделете го на множество за тренирање и множество за валидација, 
во сооднос 80% : 20% од секоја од класите, односно првите 80% од конкретна класа 
влегуваат во тренирачкото множество, а следните 20% се дел од валидациското множество.

Потребно е да се детектира дали со зададените параметри за тренирање на моделот на 
невронска мрежа се случува преголемо прилагодување (overfitting) на мрежата спрема 
тренирачкото множество. Доколку точноста која се добива со тренирачкото множество е 
поголема за 15% од точноста добиена со валидациско множество, тогаш детектираме дека 
моделот прави overfitting, односно премногу се прилагодува кон тренирачкото множество. 
Точноста на моделот со дадено множество се пресметува преку формулата 
accuracy=predicted_correct/total, каде што predicted_correct претставува број на точно 
предвидени инстанци, додека total е број на сите инстанци во множеството 
(точно и неточно предвидени).

Потребно е на стандарден излез да се испечати дали се случува overfitting или не 
(Se sluchuva overfitting/Ne se sluchuva overfitting), по што се печати точноста добиена 
со тренирачкото множество и точноста со валидациското множество.
"""


if __name__ == '__main__':

    dataset_0 = [row for row in dataset if row[-1]==0]
    dataset_1 = [row for row in dataset if row[-1]==1]

    train_set = dataset_0[:int(0.8 * len(dataset_0))] \
               +dataset_1[:int(0.8 * len(dataset_1))]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    val_set = dataset_0[int(0.8 * len(dataset_0)):] \
               +dataset_1[int(0.8 * len(dataset_1)):]
    val_x = [row[:-1] for row in val_set]
    val_y = [row[-1] for row in val_set]

    
    learning_rate = float(input())
    epoch_num = int(input())

    classifier = MLPClassifier(hidden_layer_sizes=(6,),
                               activation='tanh',
                               learning_rate_init=learning_rate,
                               max_iter=epoch_num,
                               random_state=0)
    
    classifier.fit(train_x,train_y)

    pred_train = classifier.predict(train_x)
    pred_val = classifier.predict(val_x)

    accuracy_train = 0
    accuracy_val = 0

    for gt_class,pred_class in zip(train_y,pred_train):
        if gt_class==pred_class:
            accuracy_train+=1

    for gt_class,pred_class in zip(val_y,pred_val):
        if gt_class==pred_class:
            accuracy_val+=1

    accuracy_train = accuracy_train / len(train_set)
    accuracy_val = accuracy_val / len(val_set)

    if accuracy_train > accuracy_val * 1.15:
        print("Se sluchuva overfitting")
    else:
        print("Ne se sluchuva overfitting")

    print(f"Tochnost so trenirachko mnozhestvo: {accuracy_train}")
    print(f"Tochnost so validacisko mnozhestvo: {accuracy_val}")

