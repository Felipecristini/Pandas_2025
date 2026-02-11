# %%

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 22, 36, 33,
]

media = sum(idades) / len(idades)
print('media:', media)

diffs = 0 
for i in idades: 
    diffs += (i - media) ** 2

variancia = diffs / (len(idades)-1)

print('Variancia:', variancia)

# %%
#importação do pandas
import pandas as pd

#dados/lista
idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 22, 36, 33,
]

#criação das series
series_idades = pd.Series(idades)
series_idades

# %%

#Estatísticas
media_idades = series_idades.mean()
var_idades = series_idades.var()
var_idades
summary_idade = series_idades.describe()
summary_idade