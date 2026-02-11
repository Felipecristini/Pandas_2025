# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=';')
df

# %%
df.shape

# %%
df.info(memory_usage='deep')

# %%
df.dtypes

# %%

#renomear colunas

renamed_columns = {'QtdePontos': "qtPontos",
                        "DescSistemaOrigem": 'SistemaOrigem'
                        }
df.rename(columns= renamed_columns, inplace=True)

# %%
# SELECT * FROM df
df

# %%

# selecionar as colunas mostradas
#SELECT IdCliente FROM df
df[['IdCliente', 'qtPontos']]

# %%

# SELECT IdCliente, qtPontos FROM df LIMITS 5
df[['IdCliente', 'qtPontos']].tail(5)

# %%
 
 # SELECT IdClinte,IdTransacao, qtPontos FROM df LIMIT 5
df[['IdCliente','IdTransacao','qtPontos']].head(5)

# %%

#ordenar a ordem das colunas
colunas = df.columns.to_list()
colunas.sort()
colunas

df = df[colunas]
df
