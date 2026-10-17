import numpy as np
from scipy import stats

np.random.seed(42)
n = 1000

dados = np.random.normal(loc=50, scale=10, size=n)

# Amplitude: diferença entre o maior e o menor valor
amplitude = np.ptp(dados)

# Variância: média dos quadrados dos desvios em relação à média
# ddof=0 -> populacional (divide por n), ddof=1 -> amostral (divide por n-1)
variancia_populacional = np.var(dados, ddof=0)
variancia_amostral = np.var(dados, ddof=1)

# Desvio padrão: raiz quadrada da variância, na mesma unidade dos dados
desvio_padrao_populacional = np.std(dados, ddof=0)
desvio_padrao_amostral = np.std(dados, ddof=1)

# Coeficiente de variação: desvio padrão relativo à média (adimensional)
coeficiente_variacao = stats.variation(dados, ddof=1)

# Quartis e intervalo interquartil (IQR): dispersão dos 50% centrais dos dados
q1, q2, q3 = np.percentile(dados, [25, 50, 75])
iqr = stats.iqr(dados)

# Desvio absoluto médio: média das distâncias absolutas em relação à média
desvio_absoluto_medio = np.mean(np.abs(dados - np.mean(dados)))

# Desvio absoluto mediano (MAD): mediana das distâncias absolutas em relação à mediana (robusto a outliers)
mad = stats.median_abs_deviation(dados)

# Erro padrão da média: desvio padrão da média amostral
erro_padrao = stats.sem(dados)

print("Amplitude: ", amplitude)
print("Variância populacional: ", variancia_populacional)
print("Variância amostral: ", variancia_amostral)
print("Desvio padrão populacional: ", desvio_padrao_populacional)
print("Desvio padrão amostral: ", desvio_padrao_amostral)
print("Coeficiente de variação: ", coeficiente_variacao)
print("Q1: ", q1, "| Q2: ", q2, "| Q3: ", q3)
print("Intervalo interquartil (IQR): ", iqr)
print("Desvio absoluto médio: ", desvio_absoluto_medio)
print("Desvio absoluto mediano (MAD): ", mad)
print("Erro padrão da média: ", erro_padrao)

# Resumo descritivo com scipy
print("\nResumo (scipy.stats.describe):")
print(stats.describe(dados))

# Efeito de um outlier: desvio padrão e amplitude são sensíveis, IQR e MAD são robustos
dados_com_outlier = np.append(dados, 500)
print("\nDesvio padrão com outlier: ", np.std(dados_com_outlier, ddof=1))
print("Amplitude com outlier: ", np.ptp(dados_com_outlier))
print("IQR com outlier: ", stats.iqr(dados_com_outlier))
print("MAD com outlier: ", stats.median_abs_deviation(dados_com_outlier))
