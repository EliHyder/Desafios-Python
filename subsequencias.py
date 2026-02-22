from functools import lru_cache

@lru_cache(None)
def subsequencias(str1, str2):
    if not str1 or not str2:
        return 0
    if str1[-1] == str2[-1]:
        return 1 +subsequencias(str1[:-1], str2[:-1])
    else:
        return max(subsequencias(str1[:-1], str2), subsequencias(str1, str2[:-1]))

def lcs_pro(s1, s2):
    @lru_cache(None)
    def buscar(i, j):
        # i e j representam a posição atual nas strings
        if i < 0 or j < 0:
            return 0
        
        if s1[i] == s2[j]:
            return 1 + buscar(i - 1, j - 1)
        else:
            return max(buscar(i - 1, j), buscar(i, j - 1))

    # Começamos do fim (último índice) para o começo
    return buscar(len(s1) - 1, len(s2) - 1)
    
if __name__ == "__main__":
    str1 = "abcdeasdaofjoasfjoidsjfoiweciondnfeiojrfioewjfsdjfnsdojfiowesoadkasodjsaoifjaoijfaasadfhdsfhsdfhahwhsoiwiodsiofhuieugdjaodawiodoiwofsjbbdbsbsssaafdsgfdcwfasfeahsedegfasdfasdasdfasdfsdfasdasdfasdfsdfasdfsdfasdfsdfasdfsdfasdfsdfasdfsdfasdfasdfsdfasdfsdfasdfsdfasdfsdfasdfsdfasdfsdfasdfasdfsdfasdfsdfasdfsdfasdfsdfasdfsdfasdfsdfasassabcdeasdaofjoasfjoidsjfoiweciondnfeiojrfioewjfsdjfnsdojfiowesoadkasodjsaoifjaoijfaasadfhdsfhsdfhahwhsoiwiodsiofhuieugdjaodawiodoiwofsjbbdbsbsssaafdsgfdcwfasfeahsedegfasdfasdasdfasdfsdfasdasdfasdfsdfasdfsdfasdfsdfasdfsdfasdfsdfasdfsdfasdfasdfsdfasdfsdfasdfsdfasdfsdfasdfsdfasdfsdfasdfasdfsdfasdfsdfasdfsdfasdfsdfasdfsdfasdfsdfasassagfasfsdfasdfsdfasdfsdfasassagfasfsfsfsffsdfasassagfasfsdfasdfsdfasdfsdfasassagfasfsfsfsf"
    str2 = "acesadfdhsfhahhwhsoiwiodsiofhuieugdjaodawiodoiwofsjbbdbsbsssaafdsgfdcwfasfeahsedegfgasdfasdasdfasdfsdfasdasdfasdfsdfasdfsdfasdfsdfasdfsdfasdfsdfasdfasdfsdfasdfsdfasdfsdfasdfsdfasdfsdfasdfsdfasdfasdfsdfasdfsdfasdfsdfasdfsdfasdfsdfasassgdsadfasdfsdfasdfsdfasdfsdfasdfsdfasdfsdfasdfsdfasdfsdfasdfsdfasdfsdfasdfasdfsdfasdfsdfasdfsdfasdfsdfasdfsdfasdfsdfasdfasdfsdfasdfsdfasdfsdfasdfsdfasdfsdfasasssadfsa"
    resultado = subsequencias(str1, str2)
    print(f"Número de subsequências de '{str1}' que formam '{str2}': {resultado}")
    print("\nUsando a versão pro:")
    resultado_pro = lcs_pro(str1, str2)
    print(f"Número de subsequências de '{str1}' que formam '{str2}': {resultado_pro}")