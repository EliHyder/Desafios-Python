import sqlite3
import pandas as pd

class Venda:
    def __init__(self, produto, categoria, valor):
        self.produto = produto
        self.categoria = categoria
        self.valor = valor

def save_venda(venda):
    conexao = sqlite3.connect("empresa.db")
    cursor = conexao.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vendas (
            produto TEXT,
            categoria TEXT,
            valor REAL
        )
    ''')
    
    cursor.execute("INSERT INTO vendas (produto, categoria, valor) VALUES (?, ?, ?)", 
                   (venda.produto, venda.categoria, venda.valor))
    conexao.commit()
    conexao.close()

def gerar_relatorio():
    conexao = sqlite3.connect("empresa.db")
    df = pd.read_sql_query("SELECT * FROM vendas", conexao)
    conexao.close()
    
    soma_total = df['valor'].sum()
    print(f"Faturamento total: R${soma_total:.2f}")
    media_valor_categoria = df.groupby('categoria')['valor'].mean()
    print("Média de valor por categoria:")
    print(media_valor_categoria)

def top_produtos():
    conexao = sqlite3.connect("empresa.db")
    df = pd.read_sql_query("SELECT * FROM vendas", conexao)
    conexao.close()

    top_produtos = df[df['valor'] > df['valor'].mean()]
    print("Top produtos:")
    print(top_produtos)

def save_electronicos():
    conexao = sqlite3.connect("empresa.db")
    df = pd.read_sql_query("SELECT * FROM vendas WHERE categoria = 'Eletrônicos'", conexao)
    conexao.close()
    df.to_csv("eletronicos.csv", index=False)

import matplotlib.pyplot as plt
def grafico_vendas():
    conexao = sqlite3.connect("empresa.db")
    df = pd.read_sql_query("SELECT * FROM vendas", conexao)
    conexao.close()
    media_valor_categoria = df.groupby('categoria')['valor'].mean()
    media_valor_categoria.plot(kind='bar')
    plt.title("Média de Valor por Categoria")
    plt.show()

def limpar_e_analisar():
    conexao = sqlite3.connect("empresa.db")
    df = pd.read_sql_query("SELECT * FROM vendas", conexao)
    conexao.close()
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    df["lucro"] = df["valor"] * 0.25
    produto_maior_lucro = df.loc[df["lucro"].idxmax()]
    print("produto com maior lucro:")
    print(produto_maior_lucro)

if __name__ == "__main__":
    venda1 = Venda("Notebook", "Eletrônicos", 3500.00)
    venda2 = Venda("Cadeira", "Móveis", 450.00)
    
    save_venda(venda1)
    save_venda(venda2)
    
    gerar_relatorio()
    top_produtos()
    save_electronicos()
    grafico_vendas()