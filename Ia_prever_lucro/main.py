import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import sqlite3
import random

conexao = sqlite3.connect("empresa.db")
df = pd.read_sql_query("SELECT * FROM vendas", conexao)
conexao.close()
df["lucro"] = df["valor"] * 0.25
df["desconto_aplicado"] = [random.uniform(0, 30) for _ in range(len(df))]

X = df[['valor', 'desconto_aplicado']]
y = df['lucro']

modelo = LinearRegression()
modelo.fit(X, y)

print(modelo.score(X, y))

if __name__ == "__main__":
    print("Modelo treinado com sucesso!")
    print("\n\nModelo pronto para prever o lucro de novas vendas.")
    valor = float(input("Digite o valor da venda: "))
    desconto = float(input("Digite o desconto aplicado: "))
    nova_venda = np.array([[valor, desconto]])
    previsao = modelo.predict(nova_venda)
    print(f"Predição de lucro: R${previsao[0]:.2f}")