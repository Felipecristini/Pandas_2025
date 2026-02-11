# %%

import pandas as pd

clientes = pd.read_csv('../data/clientes.csv', sep=';')
clientes.head()

# %%
clientes.dropna(how='any')

# %%
df= pd.DataFrame(
    {
        "nome": ["Teo", None, "Nah", "Marcio"],
     "idade": [None, None, 43, 52],
     "salario": [3453, 4324,None, 5423]
     }
)

df.dropna(how="all", subset=["idade", "nome"])

# %%

df.fillna(0)

# %% 
medias = df[['idade', 'salario']].mean()
df.fillna(medias)