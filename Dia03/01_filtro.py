# %%
import pandas as pd

df = pd.read_csv('../data/transacoes.csv', sep=';')
df.head()

# %%

pontos = [10, 1, 1, 1, 50, 100, 130, 30, 25, 50]
filtro = []

valores_50_mais = []
for i in pontos:
    filtro.append(i>= 50):

resultado = []
for i in range(len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i])
        
resultado

# %%

brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "nah", "mah"],
        "idade": [32,35,14],
        "uf": ["sp","pr","rj"],
    }
)

#gera uma serie com True e False
filtro = brinquedo["idade"] >= 18

# Aplica o filtro retornando apenas os True
brinquedo[filtro]

