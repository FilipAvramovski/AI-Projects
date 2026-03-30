from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from tree_zadaca2_dataset import dataset

"""
Дадено е податочно множество за класификација на тип на стакло. Податочното множество содржи 9 атрибути кои го 
претставуваат хемискиот состав на стаклото (силикон, калиум, калциум, алуминиум, железо, итн.). Класниот атрибут 
го претставува типот на стакло и има 7 вредности.
Податочното множество поделете го на подмножества за тренирање и тестирање така што првите N примероци ќе се 
користат за тестирање, а останатите за тренирање. Со помош на класификатор - дрво на одлука со најмногу L листови 
одредете го најважниот атрибут и отстранете го. Потоа скалирајте ги атрибутите со StandardScaler.
Потребно е да проверите како скалирањето на податоци влијае врз класификацијата на типот на стакло доколку се 
отстрани најважниот атрибут. Направете класификатор - колекција од D дрва на одлука кои користат gini како критериум 
за избор на најдобар атрибут за поделба. Тренирајте го класификаторот со оригиналното податочно множество и со множеството од кое е отстранет најважниот атрибут, а останатите атрибути се скалирани. Потоа пресметајте ја точноста која се добива со множеството за тестирање.
Од стандарден влез прво се чита вредноста N za бројот на примероци во множеството за тестирање. Потоа се читаат 
вредноста L за максималниот број на листови и вредноста D за бројот на дрва на одлука.
На стандарден излез да се испечати точноста добиена со двата класификатори. Потоа да се испечати како скалирањето 
на атрибути влијае врз точноста („Skaliranjeto na atributi ja podobruva tochnosta“, „Skaliranjeto na atributi ne 
ja podobruva tochnosta“, или „Skaliranjeto na atributi nema vlijanie“).
За да ги добиете истите резултати како и во тест примерите, при креирање на класификаторите поставете random_state=0.
"""

if __name__ == '__main__':
    N=int(input())
    L=int(input())
    D=int(input())

    train_set=dataset[N:]
    train_X=[row[:-1] for row in train_set]
    train_Y=[row[-1] for row in train_set]

    test_set=dataset[:N]
    test_X=[row[:-1] for row in test_set]
    test_Y=[row[-1] for row in test_set]

    model=DecisionTreeClassifier(max_leaf_nodes=L,random_state=0)
    model.fit(train_X,train_Y)

    feature_importances=list(model.feature_importances_)
    max_importances=feature_importances.index(max(feature_importances))
    
    train_X_moded=[[el for ind,el in enumerate(row) if ind!=max_importances] for row in train_X]
    test_X_moded=[[el for ind,el in enumerate(row) if ind!=max_importances] for row in test_X]

    scaler=StandardScaler()
    scaler.fit(train_X_moded)
    train_X_scaled=scaler.transform(train_X_moded)
    test_X_scaled=scaler.transform(test_X_moded)

    model=RandomForestClassifier(n_estimators=D,criterion='gini',random_state=0)
    
    model.fit(train_X,train_Y)
    accuracy1=model.score(test_X,test_Y)
    print(f'Tochnost so originalnoto podatochno mnozestvo: {accuracy1}')

    model.fit(train_X_scaled,train_Y)
    accuracy2=model.score(test_X_scaled,test_Y)
    print(f'Tochnost so skalirani atributi: {accuracy2}')

    if accuracy2>accuracy1:
        print('Skaliranjeto na atributi ja podobruva tochnosta')
    elif accuracy2<accuracy1:
        print('Skaliranjeto na atributi ne ja podobruva tochnosta')
    else:
        print('Skaliranjeto na atributi nema vlijanie')