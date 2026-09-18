from scipy import stats
import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()
nome_colunas = diabetes.feature_names
df_diabetes = pd.DataFrame(diabetes.data, columns=nome_colunas)

z = np.abs(stats.zscore(df_diabetes))


print(z)

#Eliminando outliers com z-score
threshold = 3

outliers_indices = np.where(z > threshold)[0]
sem_outliers = df_diabetes.drop(outliers_indices)

print("Formato original do dataset:", df_diabetes.shape)
print("Formato do dataset sem outliers:", sem_outliers.shape)