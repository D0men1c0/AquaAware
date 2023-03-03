import csv
import random
import numpy as np
from function_utils import *

start_date = date(year=2022, month=3, day=1)
stop_date = date(year=2022, month=7, day=25)

#lista date
date_ls = return_list(start_date, stop_date)

#tempo espresso in minuti
#acqua espressa in litri
task_durata_acqua = {
    "mani": {"acqua": [round(x, 2) for x in np.linspace(0.1, 0.8, 9).tolist()],
            "tempo": [round(x, 2) for x in np.linspace(0.3, 0.8, 10).tolist()]
    },
    "bagno": {"acqua": [round(x, 2) for x in np.linspace(80, 140, 10).tolist()],
            "tempo": [round(x, 2) for x in np.linspace(20, 50, 5).tolist()]
    },
    "doccia": {"acqua": [round(x, 2) for x in np.linspace(15, 35, 10).tolist()],
            "tempo": [round(x, 2) for x in np.linspace(3, 10, 8).tolist()]
    },
    "denti": {"acqua": [round(x, 2) for x in np.linspace(0.2, 1, 10).tolist()],
            "tempo": [round(x, 2) for x in np.linspace(1, 3, 5).tolist()]
    },
    "piatti": {"acqua": [round(x, 2) for x in np.linspace(12, 22, 10).tolist()],
            "tempo": [round(x, 2) for x in np.linspace(18, 38, 5).tolist()]
    },
    "auto": {"acqua": [round(x, 2) for x in np.linspace(110, 160, 10).tolist()],
            "tempo": [round(x, 2) for x in np.linspace(18, 38, 5).tolist()]
    }
}

# Apertura del file CSV in modalità scrittura
with open('dataset/nofeat_acqua.csv', mode='w', newline='') as csv_file:
    # Definizione delle colonne del CSV
    fieldnames = ['Data', 'Durata', 'Consumo']
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
                             'Consumo': acqua
                             })

