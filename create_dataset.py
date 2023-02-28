import csv
import random
import numpy as np

from utils import *

start_date = date(year=2022, month=1, day=1)
stop_date = date(year=2022, month=12, day=31)

#lista date
date_ls = return_list(start_date, stop_date)

#tempo espresso in minuti
#acqua espressa in litri
task_durata_acqua = {
    "mani": {"acqua": [round(x, 2) for x in np.linspace(0.2, 1, 9).tolist()],
            "tempo": [round(x, 2) for x in np.linspace(0.5, 1, 10).tolist()]
    },
    "bagno": {"acqua": [round(x, 2) for x in np.linspace(100, 160, 10).tolist()],
            "tempo": [round(x, 2) for x in np.linspace(30, 60, 5).tolist()]
    },
    "doccia": {"acqua": [round(x, 2) for x in np.linspace(20, 40, 10).tolist()],
            "tempo": [round(x, 2) for x in np.linspace(4, 11, 8).tolist()]
    },
    "denti": {"acqua": [round(x, 2) for x in np.linspace(0.3, 1.2, 10).tolist()],
            "tempo": [round(x, 2) for x in np.linspace(2, 4, 5).tolist()]
    },
    "piatti": {"acqua": [round(x, 2) for x in np.linspace(15, 25, 10).tolist()],
            "tempo": [round(x, 2) for x in np.linspace(20, 40, 5).tolist()]
    },
    "auto": {"acqua": [round(x, 2) for x in np.linspace(120, 170, 10).tolist()],
            "tempo": [round(x, 2) for x in np.linspace(20, 40, 5).tolist()]
    }
}

# Apertura del file CSV in modalità scrittura
with open('consumo_acqua.csv', mode='w', newline='') as csv_file:
    # Definizione delle colonne del CSV
    fieldnames = ['Data', 'Durata', 'Consumo', "Compito"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Scrittura dell'intestazione del CSV
    writer.writeheader()

    # Popolazione del CSV con dati casuali
    for dt in date_ls:
        for task, values in task_durata_acqua.items():
            durata = random.choice(values['tempo'])
            acqua = random.choice(values['acqua'])
            writer.writerow({'Data': dt,
                             'Durata': durata,
                             'Consumo': acqua,
                             'Compito': task})

