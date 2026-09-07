import numpy as np

np.random.seed(42)
n = 1000

x = np.random.normal(loc=50, scale=10, size=n)
y = 2.5*x + np.random.normal(loc=0, scale=15, size=n)

matriz_cov = np.cov(x,y)
cov_xy = matriz_cov[0,1]

print("Covariância entre x e y: ", cov_xy)