import numpy as np
from scipy import stats
import statistics

np.random.seed(42)
n = 1000

# Dados assimétricos (distribuição exponencial) para evidenciar a diferença entre as medidas
dados = np.random.exponential(scale=20, size=n).round(0)

# Média aritmética: soma dos valores dividida pela quantidade
media = np.mean(dados)

# Mediana: valor central dos dados ordenados (robusta a outliers)
mediana = np.median(dados)

# Moda: valor mais frequente
moda = stats.mode(dados, keepdims=False)
moda_statistics = statistics.multimode(dados.tolist())

# Média aparada: descarta 10% dos menores e 10% dos maiores valores antes de calcular a média
media_aparada = stats.trim_mean(dados, proportiontocut=0.1)

# Média geométrica: raiz n-ésima do produto (apenas valores positivos), útil para taxas de crescimento
media_geometrica = stats.gmean(dados[dados > 0])

# Média harmônica: n dividido pela soma dos inversos (apenas valores positivos), útil para razões e velocidades
media_harmonica = stats.hmean(dados[dados > 0])

# Média ponderada: cada valor contribui de acordo com seu peso
notas = np.array([7.0, 8.5, 6.0, 9.0])
pesos = np.array([2, 3, 1, 4])
media_ponderada = np.average(notas, weights=pesos)

print("Média: ", media)
print("Mediana: ", mediana)
print("Moda (scipy): ", moda.mode, "- frequência:", moda.count)
print("Moda(s) (statistics): ", moda_statistics)
print("Média aparada (10%): ", media_aparada)
print("Média geométrica: ", media_geometrica)
print("Média harmônica: ", media_harmonica)
print("Média ponderada das notas: ", media_ponderada)

# Efeito de um outlier: a média se desloca bastante, a mediana quase não muda
dados_com_outlier = np.append(dados, 5000)
print("\nMédia com outlier: ", np.mean(dados_com_outlier))
print("Mediana com outlier: ", np.median(dados_com_outlier))
