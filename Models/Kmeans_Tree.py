from sklearn.cluster import KMeans
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Parte Clustering

# Caricamento dei dati
data = pd.read_csv("dataset/nofeat_acqua.csv")

# Seleziona le colonne Durata e Consumo
X = data[['Durata', 'Consumo']]


# Inizializza l'algoritmo K-means con 4 cluster
kmeans = KMeans(n_clusters=6, random_state=42)

#predict the labels of clusters.
label = kmeans.fit_predict(X)

# Aggiunta delle etichette come una nuova colonna al dataframe di dati
data["Etichetta"] = label
data.to_csv('dataset/acqua_etichette.csv', index=False)

'''
# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(label)) - (1 if -1 in label else 0)
n_noise_ = list(label).count(-1)

print("Estimated number of clusters: %d" % n_clusters_)
print("Estimated number of noise points: %d" % n_noise_)
'''

# Parte Classifier

# Caricamento dei dati etichettati
data = pd.read_csv("dataset/acqua_etichette.csv")
X_labeled = data[['Durata', 'Consumo']]
y_labeled = data[['Etichetta']]

# Divisione dei dati in training set e test set
X_train, X_test, y_train, y_test = train_test_split(X_labeled, y_labeled, test_size=0.2, random_state=42)

# Creazione di un'istanza di DecisionTreeClassifier e addestramento del modello
model = DecisionTreeClassifier(criterion = 'gini', max_depth = 15, max_features = 'sqrt', min_samples_split = 2, random_state = 36, splitter = 'best', max_leaf_nodes = 20)
model.fit(X_train, y_train)

# Valutazione della performance del modello sul test set
print(model.score(X_test, y_test))
