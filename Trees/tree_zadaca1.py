from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from Trees.tree_zadaca1_dataset import dataset

if __name__=='__main__': 
    percent=int(input())
    criterion=input()
    max_leaves=int(input())

    threshold=int(percent/100*len(dataset))

    train_set=dataset[:threshold]
    train_X=[row[:-1] for row in train_set]
    train_Y=[row[-1] for row in train_set]

    test_set=dataset[threshold:]
    test_X=[row[:-1] for row in test_set]
    test_Y=[row[-1] for row in test_set]


    model1=DecisionTreeClassifier(criterion=criterion,max_leaf_nodes=max_leaves,random_state=0)
    model1.fit(train_X,train_Y)

    predictions1=model1.predict(test_X)
    accuracy1=accuracy_score(test_Y,predictions1)

    models=[]
    
    for class_ in ['Perch','Roach','Bream']:
        model2=DecisionTreeClassifier(criterion=criterion,max_leaf_nodes=max_leaves,random_state=0)
        model2.fit(train_X,[1 if label==class_ else 0 for label in train_Y])
        models.append((class_,model2))

    counter=0
    
    for row_X,label in zip(test_X,test_Y):
        all_models_predict_correctly=True
        for class_,model2 in models:
            pred=model2.predict([row_X])[0]
            if label==class_:
                if pred!=1:
                    all_models_predict_correctly=False
                    break
            else:
                if pred!=0:
                    all_models_predict_correctly=False
                    break

        if all_models_predict_correctly:
            counter+=1
    
    accuracy2=counter/len(test_X)

    print(f'Tochnost so originalniot klasifikator: {accuracy1}')
    print(f'Tochnost so kolekcija od klasifikatori: {accuracy2}')


