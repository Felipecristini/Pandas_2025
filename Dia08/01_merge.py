# %%
import pandas as pd

transacoes = pd.read_csv('../data/transacoes.csv', sep=';')
transacoes.head()

# %%
clientes = pd.read_csv('../data/clientes.csv', sep=';')
clientes.head()

# %%
transacoes.merge(
                right=clientes, 
                how='left',
                left_on=['IdCliente'],
                right_on=['idCliente'] 
                suffixes=['Transacao', 'Clientes']
                )
# %%

df_1 = pd.DataFrame({
    'transacao': [1,2,3,4,5],
    'nome': ['t1','t2','t3','t4','t5'],
    'idcliente': [1,2,3,2,2],
    'valor': [10,45,32,17,87],
})

df_2 = pd.DataFrame({
    'id': [1,2,3,4],
    'nome': ['teo','nah', 'mah', 'jose'],
})

df_1.merge(
    df_2, 
    left_on=['idcliente'],
      right_on=['id'], 
      how='left',
      suffixes=['Trasacao', 'Cliente']
      )

# %%

produtos = produtos[produtos["descProduto"]=="Presença Streak"]

(transacoes.merge(transacao_produto, on=["idTransacao"], how="left")
           .merge(produtos, on=["idProduto"], how="inner")
           .groupby(by="idCliente")["idTransacao"]
           .count()
           .sort_values(ascending=False)
           .head(1)
)