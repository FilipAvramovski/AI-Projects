from krioterapija_dataset import dataset
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

"""
Дадено ни е податочно множество за третмани со криотерапија. Сите атрибути кои ги 
содржи се од непрекинат тип и може да се претпостави дека имаат непрекината распределба. 
Ваша задача е да истренирате наивен баесов класификатор кој ќе предвидува дали 
терапијата е успешна или не (1 и 0) користејќи ги првите 85% од даденото податочно 
множество. Треба да ја пресметате точноста која ја добивате над останатите 15% од 
податочното множество и потоа да направите предвидувања на записи кои ги примате на влез.

Во почетниот код имате дадено податочно множество. На влез се прима еден запис за кој 
треба да се направи предвидување на класата. На излез треба да се испечати точноста на 
моделот, класата на предвидување како и веројатностите за припадност во класите.
"""


# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['1', '35', '12', '5', '1', '100', '0'], 
                  ['1', '29', '7', '5', '1', '96', '1'],
                  ['1', '50', '8', '1', '3', '132', '0'], 
                  ['1', '32', '11.75', '7', '3', '750', '0'],
                  ['1', '67', '9.25', '1', '1', '42', '0']]

if __name__ == '__main__':
    threshold = int(0.85 * len(dataset))

    train_data = dataset[:threshold]
    train_X = [[float(val) for val in row[:-1]] for row in train_data]
    train_Y = [row[-1] for row in train_data]

    test_data = dataset[threshold:]
    test_X = [[float(val) for val in row[:-1]] for row in test_data]
    test_Y = [row[-1] for row in test_data]

    classifier = GaussianNB()
    classifier.fit(train_X, train_Y)

    accuracy = 0
    predictions=classifier.predict(test_X)
    for gt_class,pred_class in zip(test_Y,predictions):
        if pred_class == gt_class:
            accuracy += 1

    accuracy = accuracy / len(test_data)

    new_sample = input().split(" ")
    new_sample = [[float(i) for i in new_sample]]
    predicted_class = classifier.predict(new_sample)[0]
    probabilities = classifier.predict_proba(new_sample)

    print(accuracy)
    print(predicted_class)
    print(probabilities)