#%%
# 7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.

def es_palindromo(word:str): 
    palabra = word[::-1]
    if word == palabra: 
        return True
    else: 
        return False
    
es_palindromo("radar")

assert es_palindromo("lool") == True
# %%
