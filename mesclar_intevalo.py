def mesclar_intervalo(intervalos):
    if not intervalos:
        return []

    # Ordenar os intervalos pelo início
    intervalos.sort(key=lambda x:  x[0])
    print(f"Intervalos ordenados: {intervalos}")  # Para verificar a ordenação
    mesclados = [intervalos[0]]
    for i in range(len(intervalos)):
        atual = intervalos[i]
        ultimo_mesclado = mesclados[-1]
        if atual[0] <= ultimo_mesclado[1]:  # Se houver sobreposição
            # Atualizar o intervalo mesclado com o maior fim
            ultimo_mesclado[1] = max(ultimo_mesclado[1], atual[1])
        else:
            mesclados.append(atual)

    return mesclados

def mesclar_intervalo_pro(intervalos):
    if not intervalos:
        return []

    # sorted() não altera a lista original
    # Usamos fatiamento [1:] para pular o primeiro que já está em 'mesclados'
    ordenados = sorted(intervalos, key=lambda x: x[0])
    mesclados = [ordenados[0]]

    for atual in ordenados[1:]:
        ultimo = mesclados[-1]
        
        # Se o início do atual for menor ou igual ao fim do último mesclado
        if atual[0] <= ultimo[1]:
            ultimo[1] = max(ultimo[1], atual[1])
        else:
            mesclados.append(atual)

    return mesclados

if __name__ == "__main__":
    intervalos = [[2, 6], [1, 3], [8, 10], [15, 18]]
    resultado = mesclar_intervalo(intervalos)
    print(f"Resultado: {resultado}")
    print("\nUsando a versão pro:")
    resultado_pro = mesclar_intervalo_pro(intervalos)
    print(f"Resultado: {resultado_pro}")