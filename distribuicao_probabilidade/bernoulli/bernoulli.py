from scipy.stats import bernoulli
import seaborn as sns

dados = bernoulli.rvs(size=10000, p = 0.6)

ax = sns.distplot(dados, kde=False, color="skyblue", hist_kws={"linewidth": 15, "alpha": 1})
ax.set(xlabel="Distribuição Bernoulli", ylabel="Frequência")