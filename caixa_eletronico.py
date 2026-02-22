def caixa_eletronico(valor: int) -> dict:
    if valor <= 0:
        raise ValueError("O valor deve ser um número inteiro positivo.")
    notas = [100, 50, 20, 10, 5, 2]
    
    resultado = {}
    for nota in notas:
        quantidade = valor // nota
        if quantidade > 0:
            resultado[nota] = quantidade
            valor -= quantidade * nota
    return resultado

def caixa_eletronico_pro(valor):
    notas = [100, 50, 20, 10, 5, 2]
    resultado = {}
    
    for nota in notas:
        # divmod retorna (quociente, resto) de uma só vez
        quantidade, valor = divmod(valor, nota)
        if quantidade > 0:
            resultado[nota] = quantidade
            
    return resultado

if __name__ == "__main__":
    valor = 187
    resultado = caixa_eletronico(valor)
    print(f"Valor solicitado: R${valor}")
    print("Notas fornecidas:")
    for nota, quantidade in resultado.items():
        print(f"{quantidade} nota(s) de R${nota}")
    print("\nUsando a versão pro:")
    resultado_pro = caixa_eletronico_pro(valor)
    print(f"Valor solicitado: R${valor}")
    print("Notas fornecidas:")
    for nota, quantidade in resultado_pro.items():
        print(f"{quantidade} nota(s) de R${nota}")