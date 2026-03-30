import csv
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

"""
Дадено е податочно множество со информации за нивото на глукоза во крвта и крвен притисок 
составено од атрибути со непрекинати вредности. Податочното множество поделете го на 
подмножества за тренирање и тестирање во сооднос 70%-30%. Тренирајте класификатор кој ќе 
предвидува дали личноста има дијабетес или не, со првите 70% од примероците, а потоа 
пресметајте ја точноста над останатите 30%.

Од стандарден влез се чита нов примерок за кој е потребно да се одреди класата во која 
припаѓа и да се испечати на стандарден излез. Користи Naive Bayes класификатор.
"""

def read_file(file_name):
    with open(file_name) as doc:
        csv_reader = csv.reader(doc, delimiter=',')
        dataset = list(csv_reader)[1:]

    dataset_v2 = []
    for row in dataset:
        row_v2 = [int(el) for el in row]
        dataset_v2.append(row_v2)

    return dataset_v2


if __name__ == '__main__':
    dataset = read_file('NaiveBayes/medical_data.csv')

    train_set = dataset[:int(0.7 * len(dataset))]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_set = dataset[int(0.7 * len(dataset)):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifier = GaussianNB()

    classifier.fit(train_x, train_y)

    accuracy_count = 0

    predictions = classifier.predict(test_x)

    for gt_class, pred_class in zip(test_y, predictions):
        if gt_class == pred_class:
            accuracy_count += 1

    acc = accuracy_score(test_y, predictions)

    accuracy = accuracy_count / len(test_set)
    print(f'Tochnosta na klasifikatorot e: {accuracy}')

    new_sample = input()
    new_sample = [int(el) for el in new_sample.split(',')]

    predicted_class = classifier.predict([new_sample])[0]
    probabilities = classifier.predict_proba([new_sample])

    print(f'Nov primerok: {new_sample}')
    print(f'Predvidena klasa: {predicted_class}')
    print(f'Verojatnosti za pripadnost vo klasite: {probabilities}')