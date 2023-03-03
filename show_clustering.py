import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

# leggi il dataset dal file CSV
data = pd.read_csv("dataset/acqua_etichette.csv")


# estrai le colonne delle coordinate x e y
x = data['Durata']
y = data['Consumo']

# crea un array unidimensionale con valori univoci per ciascuna classe
classes, _ = pd.factorize(data[['Etichetta']].values.ravel())


# assegna una lista di colori a ciascuna classe
cmap = ListedColormap(['red', 'blue', 'green', 'yellow', 'orange', 'purple'])

# crea un grafico a dispersione
plt.scatter(x, y, c=classes, cmap=cmap)

# aggiungi le etichette degli assi e il titolo del grafico
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Relazione durata e consumo per ogni task')
plt.xlabel('Durata (minuti)')
plt.ylabel('Consumo (litri)')


# mostra il grafico
plt.show()
