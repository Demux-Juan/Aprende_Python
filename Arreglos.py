primero = 50
segundo = 9
arreglo = ['Beto','Igor', 10, 0xff,24,0xfe,"Saul"]


print('\nEl resultado es ', primero + segundo, "\n")
suma= primero + segundo

if suma < 50 :  
    print('La suma de los número es menos que 50 \n')
elif suma == 50:
    print('la suma de los número es exactamente igual a 50 \n')
else:
    print('La suma es mayor que 50 \n')

if 0xff in arreglo:
    print('El número exagecimal se encuentra dentro del arreglo \n')
else:
    print('No se encuentra dentro del arreglo \n')

# Escribir and es igual que &&, y or a ||
# if not x == y, significa que si no son iguales hace algo
# Aqui no hay autoincrementos i++, es i = i + 1

for beto in arreglo:
    print('Sí se encontró el nombre de beto en el arreglo se imprime esta linea correspondiente al tamaño de arreglo')



# Especifica hasta donde hablar del arreglo

print(arreglo[1:3],'\n') #Se muesta el contenido de la 1ra a 3ra casilla
print(arreglo[:3],'\n') #Se muestra el contenido hasta la 3ra casilla
print(arreglo[2:],'\n') #Se muestra el contenido empezando desde la segunda casilla en adelante

###### Concatenar ######

palabra_uno = 'Hola'
palabra_dos = 'Juan'
palabra = 'Saludo: %s %s  ' %( palabra_uno, palabra_dos)
print(palabra * 3)
print('El número de caracteres que tiene es : ', len(palabra),'\n')



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
print(pokemon.nombre, pokemon.nivel, pokemon.peso)




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


