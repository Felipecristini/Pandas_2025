# %%
import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep = ';')
df

# %%

# coverte o tipo do dado
df['qtdePontos'].astype(float)

# %%

df.to_datetime(df['DtCriacao'])

# %%

# substitui um por outro
# nesse caso corrige datas invalidas
df['DtCriacao'] = df['DtCriacao'].replace({
    '0000-00-00 00:00:00.000': '2024-02-01 09:00:00.000',
     '2024-02-01 00:00:00.000': '2024-02-01 09:37:00.000' })

# %%

pd.to_datetime(df['DtCriacao'])

# %% 

replace = {'0000-00-00 00:00:00.000': '2024-02-01 09:00:00.000',
     '2024-02-01 00:00:00.000': '2024-02-01 09:37:00.000' }

df['DtCriacao'] = pd.to_datetime(df['DtCriacao'].replace(replace))

# %%

df['DtCriacao'].dt.year
