import string

def contar_letras(texto):
    texto_limpo = texto.lower().strip()
    for l in texto_limpo:
        if l in string.punctuation:
            texto_limpo = texto_limpo.replace(l, "")
    texto_separado = texto_limpo.split()
    contagem = {}
    for palavra in texto_separado:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return max(contagem, key=contagem.get)

from collections import Counter

def contar_palavras_pro(texto):
    # Cria uma tabela de tradução que mapeia pontuação para None
    tabela = str.maketrans('', '', string.punctuation)
    # Limpa, converte para minúsculo e separa
    palavras = texto.lower().translate(tabela).split()
    print(palavras)  # Para verificar o resultado da limpeza e separação
    # Conta tudo instantaneamente
    contagem = Counter(palavras)
    
    # Retorna a palavra mais comum (most_common retorna uma lista de tuplas)
    return contagem.most_common(1)[0][0]

if __name__ == "__main__":
    print(contar_letras("Python é legal, mas Java também é legal! Python ganha."))
    print(contar_palavras_pro("Python é legal, mas Java também é legal! Python ganha."))