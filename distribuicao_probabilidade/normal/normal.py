from scipy.stats import norm
import matplotlib.pyplot as plt

data_normal = norm.rvs(size=10000, loc=0, scale=1)
plt.hist(data_normal, bins=50, color="steelblue", edgecolor="white")
plt.title("Distribuição normal")
plt.xlabel("Valor")
plt.ylabel("Frequência")
plt.show()