from solaren_odblesok_dataset import dataset
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB

"""
Дадено ни е податочно множество за соларен одблесок. Сите атрибути кои ги содржи се од 
категориски тип (последната колона е класен атрибут). Ваша задача е да истренирате 
наивен баесов класификатор кој ќе предвидува класи на соларен одблесок користејќи ги 
првите 75% од даденото податочно множество. Треба да ја пресметате точноста која ја 
добивате над останатите 25% од податочното множество и потоа да направите предвидувања 
на записи кои ги примате на влез.

Во почетниот код имате дадено податочно множество. На влез се прима еден запис за кој 
треба да се направи предвидување на класата. На излез треба да се испечати точноста на 
моделот, класата на предвидување како и веројатностите за припадност во класите.
"""

dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__ == '__main__':

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    threshold = int(0.75 * len(dataset))

    train_data = dataset[:threshold]
    train_X = [row[:-1] for row in train_data]
    train_Y = [row[-1] for row in train_data]

    test_data = dataset[threshold:]
    test_X = [row[:-1] for row in test_data]
    test_Y = [row[-1] for row in test_data]

    train_X_enc = encoder.transform(train_X)
    test_X_enc = encoder.transform(test_X)

    classifier = CategoricalNB()
    classifier.fit(train_X_enc, train_Y)

    pred=classifier.predict(test_X_enc)

    accuracy = 0
    for pred_class, gt_class in zip(pred, test_Y):
        if pred_class == gt_class:
            accuracy += 1

    accuracy = accuracy / len(test_Y)

    new_sample = input().split(" ")
    new_sample = encoder.transform([new_sample])
    predicted_class = classifier.predict(new_sample)[0]
    probabilities = classifier.predict_proba(new_sample)

    print(accuracy)
    print(predicted_class)
    print(probabilities)