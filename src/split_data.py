from sklearn.model_selection import train_test_split

def create_splits(X, y, ratios=[(0.4,0.6),(0.6,0.4),(0.8,0.2),(0.9,0.1)]):
    splits=[]
    for i,(tsize,_) in enumerate(ratios):
        X_train,X_test,y_train,y_test=train_test_split(
            X,y,train_size=tsize,stratify=y,random_state=42
        )
        splits.append((X_train,X_test,y_train,y_test))
    return splits