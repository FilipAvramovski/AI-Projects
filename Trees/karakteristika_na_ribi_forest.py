from karakteristika_na_ribi_dataset import dataset
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

"""
Дадено ни е податочно множество за карактеристики на риби. Сите атрибути кои ги содржи 
се од непрекинат тип. Ваша задача е да истренирате класификатор - колекција од дрва на 
одлука кој ќе предвидува класи на тип на риби користејќи ги првите 85% од даденото 
податочно множество. Треба да ја пресметате точноста која ја добивате над останатите 
15% од податочното множество. Притоа, се користи дел од множеството во кој е отстранета 
колоната col_index.

Во почетниот код имате дадено податочно множество. На влез се прима индекс на колоната 
која треба да се отстрани col_index. Дополнително се вчитува бројот на дрва на одлука 
кои ќе се користат и вредност за критериумот за избор на најдобар атрибут. На крај, се 
вчитува нов запис кој треба да се класифицира со тренираниот класификатор.

На излез треба да се испечати точност на класификаторот, предвидената класа за новиот 
запис и веројатностите за припадност во класите.

Напомена: бидејќи вредностите се од непрекинат тип, нема потреба да ги претворите во 
целобројни вредности.

За да ги добиете истите резултати како и во тест примерите, при креирање на 
класификаторот поставете random_state=0.
"""

if __name__=='__main__': 
    col_index=int(input())

    dataset2=[]

    for row in dataset:
        dataset2.append(row[:col_index]+row[col_index+1:])

    threshold=int(0.85*len(dataset2))

    train_set=dataset2[:threshold]
    train_X=[row[:-1] for row in train_set]
    train_Y=[row[-1] for row in train_set]
    
    test_set=dataset2[threshold:]
    test_X=[row[:-1] for row in test_set]
    test_Y=[row[-1] for row in test_set]

    n_trees=int(input())
    crit=input()
    classifier=RandomForestClassifier(n_estimators=n_trees,criterion=crit,random_state=0)
    classifier.fit(train_X,train_Y)

    predicions=classifier.predict(test_X)
    accuracy=accuracy_score(test_Y,predicions)
    print(f'Accuracy: {accuracy}')

    new_input=input().split()
    new_input=new_input[:col_index]+new_input[col_index+1:]

    pred_class=classifier.predict([new_input])[0]
    print(pred_class)
    probabilities=classifier.predict_proba([new_input])[0]
    print(probabilities)
