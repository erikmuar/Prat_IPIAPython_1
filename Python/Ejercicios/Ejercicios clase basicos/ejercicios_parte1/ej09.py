# 9 - Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
#%% 
def generar_n_caracteres(n:int, letra:str):
    concat = " "
    for i in range(n): 
        concat += letra 
    print(concat)
    
generar_n_caracteres(7,"h")
# %% Forma facil

def generar_n_caracteres(n: int, letra: str):
    concat = letra * n
    print(concat)
    
generar_n_caracteres(7, "h")

# %%
