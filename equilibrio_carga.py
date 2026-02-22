from functools import lru_cache

def equilibrar_carga(cargas):
    if not cargas:
        return 0
    
    total_carga = sum(cargas)
    @lru_cache(None)
    def buscar_melhor_soma(i, soma_atual):
        if i == len(cargas):
            return abs(total_carga - 2 * soma_atual)
        # Incluir a carga atual
        incluir = buscar_melhor_soma(i + 1, soma_atual + cargas[i])
        pular = buscar_melhor_soma(i + 1, soma_atual)
        return min(incluir, pular)

    return buscar_melhor_soma(0, 0)

if __name__ == "__main__":
    cargas = [10, 20, 15, 5, 25]
    resultado = equilibrar_carga(cargas)
    print(f"Diferencia de carga: {resultado}")