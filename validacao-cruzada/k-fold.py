from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
import pandas as pd
import numpy as np

dados = fetch_california_housing()
X = pd.DataFrame(dados.data, columns = dados.feature_names)
Y = dados.target

k = 10
kf = KFold(n_splits=k, shuffle=True, random_state=42)
modelo = LinearRegression()
scores = cross_val_score(modelo, X, Y, cv=kf, scoring = 'r2')
average_r2 = np.mean(scores)

print(f"R2 Score para cada dobra: {[round(score, 4) for score in scores]}")
print(f"Média de R2 através das {k} dobras: {average_r2:.2f}")