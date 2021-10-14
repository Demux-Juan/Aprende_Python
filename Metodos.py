#La clases contienen métodos("Funciones que sólo funcionan con su clase")
#se puede definir un método como una instancia de una clase y que se encuentra dentro de la clase, y sólo se puede
#usarse con la clase que se usa, una función se declara aparte y cumple una acción para cualquier momento en que se llame
#Los métodos son acciones o funciones que puede realizar un objeto. 


###### Clases ######

class estadisticas:
    def __init__(self) :
        self.nombre = 'pikachu'
        self.nivel = 42
        self.peso = 15.4
        self.color = 'Amarrillo'
        self.especie = 'Rata'

    def ataca(self) :
       return self.nivel



###### Objetos ######

pokemon = estadisticas()
print( pokemon.ataca(),'\n')
print(pokemon.nombre, pokemon.color, pokemon.peso)


###### Crear archivos ######
# "a" es sólo escribir sin modificar el contenido que ya existe, "r" solo lectura, "w" escritura 

def creacion() :
    archivo = open('Archivo_Creado.txt','w')
    archivo.close()

def escribir() :
    archivo = open('Archivo_Creado.txt','a')
    archivo.write(pokemon.nombre)
    archivo.close()

def espacio() :
    archivo = open('Archivo_Creado.txt','a')
    archivo.write(' ')
    archivo.close()

#Sólo crea una vez el documento y lo mantiene para que sea modificado
while False :
    creacion()


escribir()
espacio()
