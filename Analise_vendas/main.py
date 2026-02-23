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

if __name__ == "__main__":
    venda1 = Venda("Notebook", "Eletrônicos", 3500.00)
    venda2 = Venda("Cadeira", "Móveis", 450.00)
    
    save_venda(venda1)
    save_venda(venda2)
    
    gerar_relatorio()