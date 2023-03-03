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
    "mani": {"acqua": [round(x, 2) for x in np.linspace(0.18, 0.72, 9).tolist()],
            "tempo": [round(x, 2) for x in np.linspace(0.45, 0.9, 10).tolist()]
    },
    "bagno": {"acqua": [round(x, 2) for x in np.linspace(85, 136, 10).tolist()],
            "tempo": [round(x, 2) for x in np.linspace(28.5, 57, 5).tolist()]
    },
    "doccia": {"acqua": [round(x, 2) for x in np.linspace(18, 36, 10).tolist()],
            "tempo": [round(x, 2) for x in np.linspace(3.6, 9.9, 8).tolist()]
    },
    "denti": {"acqua": [round(x, 2) for x in np.linspace(0.24, 0.96, 10).tolist()],
            "tempo": [round(x, 2) for x in np.linspace(2, 3.2, 5).tolist()]
    },
    "piatti": {"acqua": [round(x, 2) for x in np.linspace(12, 20, 10).tolist()],
            "tempo": [round(x, 2) for x in np.linspace(19, 38, 5).tolist()]
    },
    "auto": {"acqua": [round(x, 2) for x in np.linspace(102, 145, 10).tolist()],
            "tempo": [round(x, 2) for x in np.linspace(18, 36, 5).tolist()]
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

