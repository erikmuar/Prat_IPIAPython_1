class Pajaro: 
    alas = True # Atributo de clase
    
    def __init__(self,color,especie):
        self.color= color #Atributo de instancia
        self.especie = especie # Atributo de instancia
    
    def piar(self): #SIEMPRE hay que poner el parametro self de forma obligatoria 
        print("pio")
            
    def volar(self,metros):  #SIEMPRE hay que poner el parametro self de forma obligatoria 
        print(f"El pajaro vuela {metros} metros.")


piolin = Pajaro("amarillo","canario")

piolin.piar()

piolin.volar(50)