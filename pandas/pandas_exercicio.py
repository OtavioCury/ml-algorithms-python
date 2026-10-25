import pandas as pd
#carregando o dataset corretamente
data = pd.read_csv("/home/otavio/ml-algorithms-python/pandas/datasets/GasPricesinBrazil_2004-2019.csv", sep=";")
print(data.head(10))
#Imprimindo informações sobre o dataset
print(data.info())
print(type(data))
print(data.shape)
print(f"O DataFrame possui {data.shape[0]} linhas e {data.shape[1]} colunas.")
'''
vendas_df = pd.DataFrame({
    "id": [1,2,3,4,5],
    "data": ["2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04", "2026-01-05"],
    "valor": [100, 200, 130, 90, 150],
    "nome_vendedor": ["João", "Maria", "Pedro", "Ana", "Lucas"]
})

print(vendas_df)

vendas_df = vendas_df.rename(columns={
    "valor": "Valor da Venda",
    "data": "Data da Venda"
})

print(vendas_df)
'''
#Selecionando uma coluna específica
regiao = data["REGIÃO"]
print(regiao)
print(data.ANO)

#Criar uma series no pandas
serie = pd.Series([1,2,"Nome", "Rua", 3.13])
print(serie)

serie_indices_texto = pd.Series([2.4,5.2,10], index=["Ana", "João", "Maria"], name="Notas")
print(serie_indices_texto)

data_inicial = data["DATA INICIAL"]
print(data_inicial)

produto_copy_bkp = data["PRODUTO"].copy()

#Atribuir uma constante à todas as linhas de uma coluna
data["PRODUTO"] = "Combustível"
print(data["PRODUTO"])

nlinhas, ncolunas = data.shape
print(nlinhas, ncolunas)

#Criando linhas a partir de list comprehension
novos_produtos = [f"Produto {i}" for i in range(nlinhas)]

#A quantidade de elementos da lista 'novos_produtos' é igual ao número de linhas do dataframe
data["PRODUTO"] = novos_produtos

print(data["PRODUTO"])

data["PRODUTO"] = produto_copy_bkp
print(data["PRODUTO"])

#Criando uma coluna a partir de um valor constante
data["COLUNA VALOR FIXO"] = "DEFAULT"
print(data["COLUNA VALOR FIXO"])

#Criando uma coluna a partir de uma lista
data["COLUNA A PARTIR DE LISTA"] = range(data.shape[0])
print(data["COLUNA A PARTIR DE LISTA"])

#Criando uma coluna calculada
data["PREÇO MÉDIO REVENDA (dólares)"] = data["PREÇO MÉDIO REVENDA"] * 6.0
print(data["PREÇO MÉDIO REVENDA (dólares)"])

#Acessando os índices do dataset
indices_lista = data.index.to_list()
print(indices_lista)

pesquisa_de_satisfacao = pd.DataFrame({
    "bom": [50, 21, 100],
    "ruim": [131, 2, 30],
    "pessimo": [30, 20, 1]
}, index = ["XboxOne", "Playstation3", "Switch"])

print(pesquisa_de_satisfacao)
print(pesquisa_de_satisfacao.index)

#Selecionando apenas uma linha
segunda_linha = data.iloc[1]
print(segunda_linha)

#Selecionando múltiplas linhas
seis_linhas = data.iloc[:6]
print(seis_linhas)

#Selecionando múltiplas linhas específicas
linhas_especificas = data.iloc[[1,5,10,20]]
print(linhas_especificas)

#Retorna a linha de índice 0
primeira_linha = pesquisa_de_satisfacao.iloc[0]
print(primeira_linha)

#Retorna a linha de índice 0 e coluna de índice 2
primeira_linha_terceira_coluna = pesquisa_de_satisfacao.iloc[0,2]
print("Primeira linha, terceira coluna:", primeira_linha_terceira_coluna)

#Selecionando por label
print("Linha 'XboxOne': ",pesquisa_de_satisfacao.loc["XboxOne"])

#Selecionando por label linha e coluna
linha_coluna = pesquisa_de_satisfacao.loc["XboxOne", "bom"]
print("Linha 'XboxOne', coluna 'bom': ", linha_coluna)

