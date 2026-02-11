# %% 
import pandas as pd 

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")
df_clientes

# %%

# 5 primeiras linhas ou n linhas
df_clientes.head(n=10)

# %%

# ultimas 5 linhas ou n linhas
df_clientes.tail(10)

# %%

# amostra aleatoria
df_clientes.sample(10)

# %% 

# atributo para saber quant de linhas e colunas (L, C)
df_clientes.shape

# %%

# descobrir nome das colunas
df_clientes.columns

# %%

# descobrir os indices do dataframe
df_clientes.index

# %%

#  informações do dataframe + quant de RAM 
df_clientes.info(memory_usage='deep')

# %%

# retorna uma series com os tipos de valor de cada coluna
df_clientes.dtypes['idCliente']

# %%

#
df_clientes