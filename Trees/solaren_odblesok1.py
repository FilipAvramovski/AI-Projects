from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OrdinalEncoder
from solaren_odblesok_dataset import dataset 

if __name__ == "__main__":
    encoder = OrdinalEncoder()
    encoder.fit([row[:-1]for row in dataset])

    x = int(input())
    
    train_set = dataset[:-x]
    train_x = [row[:-1] for row in train_set]
    train_y = [int(row[-1]) for row in train_set]

    
    test_set = dataset[-x:]
    test_x = [row[:-1] for row in test_set]
    test_y = [int(row[-1]) for row in test_set]

    train_x = encoder.transform(train_x)
    test_x = encoder.transform(test_x)

    classifier = DecisionTreeClassifier(criterion='gini',random_state=0)
    classifier.fit(train_x,train_y)
    pred = classifier.predict(test_x)

    tp,tn,fp,fn = 0,0,0,0
    for gt_class,pred_class in zip(test_y,pred):
        if gt_class == 1:
            if pred_class == 1:
                tp += 1
            else:
                fn += 1
        elif gt_class == 0:
            if pred_class == 1:
                fp += 1
            else:
                tn += 1


    accuracy = (tp + tn) / (tp + tn + fp + fn)

    if tp+fp==0:
        precision=0.0
    else:
        precision = tp / (tp + fp)
    
    print(f"Accuracy: {accuracy}")
    print(f"Precision: {precision}")