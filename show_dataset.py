import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

# leggi il dataset dal file CSV
data = pd.read_csv("dataset/consumo_acqua.csv")

data = data.sample(n=50, random_state=42)

# estrai le colonne delle coordinate x e y
x = data['Durata']
y = data['Consumo']

# crea un array unidimensionale con valori univoci per ciascuna classe
classes, _ = pd.factorize(data[['Compito']].values.ravel())

# crea un grafico a dispersione

class_names = {
    0: 'Bagno',
    1: 'Mani',
    2: 'Auto',
    3: 'Doccia',
    4: 'Piatti',
    5: 'Denti'
}

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

handles = []
labels = np.unique(classes)
for label in labels:
    handles.append(plt.scatter([], [], c=cmap(label), label=label))
plt.legend(handles=handles, labels=[class_names[label] for label in labels], loc='lower right')
# mostra il grafico
plt.show()
