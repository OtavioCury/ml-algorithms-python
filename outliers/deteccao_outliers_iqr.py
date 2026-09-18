from scipy import stats
import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()
nome_colunas = diabetes.feature_names
df_diabetes = pd.DataFrame(diabetes.data, columns=nome_colunas)

print(df_diabetes.shape)

#Eliminando outliers com iqr
Q1 = np.percentile(df_diabetes['bmi'], 25, method='midpoint')
Q3 = np.percentile(df_diabetes['bmi'], 75, method='midpoint')
iqr = Q3 - Q1

print(iqr)

superior = Q3 + 1.5*iqr
array_superior = np.where(df_diabetes['bmi'] > superior)[0]
print("Limite superior: ", superior)
df_diabetes.drop(index=array_superior, inplace=True)

inferior = Q1 - 1.5*iqr
array_inferior = np.where(df_diabetes['bmi'] < inferior)[0]
print("Limite inferior: ", inferior)
df_diabetes.drop(index=array_inferior, inplace=True)

print(df_diabetes.shape)