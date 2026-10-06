from scipy.stats import binom
import seaborn as sns

dados_binom = binom.rvs(n=10, p = 0.8, size = 10000)

ax = sns.distplot(dados_binom,
                  kde=False,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Distribuição Binomial', ylabel='Frequência')