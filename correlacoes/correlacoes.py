import numpy as np
import scipy.stats as stats


experiencia = [1, 3, 4, 5, 5, 6, 7, 10, 11, 12, 15, 20, 25, 28, 30,35]
salario = [20000, 30000, 40000, 45000, 55000, 60000, 80000, 100000, 130000, 150000, 200000, 230000, 250000, 300000, 350000, 400000]


print("Matriz de correlação de Pearson", np.corrcoef(experiencia, salario))

spearman_corr, p_value = stats.spearmanr(experiencia, salario)
print("Correlação de Spearman", spearman_corr)

kendall_corr, _ = stats.kendalltau(experiencia, salario)
print("Correlação de Kendall", kendall_corr)
