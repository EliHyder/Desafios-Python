def inverso_matriz(matriz):
    if len(matriz) != len(matriz[0]):
        raise ValueError("A matriz deve ser quadrada para calcular o inverso.")
    n = len(matriz)
    new_matriz = []
    for i in range(n):
        new_matriz.append([])
        for j in range(n):
            new_matriz[i].append(matriz[j][i])
    return new_matriz

def transposta_pro(matriz):

    print([list(coluna) for coluna in zip(*matriz)])# Para verificar o resultado do zip(*matriz)

    # O zip(*) descompacta as linhas e as agrupa por coluna
    return [list(coluna) for coluna in zip(*matriz)]

if __name__ == "__main__":
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    inversa = inverso_matriz(matriz)
    for linha in inversa:
        print(linha)
    print("Transposta:")
    transposta = transposta_pro(matriz)
    for linha in transposta:
        print(linha)