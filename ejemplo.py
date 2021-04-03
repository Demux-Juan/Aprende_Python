primero = 50
segundo = 9
arreglo = ['beto','igor', 10, 0xff]
# comentario, guardar es ctrl + s
# Aqui no hay punto y coma al final de cada instrucción

print('\nEl resultado es ', primero + segundo, "\n")
suma= primero + segundo

if suma < 56 :  
    print('puto \n')
elif suma == 58:
    print('hola juan \n')
else:
    print('brenda \n')

if 0xff in arreglo:
    print('si está \n')
else:
    print('no está \n')

# escribir and es igual que &&, y or a ||
# if not x == y, significa que no son iguales
# aqui no hay autoincrementos i++, es i = i + 1

for holi in arreglo:
    print(holi, '\n')

#funcion sin parametros
#para hacer la funcion tenemos que poner codigo dentro de lo contrario podemos poner solo la palabra reservada pass
def saludo():
    print('hola, buenos dias\n')

saludo()

#funciones con parametros
def total ( primero, segundo):
    print( primero + segundo)

total(50,84)

def total2 ( primero, segundo):
    res = primero + segundo
    return res

print( total2(55,44))

# Especificar hasta donde hablar del arreglo

print( arreglo[1:3])
print( arreglo[:3])
print( arreglo[2:])

# Concatenar
uno = 'hola'
dos = 'juan'
tres = ' saludo: %s %s' %(uno,dos)
print(tres * 3)
print('El número de carac que tiene es : ', len(tres))

# clases 

class mascota:
    def __init__(self) :
        self.nombre = 'Arturo'
        self.edad = 3
        self.altura = 1.2

    def correr(self) :
       return self.edad

#objetos
gato = mascota()

print( '\n', gato.correr())
print(gato.nombre, gato.edad, gato.altura)

#crear archivos
# a es solo escribir sin modificar el contenido que ya existe, r solo lectura, w escritura 
def creacion() :
    archivo = open('texto.txt','w')
    archivo.close()

def escribir() :
    archivo = open('texto.txt','a')
    archivo.write(gato.nombre)
    archivo.close()

def espacio() :
    archivo = open('texto.txt','a')
    archivo.write(' ')
    archivo.close()

#solo lo ejecuta una vez
while False :
    creacion()

escribir()
espacio()


