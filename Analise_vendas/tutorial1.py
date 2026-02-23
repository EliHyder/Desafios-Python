import sqlite3

# 1. Conecta ao banco (se não existir, ele cria o arquivo voador.db)
conexao = sqlite3.connect("sistema_vendas.db")
cursor = conexao.cursor()

# 2. Cria uma tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto TEXT,
        quantidade INTEGER,
        preco_unitario REAL
    )
''')

# 3. Insere dados
def salvar_venda(produto, qtd, preco):
    cursor.execute("INSERT INTO vendas (produto, quantidade, preco_unitario) VALUES (?, ?, ?)", 
                   (produto, qtd, preco))
    conexao.commit()

import pandas as pd

# 4. Transforma a tabela SQL diretamente em um DataFrame do Pandas
def gerar_analise():
    df = pd.read_sql_query("SELECT * FROM vendas", conexao)
    
    # Criando uma nova coluna de cálculo
    df['faturamento_total'] = df['quantidade'] * df['preco_unitario']
    
    # Salvando em CSV
    df.to_csv("relatorio_vendas.csv", index=False)
    
    return df