# %%

import pandas as pd

# %%
url = 'https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil'

dfs = pd.read_html(url)
uf = dfs[1]

# %%

def str_to_float(x:str):
    x = float(x.replace(' ', '')
              .replace(",",".")
              replace.('\xa0',''))
    return float(x)

# %%

uf["Área (km²)"] = uf["Área (km²)"].apply(str_to_float)
uf['População (Censo 2022)'] = uf['População (Censo 2022)'].apply(str_to_float)
uf['PIB (2015)'] = uf['PIB (2015)'].apply(str_to_float)
uf['PIB per capita (R$) (2015)'] = uf['PIB per capita (R$) (2015)'].apply(str_to_float)
uf.dtypes
