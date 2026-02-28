from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

# 1. Preparando os Dados (X = Características, y = O que queremos prever)
# Imagine que X são as perguntas e y são as respostas da prova
df = pd.DataFrame({
    'valor': [100, 200, 300, 400, 500],
    'desconto_aplicado': [0, 5, 10, 15, 20],
    'lucro': [20, 35, 50, 60, 70]
})

X = df[['valor', 'desconto_aplicado']] 
y = df['lucro']

# 2. Criando o "Cérebro" (O Modelo)
modelo = LinearRegression()

# 3. Treinando (O computador estuda os dados)
modelo.fit(X, y)

# 4. Fazendo uma Predição
# "E se eu vender algo por R$ 500 com 10% de desconto, qual o lucro?"
nova_venda = np.array([[500, 10]])
previsao = modelo.predict(nova_venda)

print(f"Predição de lucro: R${previsao[0]:.2f}")