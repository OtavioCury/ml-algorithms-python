import pandas as pd
#carregando o dataset corretamente
data = pd.read_csv("/home/otavio/ml-algorithms-python/pandas/datasets/GasPricesinBrazil_2004-2019.csv", sep=";")
print(data.head(10))
print(data.info())
print(type(data))