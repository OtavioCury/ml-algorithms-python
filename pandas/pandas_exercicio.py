import pandas as pd
#carregando o dataset corretamente
data = pd.read_csv("datasets\GasPricesinBrazil_2004-2019.csv", sep=";")
print(data.head(10))
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