# %%
import pandas as pd

df = pd.DataFrame({
    'cliente': [1,2,3,4,5],
    'nome': ['teo','jose','nah','mah','lah'],
})

df_02 = pd.DataFrame({
    'cliente': [6,7,8],
    'nome': ['kosato','laura','dan'],
    'idade': [32,29,31],
})

df_03 = pd.DataFrame({
    'idade': [32,34,19,54,33]
})

# %%

dfs = [df , df_02]

pd.concat(dfs, ignore_index=True)

# %%

df_03 = df_03.sort_values(by='idade').reset_index(drop=True)
df_03

# %%
pd.concat([df, df_03], axis= 1)

# %%

pd.concat([df, df_02, df_03], axis=1)

# %%

import pandas as pd

df_geral = pd.DataFrame({
    'cod':[53,11,12,13,14],
    'nome': ['DF','RO','AC','AM','RR'],
    'periodo': [1989,1989,1989,1989,1989],
    'homicidios': [331,490,95,321,113],
})

df_negros = pd.DataFrame({
    'cod':[12,17,35,28,42],
    'nome': ['AC','TO','SP','SE','SC'],
    'periodo': [1996,1996,1996,1996,1996],
    'homicidios-negros': [56,130,359,785,33],
})

df_geral = df_geral.set_index(['nome', 'periodo'])
df_geral= df_geral.drop(['cod'],axis=1)
df_negros = df_negros.set_index(['nome', 'periodo'])
df_negros = df_negros.drop(['cod'],axis=1)

pd.concat([df_geral, df_negros], axis=1)