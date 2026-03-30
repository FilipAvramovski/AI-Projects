from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier 
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from exercise1_dataset import dataset

"""
Дадено е податочно множество во променливата dataset. Последната колона ја претставува класата (0 или 1). Сите атрибути кои 
ги содржи се од нумерички тип.
Потребно е да направите 4 модели на класификација:

-Наивен баесов класификатор.
-Дрво на одлука со ентропија како критериум за избор на најдобар атрибут за поделба.
-Класификатор со колекција од 4 дрва на одлука со ентропија како критериум за избор на најдобар атрибут за поделба.
-Невронска мрежа со 10 неврони, ReLU активациска функција, 0.001 рата на учење.

Од стандарден влез се чита процентот на примероци за поделба. Првите X% од секоја класа се земаат за тренирање, 
додека останатите примероци се за тестирање. 
Изградете ги моделите на класификација и одредете кој од нив има најголема точност. На стандарден излез испечатете 
кој е класификаторот со најголема точност. (Najgolema tocnost ima klasifikatorot Naive Bayes/Decision Tree/Random Forest/MLP)
Потоа изградете уште еден модел за класификација со колекција на класификатори на следниот начин:
Класификаторот кој има најголема точност има тежина на глас 2 (класата која ја предвидува класификаторот со најголема 
точност добива 2 гласа)
Сите останати класификатори имаат тежина на глас 1
За предвидена се смета класата која што ќе добие најголем број гласови
На пример, ако класификаторот со најголема точност и уште еден класификатор ја предвидат класата 0, а останатите два 
класификатори ја предвидат класата 1, тогаш класата 0 ќе има 3 гласа, а класата 1 ќе има 2 гласа. Класификаторот ја предвидува класата 0.
Пресметајте и испечатете го одзивот на овој модел (колекцијата од класификатори).
"""

if __name__ == '__main__':
    X = int(input())

    dataset_0 = [row for row in dataset if row[-1] == 0]
    dataset_1 = [row for row in dataset if row[-1] == 1]

    train_set_0, test_set_0 = dataset_0[:int(X / 100 * len(dataset_0))], dataset_0[int(X / 100 * len(dataset_0)):]
    train_set_1, test_set_1 = dataset_1[:int(X / 100 * len(dataset_1))], dataset_1[int(X / 100 * len(dataset_1)):]

    model_1 = GaussianNB()
    model_2 = DecisionTreeClassifier(criterion='entropy', random_state=0)
    model_3 = RandomForestClassifier(n_estimators=4, criterion='entropy', random_state=0)
    model_4 = MLPClassifier(hidden_layer_sizes=(10,), activation='relu', learning_rate_init=0.001, random_state=0)

    train_set = train_set_0 + train_set_1
    test_set = test_set_0 + test_set_1

    train_X, train_Y = [row[:-1] for row in train_set], [row[-1] for row in train_set]
    test_X, test_Y = [row[:-1] for row in test_set], [row[-1] for row in test_set]

    models = [model_1, model_2, model_3, model_4]
    names = ['Naive Bayes', 'Decision Tree', 'Random Forest', 'MLP']
    accs = []
    for model in models:
        model.fit(train_X, train_Y)
        acc = model.score(test_X, test_Y)
        accs.append(acc)

    index = accs.index(max(accs))

    print(f'Najgolema tocnost ima klasifikatorot {names[index]}')

    # preds = []
    TP = 0
    FN = 0
    for row_X, class_ in zip(test_X, test_Y):
        votes_0 = 0
        votes_1 = 0

        for i, model in enumerate(models):
            prediction = model.predict([row_X])[0]
            if prediction == 0:
                votes_0 += 2 if i == index else 1
            else:
                votes_1 += 2 if i == index else 1

        final_prediction = 0 if votes_0 > votes_1 else 1
        # preds.append(final_prediction)

        if final_prediction == 1 and final_prediction == class_:
            TP += 1
        elif final_prediction == 0 and final_prediction != class_:
            FN += 1

    print(f'Odzivot na kolekcijata so klasifikatori e {TP / (TP + FN)}')
    # print(f'Odzivot na kolekcijata so klasifikatori e {recall_score(test_Y, preds)}')