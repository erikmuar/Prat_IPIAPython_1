def superposicion(lista1: list, lista2:list):
    for i in lista1: 
        x = lista1[i]
        if x in lista2:
            return True
        else: 
            return False
    

superposicion([1,5,8,22,90],[2,7,5,40,61])