#Fatiamento por label
fatiamento = pesquisa_de_satisfacao.loc[:, ["bom", "ruim"]]
print("Fatiamento por label (todas as linhas, colunas 'bom' e 'ruim'):\n", fatiamento)

#Selecionando colunas
coluna_estado = data["ESTADO"]
print("Coluna 'ESTADO': ", coluna_estado)

#Selecionando mais de uma coluna
várias_colunas = data[["ESTADO", "REGIÃO", "PRODUTO"]]
print("Várias colunas:\n", várias_colunas)

#Removendo colunas
print(list(data.columns))
del data["Unnamed: 0"]
del data["COLUNA A PARTIR DE LISTA"]
del data["PREÇO MÉDIO REVENDA (dólares)"]
print("Colunas após remoção:\n", list(data.columns))

data.to_csv("/home/otavio/ml-algorithms-python/pandas/datasets/GasPricesinBrazil_2004-2019_modificado.csv", index=False)

#Mostra todos os estado sem repetição
print("Estados do dataset: ",data["ESTADO"].unique())

#Mostra todos os anos sem repetição
print("Anos do dataset: ", data["ANO"].unique())

#Filtrando apenas as linhas do estado de São Paulo
sp_data = data[data["ESTADO"] == "SAO PAULO"]
print("Dados do estado de São Paulo:\n", sp_data.head())

#Filtrando apenas as linhas do estado de São Paulo do ano de 2010
sp_2010_data = data[(data["ESTADO"] == "SAO PAULO") & (data["ANO"] == 2010)]
print("Dados do estado de São Paulo:\n", sp_2010_data.head())

#Selecionando registros do Rio de Janeiro com preços acima de 2 reais
rj_preco_acima_2 = data[(data["ESTADO"] == "RIO DE JANEIRO") 
                        & (data["PREÇO MÉDIO REVENDA"] >= 2)]
print("Dados do Rio de Janeiro com preços acima de 2 reais: ", rj_preco_acima_2.head())

#Selecionando registros de postos de São Paulo ou do 
# Rio de Janeiro com gasolina comum acima de 2 reais
selecao_sp = data["ESTADO"] == "SAO PAULO"
selecao_rj = data["ESTADO"] == "RIO DE JANEIRO"
selecao_gasolina_comum = data["PRODUTO"] == "GASOLINA COMUM"
selecao_acima_2 = data["PREÇO MÉDIO REVENDA"] >= 2
dados_filtrados = data[(selecao_sp | selecao_rj) & selecao_gasolina_comum & selecao_acima_2]
print("Dados de postos de São Paulo ou do Rio de Janeiro com gasolina comum acima de 2 reais: ", dados_filtrados.head())

#Selecionando registros do anos de 2008, 2010, 2012
lista_anos = [2008, 2010, 2012]
selecao_anos = data["ANO"].isin(lista_anos)
print("Dados do anos de 2008, 2010, 2012: ", data[selecao_anos].head())

#Selecionando registros do anos de 2008, 2010, 2012 usando query
print("Dados do anos de 2008, 2010, 2012 usando query: ", data.query("ANO in @lista_anos").head())

#Fazendo limpeza nos dados
data_pre = data.copy()
data_pre["DATA INICIAL"] = pd.to_datetime(data_pre["DATA INICIAL"])
data_pre["DATA FINAL"] = pd.to_datetime(data_pre["DATA FINAL"])
print("Informações do banco: ", data_pre.info())

# convertendo atributos/colunas para 'numeric'
for atributo in ['MARGEM MÉDIA REVENDA', 'PREÇO MÉDIO DISTRIBUIÇÃO', 'DESVIO PADRÃO DISTRIBUIÇÃO', 
                 'PREÇO MÍNIMO DISTRIBUIÇÃO', 'PREÇO MÁXIMO DISTRIBUIÇÃO', 'COEF DE VARIAÇÃO DISTRIBUIÇÃO']:
    data_pre[atributo] = pd.to_numeric(data_pre[atributo], errors="coerce")

data_pre.info()