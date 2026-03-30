import csv
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder

"""
Дадено е податочно множество за автомобили составено од категориски атрибути. Податочното 
множество поделете го на подмножества за тренирање и тестирање во сооднос 70%-30%. 
Тренирајте класификатор кој ќе одредува дали даден автомобил е прифатлив или не, со 
првите 70% од примероците, а потоа пресметајте ја точноста над останатите 30%.

Од стандарден влез се чита нов примерок за кој е потребно да се одреди класата во која 
припаѓа и да се испечати на стандарден излез. Користи Naive Bayes класификатор.
"""


def read_file(file_name):
    with open(file_name) as doc:
        csv_reader = csv.reader(doc, delimiter=',')
        dataset = list(csv_reader)[1:]

    return dataset


if __name__ == '__main__':
    dataset = read_file('NaiveBayes/car.csv')

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_set = dataset[:int(0.7 * len(dataset))]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_set = dataset[int(0.7 * len(dataset)):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifier = CategoricalNB()

    train_x_enc = encoder.transform(train_x)
    test_x_enc = encoder.transform(test_x)

    classifier.fit(train_x_enc, train_y)

    # Klasa predvidena so modelot
    pred_class_test_0 = classifier.predict([test_x_enc[0]])[0]

    # Vistinska klasa
    gt_class_test_0 = test_y[0]

    print(f'Vistinska klasa za prviot test primerok: {gt_class_test_0}')
    print(f'Predvidena klasa za prviot test primerok: {pred_class_test_0}')

    accuracy_count = 0

    for sample_X, gt_class in zip(test_x_enc, test_y):
        pred_class = classifier.predict([sample_X])[0]
        if gt_class == pred_class:
            accuracy_count += 1

    accuracy = accuracy_count / len(test_set)
    print(f'Tochnost na klasifikatorot: {accuracy}')
    
    new_sample = input()
    new_sample = new_sample.split(',')
    new_sample = encoder.transform([new_sample])

    predicted_class = classifier.predict(new_sample)[0]
    probabilities = classifier.predict_proba(new_sample)

    print(f'Nov primerok: {new_sample}')
    print(f'Predvidena klasa: {predicted_class}')
    print(f'Verojatnosti za pripadnost vo klasite: {probabilities}')
