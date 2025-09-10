#Autor: Jose Luis Ramirez
#Programa creado con el fin de hacer feliz a un perro por medio de tres acciones, dar un juguete, acariciar y dar comida

class perro:

    #Constructor
    def __init__(self, nombre, edad, raza, color):
        self.nombre = nombre
        self.edad = int(edad)
        self.raza = raza
        self.color = color
        self.hasComida = False
        self.hasCaricia = False
        self.hasJuguete = False
        self.felicidad = 0

    #Declaracion de getters y setters
    
    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre
        return
    
    def getEdad(self):
        return self.edad
    def setEdad(self, edad):
        self.edad = edad
        return
    
    def getRaza(self):
        return self.raza
    def setRaza(self, raza):
        self.raza = raza
        return
    
    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color = color
        return
    
    def getFelicidad(self):
        return self.felicidad 

    #Declaracion de metodos

    def darComida(self):
        if(self.hasComida):
            print ("El perro ya fue alimentado, intenta con las demas opciones")
        else:
            print ("El perro ha sido alimentado, su felicidad ha aumentado")
            self.felicidad += 1

    def acariciar(self):
        if(self.hasCaricia):
            print ("El perro ya fue acariciado, intenta con las demas opciones")
        else:
            print("El perro ha sido acariciado, su felicidad ha aumentado")
            self.felicidad += 1

    def darJuguete(self):
        if(self.hasJuguete):
            print ("Ya le diste el juguete al perro, intenta con las demas opciones")
        else:
            print("Le diste el juguete al perro, su felicidad ha aumentado")
            self.felicidad += 1

    def comprobarFelicidad(self):
        nombre = self.nombre
        if(self.felicidad < 1):
            return(f"La felicidad de {nombre} esta en 0%, intenta interactuar mas con el")
        elif(self.felicidad < 2):
            return(f"La felicidad de {nombre} esta en 33% interactua un poco mas con el")
        elif(self.felicidad < 3):
            return(f"La felicidad de {nombre} esta en 66% ya casi lo logras")
        elif(self.felicidad == 3):
            return(f"La felicidad de {nombre} esta en 100%, lograste el objetivo")