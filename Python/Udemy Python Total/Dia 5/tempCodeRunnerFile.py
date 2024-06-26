def cafe_mas_caro(precios_cafe):
    max_precio = 0
    cafe_mas_caro = ""
    
    for cafe,precio in precios_cafe:
        
        if precio > max_precio:
            max_precio = precio
            cafe_mas_caro = cafe
        else:
            pass
            
    return max_precio, cafe_mas_caro

print(cafe_mas_caro([("Capuccino",1.5),("Moccha",1.9),("Espresso",1.6)]))