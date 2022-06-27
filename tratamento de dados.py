import pandas as pd

# Lendo os arquivos CVS
vendas_df = pd.read_csv('Contoso - Vendas  - 2017.csv', sep=';')
produtos_df = pd.read_csv('Contoso - Cadastro Produtos (1).csv', sep=';')
clientes_df = pd.read_csv('Contoso - Clientes.csv', sep=';')
lojas_df = pd.read_csv('Contoso - Lojas.csv', sep=';')


# Excluindo colunas (axis = 1)
clientes_df = clientes_df.drop(['Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10'], axis=1)


# Escolhendo colunas
clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]


# Mesclando Dataframe
vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente')


# Renomeando colunas
vendas_df = vendas_df.rename(columns={'E-mail': 'E-mail do Cliente'})




# Mostrando
print(vendas_df)
print('\n')
print('-=' * 50)
print('\n')
print(produtos_df)
print('\n')
print('-=' * 50)
print('\n')
print(clientes_df)
print('\n')
print('-=' * 50)
print('\n')
print(lojas_df)