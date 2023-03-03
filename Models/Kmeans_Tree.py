from sklearn.cluster import DBSCAN, KMeans
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Caricamento dei dati
data = pd.read_csv("dataset/nofeat_acqua.csv")

# Seleziona le colonne Durata e Consumo
X = data[['Durata', 'Consumo']]


# Inizializza l'algoritmo K-means con 4 cluster
kmeans = KMeans(n_clusters=6, random_state=42)

#predict the labels of clusters.
label = kmeans.fit_predict(X)

# Aggiunta delle etichette come una nuova colonna al dataframe di dati
data["etichette"] = label
data.to_csv('dataset/acqua_etichette.csv', index=False)



'''
# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(label)) - (1 if -1 in label else 0)
n_noise_ = list(label).count(-1)

print("Estimated number of clusters: %d" % n_clusters_)
print("Estimated number of noise points: %d" % n_noise_)
'''

