# %%
import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39,
]

series_idades = pd.Series(idades)
series_idades

# %%
idades[0]
series_idades[0]
# %%
series_idades[-1]

# %%
series_idades = series_idades.sort_values()
series_idades

# %%
series_idades[0]

# %% 
series_idades.iloc[0]

# %%
series_idades.iloc[-1]

# %%
series_idades.iloc[:3]

# %%
idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39,
]

nomes = [
    'Teo', 'Maria', 'Jose', 'Luis', 'Ana',
    'Nah', 'Dani', 'Mah', 'Fe', 'Nanda',
    'Naty', 'Nih', 'Pedro', 'Kosato', 'Kosato',
]

series_idades = pd.Series(idades, index=nomes)
series_idades

# %%
series_idades['Kosato']

# %%
series_idades.iloc[-1]