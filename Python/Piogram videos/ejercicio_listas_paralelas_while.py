#Ejercicio 1 Tenemos dos listas,  la primera contiene el nombre de los productos y la segunda contiene los precios. La empresa requiere la siguientge informacion:


# a) El nombre de producto de menor precio.
# b) El precio del mouse.
# c) Presentar un  top 5 de productos en orden de mayor a menor segun su precio.

#A) Nombre del producto menor precio

productos = ["monitor", "mouse", "teclado","microfono","camara","audifonos"]
precios = [200, 15, 25, 5, 40,80]

minimo = min(precios) # 5

posicion = precios.index(minimo)

prod_min = productos[posicion]


print(prod_min)
    
    
# B) Precio del mouse

posicion_mouse = productos.index("mouse")

precio_mouse = precios[posicion_mouse]

print(precio_mouse)


# C) Presentar un  top 5 de productos en orden de mayor a menor segun su precio.


i = 0 

while i < 5: 
    maxi = max(precios)
    pos = precios.index(maxi)
    prod_max = productos[pos]
    print(prod_max, maxi)
    del productos[pos]
    del precios[pos]
    i+=1