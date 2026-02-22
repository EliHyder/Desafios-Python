def labirinto_recursivo(m, n):
    if m == 1 and n == 1:
        return 1
    if m < 1 or n < 1:
        return 0
    return labirinto_recursivo(m - 1, n) + labirinto_recursivo(m, n - 1)

from functools import lru_cache

# O lru_cache faz o memoization automaticamente para você!
@lru_cache(None)
def caminhos_unicos_pro(m, n):
    if m == 1 or n == 1:
        return 1
    return caminhos_unicos_pro(m - 1, n) + caminhos_unicos_pro(m, n - 1)

import math
def caminhos_unicos_matematico(m, n):
    return math.factorial(n + m - 2) / (math.factorial(m - 1) * math.factorial(n - 1))

if __name__ == "__main__":
    m = 20
    n = 20
    # resultado = labirinto_recursivo(m, n)
    # print(f"Número de caminhos para um labirinto {m}x{n}: {resultado}")
    print("\nUsando a versão pro com memoization:")
    resultado_pro = caminhos_unicos_pro(m, n)
    print(f"Número de caminhos para um labirinto {m}x{n}: {resultado_pro}")
    print("\nUsando a versão matemática:")
    resultado_mat = caminhos_unicos_matematico(m, n)
    print(f"Número de caminhos para um labirinto {m}x{n}: {resultado_mat}")