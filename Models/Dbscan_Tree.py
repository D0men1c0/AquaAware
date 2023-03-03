from sklearn.cluster import DBSCAN, KMeans
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Caricamento dei dati
data = pd.read_csv("dataset/nofeat_acqua.csv")

# Seleziona le colonne Durata e Consumo
X = data[['Durata', 'Consumo']]


# Creazione di un'istanza di DBSCAN e addestramento del modello
dbscan = DBSCAN(eps = 7, min_samples = 10)
dbscan.fit(X)

# Ottenimento delle etichette di cluster
labels = dbscan.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print("Estimated number of clusters: %d" % n_clusters_)
print("Estimated number of noise points: %d" % n_noise_)

# Aggiunta delle etichette come una nuova colonna al dataframe di dati
data["etichette"] = labels
data.to_csv('dataset/acqua_etichette.csv', index=False)


'''
# Inizializza l'algoritmo K-means con 4 cluster
kmeans = KMeans(n_clusters=6, random_state=42)

#predict the labels of clusters.
label = kmeans.fit_predict(X)

print(label)
'''



