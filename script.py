#Autor: Jose Luis Ramirez
#Tengo un punto extra por contestar una pregunta en clase, sobre herencia si no estoy mal creo
#Programa creado con el fin de hacer feliz a un perro por medio de tres acciones, dar un juguete, acariciar y dar comida

#Ceacion de objeto perro
class Perro:

    #Constructor

    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.raza = ""
        self.color = ""
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
            self.hasComida = True

    def acariciar(self):
        if(self.hasCaricia):
            print ("El perro ya fue acariciado, intenta con las demas opciones")
        else:
            print("El perro ha sido acariciado, su felicidad ha aumentado")
            self.felicidad += 1
            self.hasCaricia = True

    def darJuguete(self):
        if(self.hasJuguete):
            print ("Ya le diste el juguete al perro, intenta con las demas opciones")
        else:
            print("Le diste el juguete al perro, su felicidad ha aumentado")
            self.felicidad += 1
            self.hasJuguete=True

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
        
#Funcion creada para tomar los datos del perro
def tomaDatos(perro1):
    print("--------------------------------------------------------------\n" \
    "Bienvenido, vamos a comenzar tomando los datos del perro ")
    perro1.setNombre(input("Ingresa el nombre del perro: "))
    perro1.setEdad(float(input("Ingresa la edad del perro en años: ")))
    perro1.setRaza(input("Ingresa la raza del perro: "))
    perro1.setColor(input("Ingresa el color de tu perro: "))
    print("--------------------------------------------------------------")
    return

#Funcion creada para mostrar los datos del perro
def mostrarDatos(perro1):
    print("--------------------------------------------------------------\n" \
    "Los datos del perro son:  \n" \
    f"Nombre: {perro1.getNombre()} \n" \
    f"Edad: {perro1.getEdad()} \n" \
    f"Raza: {perro1.getRaza()} \n" \
    f"Color: {perro1.getColor()} \n" \
    "--------------------------------------------------------------\n")

#Funcion de menu para interactuar con las distintas funciones
def menu(perro1):
    name=perro1.getNombre()
    opc=0
    opc = int(input("--------------------------------------------------------------\n" \
            f"Que quieres hacer con {name} ?\n" \
            f"1. Ver los datos de {name} \n" \
            f"2. Acariciar a {name} \n" \
            f"3. Dar comida a {name} \n" \
            f"4. Dar juguete a {name} \n" \
            "5. Salir del programa \n"))
    match opc:
        case 1:
            mostrarDatos(perro1)
        case 2:
            perro1.acariciar()
            print(perro1.comprobarFelicidad())
        case 3:
            perro1.darComida()
            print(perro1.comprobarFelicidad())
        case 4:
            perro1.darJuguete()
            print(perro1.comprobarFelicidad())
        case 5:
            print("Saliendo del programa...")
        case _:
            print("Opcion Inexistente, selecciona una opcion valida.")
            
    if(opc == 5):
        return
    elif(perro1.getFelicidad() == 3):
        print("---------------------------------------\n" \
        "Felicidades!, lograste el objetivo, el programa ha terminado.")
    else:
        menu(perro1)
    return

#Funcion main
def main():
    perro1 = Perro()
    tomaDatos(perro1)
    menu(perro1)
    return


if __name__ == "__main__":
    main()
