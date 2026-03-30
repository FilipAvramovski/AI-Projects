import csv
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import MinMaxScaler


"""Дадено е податочно множество за класификација на квалитет на вино. Секоја инстанца е претставена со 11 хемиски карактеристики
и една класа за добар ('good') и лош ('bad') квалитет на вино. Променете го податочното множество така што првата и последната
хемиска карактеристика ќе ги замените со збирот на соодветните вредности. Новата карактеристика поставете ја како прва колона
во множеството. Новата верзија на податочното множество треба да има 10 хемиски карактеристики.
Поделете го податочното множество на множества за тренирање и тестирање на следниот начин. Ако критериумот за поделба C има 
вредност 0 за тренирање се користат првите P проценти од секоја од класите, а за тестирање останатите 100 - P проценти. Ако 
критериумот за поделба C има вредност 1 за тренирање се користат последните P проценти од секоја од класите, а за тестирање 
останатите 100 - P проценти. При поделба користете ја прво класата good, а потоа класата bad. Потоа скалирајте ги атрибутите во рангот [-1, 1].
Направете наивен баесов класификатор кој ќе го тренирате со верзијата на податочното множество во која првата и последната 
хемиска карактеристика се заменети со нивниот збир без примена на скалирање. Потоа, направете и втор наивен баесов класификатор 
кој ќе го тренирате со верзијата на податочното множество во која првата и последната хемиска карактеристика се заменети со 
нивниот збир и потоа е применето скалирање. Испечатете ја точноста на двата класификатори.
Од стандарден влез прво се чита критериумот за поделба C, а потоа се чита процентот за поделба P.
На стандарден излез да се испечати точноста добиена со двата класификатори. Користи Naive Bayes класификатор."""


def read_dataset():
    data = []
    with open('NaiveBayes/winequality.csv') as f:
        _ = f.readline()
        while True:
            line = f.readline().strip()
            if line == '':
                break
            parts = line.split(';')
            data.append(list(map(float, parts[:-1])) + parts[-1:])

    return data

def main():
    C=int(input())
    P=int(input())

    dataset=read_dataset()
    dataset2=[]

    for row in dataset:
        sum=row[0]+row[10]
        dataset2.append([sum]+row[1:10]+[row[11]])

    good = [row for row in dataset2 if row[-1] == 'good']
    bad = [row for row in dataset2 if row[-1] == 'bad']

    
    if C==0:
        threshold_good=int((P/100)*len(good))
        threshold_bad=int((P/100)*len(bad))

        train_set=good[:threshold_good]+bad[:threshold_bad]
        test_set=good[threshold_good:]+bad[threshold_bad:]
    elif C==1:
        threshold_good=int((100-P)/100*len(good))
        threshold_bad=int((100-P)/100*len(bad))

        train_set=good[threshold_good:]+bad[threshold_bad:]
        test_set=good[:threshold_good]+bad[:threshold_bad]

    train_X=[row[:-1] for row in train_set]
    train_Y=[row[-1] for row in train_set]
    test_X=[row[:-1] for row in test_set]
    test_Y=[row[-1] for row in test_set]

    print(f'Broj na podatoci vo train se: {len(train_set)}')
    print(f'Broj na podatoci vo test se: {len(test_set)}')

    classifier=GaussianNB()
    classifier.fit(train_X,train_Y)
    predictions=classifier.predict(test_X)
    
    counter=0
    for gt_class, pred_class in zip(test_Y, predictions):
        if gt_class == pred_class:
            counter += 1
    
    accuracy=counter/len(test_set)

    print(f'Tochnost so zbir na koloni: {accuracy}')

    scaler=MinMaxScaler(feature_range=(-1,1))
    scaler.fit(train_X)
    train_X=scaler.transform(train_X)
    test_X=scaler.transform(test_X)

    classifier=GaussianNB()
    classifier.fit(train_X,train_Y)
    predictions=classifier.predict(test_X)

    counter=0
    for gt_class, pred_class in zip(test_Y, predictions):
        if gt_class == pred_class:
            counter += 1
    
    accuracy=counter/len(test_set)

    print(f'Tochnost so zbir na koloni i skaliranje: {accuracy}')

main()
