# %%
import pandas as pd
# %%

clientes = pd.read_csv('../data/clientes.csv', sep=';')
clientes.head()

# %%

clientes['qtdePontos'].sort_values()

# %%

clientes.sort_values(by = 'qtdePontos', ascending=False).head(5)