import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
nomes = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(url, names=nomes)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]

teste = SelectKBest(score_func=chi2, k=4)
fit = teste.fit(X, Y)

np.set_printoptions(precision=3)
print(fit.scores_)

# mostra os nomes das features selecionadas
mask = teste.get_support()
features_selecionadas = [nomes[i] for i, selecionada in enumerate(mask) if selecionada]
print("Características escolhidas:")
print(features_selecionadas)

features = fit.transform(X)
# Summarize selected features
print(features[0:5,:])