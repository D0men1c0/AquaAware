from datetime import datetime, date, timedelta
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def date_range_list(start_date, end_date):
    # Return generator for a list datetime.date objects (inclusive) between start_date and end_date (inclusive).
    curr_date = start_date
    while curr_date <= end_date:
        yield curr_date 
        curr_date += timedelta(days=1)

  
def return_list(start_date, end_date):
    sets = date_range_list(start_date, end_date)
    date_list_formattate = []
    for data in sets:
        data_formattata = data.strftime("%d/%m/%y")
        date_list_formattate.append(data_formattata)

    return date_list_formattate


def init_ml():
    # Caricamento del dataset
    data = pd.read_csv("dataset/consumo_acqua.csv")

    # Modifica data
    data['Data'] = pd.to_datetime(data['Data'])
    data.insert(1, column = "Anno", value = 0)
    data.insert(1, column = "Mese", value = 0)
    data.insert(1, column = "Giorno", value = 0)

    for idx, row in data.iterrows():
        time_str = row['Data'].strftime('%Y-%m-%d')
        time = datetime.strptime(time_str, '%Y-%m-%d')

        data.loc[idx, 'Anno'] = time.year
        data.loc[idx, 'Mese'] = time.month
        data.loc[idx, 'Giorno'] = time.day
    data.drop(['Data'], axis=1, inplace=True)

    # Scaler
    X = data[['Durata', 'Consumo']]
    scaler = MinMaxScaler()
    X = scaler.fit_transform(X.values)
    data[['durata_scalata', 'consumo_scalato']] = X

    # Rimuovo le vecchie colonne
    data = data.drop(['Durata', 'Consumo'], axis=1)
    data = data.rename(columns={'durata_scalata': 'Durata', 'consumo_scalato': 'Consumo'})

    # Applicazione del one-hot encoding
    one_hot = pd.get_dummies(data['Compito'], prefix='Compito')
    data = pd.concat([data, one_hot], axis=1)
    data = data.drop('Compito', axis=1)

    # Salvataggio del dataset aggiornato
    data.to_csv('dataset/acqua_one_hot.csv', index=False)

init_ml()