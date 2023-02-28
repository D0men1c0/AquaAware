import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("dataset/acqua_one_hot.csv")

X = data[['Giorno', 'Mese', 'Anno', 'Durata', 'Consumo']]
y = data[['Compito_auto','Compito_bagno','Compito_denti','Compito_doccia','Compito_mani','Compito_piatti']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

clf = DecisionTreeClassifier(max_depth=10)

clf.fit(X_train, y_train)

print(clf.score(X_test, y_test))
