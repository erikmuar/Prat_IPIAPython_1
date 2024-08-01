#Crea una función llamada devolver_distintos() que reciba 3integers como parámetros. 
# Si la suma de los 3 numeros es mayor a 15, va a devolver elnúmero mayor.
# Si la suma de los 3 numeros es menor a 10, va a devolver elnúmero menor.
# Si la suma de los 3 números es un valor entre 10 y 15(incluidos) va a devolver el número de valor intermedio.


def devolver_distintos(num1,num2,num3):
    
    lista = [num1,num2,num3]
    suma = sum(lista)
    
    if suma > 15:
        maximo = max(lista)
        return print(maximo)

    if suma < 10:
        minimo =  min(lista)
        return print(minimo)
    
    if 10 <= suma <= 15:
        lista.sort()
        return print(lista[1])
    
    
    
devolver_distintos(5,3,6)