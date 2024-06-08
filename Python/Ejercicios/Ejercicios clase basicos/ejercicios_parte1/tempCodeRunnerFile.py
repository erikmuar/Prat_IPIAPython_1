
  # %% 
  def num_min(lista:list):
   numero = lista[0]
   for i in lista:
    if numero < i:
      numero = i  
    print(numero)
      
  num_min([2,5,9,10,1])