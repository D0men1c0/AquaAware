import csv
from utils import *

start_date = date(year=2022, month=1, day=1)
stop_date = date(year=2022, month=12, day=31)
date_ls = return_list(start_date, stop_date)
print(date_ls)

#tempo espresso in minuti
#acqua espressa in litri
task_durata_acqua = {
    "mani": {"acqua": list(range(0.2, 1)),
            "tempo": list(range(0.5, 1))
    },
    "bagno": {"acqua": list(range(100, 160)),
            "tempo": list(range(30, 60))
    },
    "doccia": {"acqua": list(range(20, 40)),
            "tempo": list(range(4, 11))
    },
    "denti": {"acqua": list(range(0.3, 1.2)),
            "tempo": list(range(2,4))
    },
    "piatti": {"acqua": list(range(15, 25)),
            "tempo": list(range(20,40))
    },
    "auto": {"acqua": list(range(120, 170)),
            "tempo": list(range(20,40))
    }
}




'''
# Definiamo il nome del file CSV e il numero di colonne
file_name = "consumo_acqua.csv"
num_cols = 4

# Definiamo i dati da scrivere nel file CSV
tasks = []
num_tasks = 300
task = {}


for i in range(num_tasks):
    task['Data'] = 
    tasks.append(task)
'''
