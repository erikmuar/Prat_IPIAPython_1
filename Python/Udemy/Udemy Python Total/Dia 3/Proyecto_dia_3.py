texto = input("Ingresa un texto: ").lower()
letra1 = input("Ingresa la primera letra: ").lower()
letra2 = input("Ingresa la segunda letra: ").lower()
letra3 = input("Ingresa la tercera letra: ").lower()

lista = [letra1,letra2,letra3]

# Cuantas veces aparece cada letra

contad1 = texto.count(letra1)
contad2 = texto.count(letra2)
contad3 = texto.count(letra3)
print("\n")
print(f"Hemos encontrado la letra {letra1}, {texto.count(letra1)} veces.")
print("\n")
print(f"Hemos encontrado la letra {letra2}, {texto.count(letra2)} veces.")
print("\n")
print(f"Hemos encontrado la letra {letra3}, {texto.count(letra3)} veces.")
print("\n")
# Cuantas palabras hay en total

lista_palabras = texto.split()
largo = len(lista_palabras)

print(f"El texto tiene una longitud de {largo} palabras.")
print("\n")

# Primera y ultima letra

primera_letra = texto[0]
ultima_letra = texto[-1]

print(f"La primera letra es {primera_letra}, y la ultima es {ultima_letra}.")
print("\n")
# Palabras en orden inverso 

lista_palabras.reverse()

orden_inverso = " ".join(lista_palabras)

print(f"El orden inverso es '{orden_inverso}'.")

print("\n")
# Aparece python ? 

buscar_python = "python" in texto 

dic = {True:"si",False:"no"}

print(f"La palabra 'Python' {dic[buscar_python]} aparece en el texto.")