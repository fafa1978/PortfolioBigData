import pandas as pd


data = pd.read_csv('tuo_file.csv')


print(data.describe())

data.hist()
