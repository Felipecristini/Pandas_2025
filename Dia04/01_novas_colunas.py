# %%
import pandas as pd
import numpy as np

df = pd.read_csv('../data/clientes.csv', sep=';')
df.head()

# %%

df['Pontos_100'] = df['qtdePontos'] + 100

# %% 

df['EmailTwitch'] = df['flEmail'] + df['flTwitch']
df.head()

# %%

df['flEmail'] * df['flTwitch']

# %%

df['QtdeSocial'] = df['flEmail'] + df['flTwitch']	+ df['flYouTube'] + df['flBlueSky']	+ df['flInstagram']	
df

# %%

df['TodasSocial'] = df['flEmail'] * df['flTwitch'] * df['flYouTube'] * df['flBlueSky'] * df['flInstagram']	
df

# %%

df['qtdePontos'].describe()

# %%

df['Log_Pontos'] = np.log(df['qtdePontos']+1)
df['Log_Pontos'].describe()

# %% 
import matplotlib.pyplot as plt

plt.hist(df['Log_Pontos'])
plt.grid()
plt.show()