from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier
from solaren_odblesok_dataset import dataset

"""
Дадено ни е податочно множество за соларен одблесок. Сите атрибути кои ги содржи се од 
категориски тип. Ваша задача е да истренирате класификатор - дрво на одлука кој ќе 
предвидува класи на соларен одблесок користејќи ги последните X% од даденото податочно 
множество. Треба да ја пресметате точноста која ја добивате над останатите (100 - X)% 
од податочното множество.

Во почетниот код имате дадено податочно множество. На влез се прима вредност за 
процентот на поделба X. На пример, ако вредноста е 80 значи дека ги користите 
последните 80% од множеството за тренирање, а првите 20% за тестирање. Дополнително во 
променливата criterion се вчитува вредност за критериумот за избор на најдобар атрибут.

На излез треба да се испечати точност, длабочина и број на листови на изграденото дрво, 
како и карактеристиките со најголема и најмала важност.

За да ги добиете истите резултати како и во тест примерите, при креирање на 
класификаторот поставете random_state=0
"""

dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__=="__main__":

    encoder=OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    x=float(input())
    threshold = int(((100-x)/100)*len(dataset))

    train_set=dataset[threshold:]
    train_x=[row[:-1] for row in train_set]
    train_y=[row[-1] for row in train_set]
    train_x=encoder.transform(train_x)

    test_set=dataset[:threshold]
    test_x=[row[:-1] for row in test_set]
    test_y=[row[-1] for row in test_set]
    test_x=encoder.transform(test_x)

    crit=input()
    classifier=DecisionTreeClassifier(criterion=crit,random_state=0)
    classifier.fit(train_x,train_y)

    print(f'Depth: {classifier.get_depth()}')
    print(f'Number of leaves: {classifier.get_n_leaves()}')

    accuracy=0

    for i in range(len(test_set)):
        predicted_class=classifier.predict([test_x[i]])[0]
        true_class=test_y[i]
        if predicted_class==true_class:
            accuracy+=1

    accuracy=accuracy/len(test_set)
    print(f'Accuracy: {accuracy}')

    features_importances=list(classifier.feature_importances_)

    most_important_feature=features_importances.index(max(features_importances))
    print(f'Most important feature: {most_important_feature}')

    least_important_feature=features_importances.index(min(features_importances))
    print(f'Least important feature: {least_important_feature}')


