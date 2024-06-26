# Si tenemos una lista compuesta por tuplas, para acceder a ella con un bucle for ponemos for parametro1, parametro2 in lista_tuplas      
# Haciendo esto al printear el parametro 1 sale solo el primer elemento de cada tupla y poniendo solo el segundo sale el segundo elemento 

precios_cafe = [("Capuccino",1.5),("Moccha",1.9),("Espresso",1.6)]


    
def cafe_mas_caro(precios_cafe):
    max_precio = 0
    cafe_mas_caro = ""
    
    for cafe,precio in precios_cafe:
        
        if precio > max_precio:
            max_precio = precio
            cafe_mas_caro = cafe
        else:
            pass
            
    return cafe_mas_caro, max_precio

print(cafe_mas_caro([("Capuccino",1.5),("Moccha",1.9),("Espresso",1.6)]))