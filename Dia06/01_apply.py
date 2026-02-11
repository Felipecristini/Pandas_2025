# %%

import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')
df.head()

# %%

def get_last_id (id):
    return id.split('-')[-1]

df['idCliente'].apply(get_last_id)