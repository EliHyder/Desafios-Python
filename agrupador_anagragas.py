def agrupador_anagramas(palavras):
    anagramas = {}
    for palavra in palavras:
        chave = "".join(sorted(palavra))
        if chave in anagramas:
            anagramas[chave].append(palavra)
        else:
            anagramas[chave] = [palavra]
    return list(anagramas.values())

from collections import defaultdict

def agrupador_anagramas_pro(palavras):
    # Define que toda nova chave terá uma lista [] por padrão
    grupos = defaultdict(list)
    
    for palavra in palavras:
        # Ordena a palavra para criar a chave única do grupo
        chave = "".join(sorted(palavra))
        grupos[chave].append(palavra)
        
    return list(grupos.values())

if __name__ == "__main__":
    palavras = ["amor", "roma", "mar", "ramo", "mora"]
    resultado = agrupador_anagramas(palavras)
    print("Anagramas agrupados:")
    for grupo in resultado:
        print(grupo)
    print("\nUsando a versão pro:")
    resultado_pro = agrupador_anagramas_pro(palavras)
    print("Anagramas agrupados:")
    for grupo in resultado_pro:
        print(grupo)
