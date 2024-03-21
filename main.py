import pandas as pd

# Caricamento dei dati
data = pd.read_csv('tuo_file.csv')

# Analisi esplorativa
print(data.describe())

# Visualizzazione dei dati
data.hist()
