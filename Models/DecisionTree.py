import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

data = pd.read_csv("dataset/acqua_one_hot.csv")

X = data[['Giorno', 'Mese', 'Anno', 'Durata', 'Consumo']]
y = data[['Compito_auto','Compito_bagno','Compito_denti','Compito_doccia','Compito_mani','Compito_piatti']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

'''
# set best parameters
param_grid = {'max_depth': list(range(10, 18)),
            'min_samples_split': [2, 5, 10],
            'criterion': ['gini', 'entropy', 'log_loss'],
            'splitter': ['best', 'random'],
            'max_features': ['sqrt', 'log2'],
            'random_state': list(range(0, 50)),
            'max_leaf_nodes': list(range(0, 9))
            }

base_estimator = DecisionTreeClassifier(random_state=0)

# Use grid search to find the best hyperparameters
grid_search = GridSearchCV(base_estimator, param_grid, cv=6)
grid_search.fit(X_train, y_train)

# Print the best hyperparameters and corresponding accuracy
print("Best hyperparameters: ", grid_search.best_params_)
print("Best accuracy: ", grid_search.best_score_)
'''

clf = DecisionTreeClassifier(criterion = 'gini', max_depth = 15, max_features = 'sqrt', min_samples_split = 2, random_state = 36, splitter = 'best', max_leaf_nodes = 20)
clf.fit(X_train, y_train)

print(clf.score(X_test, y_test))
