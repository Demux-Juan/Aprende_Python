''' 
Asi se pueden poner 
comentario multilineas 
para no tener que usar # siempre en python

'''
from colorama import Fore, init, Style #Se cargan las librerias de estilos y color de consola
'''init() #Iniciamos el color

print(Fore.GREEN + " ") #Inicia el cambio de color en Verde


opcion =  int(input("Elige una opción (1, 2, 3) :\n"))

if  opcion == 1:
    print("Elegiste la opción 1")
    print("esto es una práctica")
    print("relacionado a funciones genéricas multiproposito")
    print("Y optimizar el código redundante, Adios\n\n")

elif opcion == 2:
    print("Elegiste la opción 2")
    print("esto es una práctica")
    print("relacionado a funciones genéricas multiproposito")
    print("Y optimizar el código redundante, Adios\n\n")
elif opcion == 3:
    print("Elegiste la opción 2")
    print("esto es una práctica")
    print("relacionado a funciones genéricas multiproposito")
    print("Y optimizar el código redundante, Adios\n\n")
else:
    print("Opción no valida")

print(Style.RESET_ALL, end="") #Finaliza el color de los textos'''

#####  Mejorado #####

#Se define una función
def conversacion(mensaje):
    print(mensaje)
    print("esto es una práctica")
    print("relacionado a funciones genéricas multiproposito")
    print("Y optimizar el código redundante, Adios\n\n")
 
#Se pide que se elija una opción
opcion =  int(input('Elige una opción (1, 2, 3) :\n'))

if  opcion == 1:
    conversacion('Elegiste la opción 1')
    valor1 = 50
    valor2 = 50

elif opcion == 2:
    conversacion('Elegiste la opción 2')
    valor1 = 150
    valor2 = 50

elif opcion == 3:
    conversacion('Elegiste la opción 3')
    valor1 = 100
    valor2 = 200

else:
    init()
    print(Fore.RED + "\nOpción no valida")
    print(Fore.YELLOW + "siga adelante con valores de 0\n")
    valor1 = 0
    valor2 = 0
    print(Style.RESET_ALL, end="") #Finaliza el color de los textos



#funcion sin parametros ("Introduciendo variables")
#para hacer la funcion tenemos que poner código dentro y tabulado, de lo contrario podemos poner solo la palabra reservada pass

def saludo():
    init()
    print(Fore.YELLOW + "B " + Fore.GREEN + "i " + Fore.BLUE + "e " + Fore.RED + "n " + Fore.CYAN + "v " + Fore.MAGENTA + "e " + Fore.WHITE + "n " + Fore.YELLOW + "i " + Fore.RED + "d "+ Fore.BLUE + "o ")
    print(Style.RESET_ALL, end="")



#funciones con parametros

def funcion_sin_return( primero, segundo):
    print("Esta es la suma de los parametros en la funcion sin return: ",primero + segundo)


def funcion_con_return( primero, segundo):
    sum = primero + segundo
    return sum #envia el valor de sum a funcion_con_return, Ahora funcion_con_return tiene un valor

saludo()

funcion_sin_return(valor1,valor2)

valores = str( funcion_con_return(valor1,valor2) )
print("Esta es la suma de los parametros en la funcion con return es: " + valores +"\n\n")