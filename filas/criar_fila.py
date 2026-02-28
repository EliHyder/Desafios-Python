import pandas as pd
import os

# Criando uma pasta para os dados
os.makedirs("dados_filiais", exist_ok=True)

# Simulando arquivos de 3 filiais com "erros" propositais
data1 = {'item': ['Teclado', 'Mouse'], 'venda': [150, 80]}
data2 = {'produto': ['Monitor', 'Mouse'], 'faturamento': [900, None]} # Colunas diferentes e valor nulo
data3 = {'item': ['Teclado', 'Cadeira'], 'venda': [150, 1200]}

pd.DataFrame(data1).to_csv("dados_filiais/filial_A.csv", index=False)
pd.DataFrame(data2).to_csv("dados_filiais/filial_B.csv", index=False)
pd.DataFrame(data3).to_csv("dados_filiais/filial_C.csv", index=False)