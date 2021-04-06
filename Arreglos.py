
#####################  Ejemplo de uso de arreglos con varios tipos de variable ###################################################

''' 
Todas las variables y arreglos se declaran en minusculas, la mayusculas estan reservadas para
las constantes.
 
* Escribir and en lugar de &&, y or en vez de ||
* if not x == y, significa que si no es X igual a Y se va a realizar algo
* Aqui no hay autoincrementos i++, es i = i + 1 o i += 1
 '''

arreglo = [ 'Beto', 'Igor', 10, 0xff, 24, 0xfe, "Saul", 10]

print('\nEl resultado es ', primero + segundo, "\n")
suma= primero + segundo



if 0xff in arreglo:
    print('El número exagecimal se encuentra dentro del arreglo \n')
else:
    print('No se encuentra dentro del arreglo \n')



for beto in arreglo:
    print('Sí se encontró el nombre de beto en el arreglo se imprime esta linea correspondiente al tamaño de arreglo')



#####################  Especifica hasta donde se muestra el arreglo ################################################################

print(arreglo[1:3],'\n') #Se muesta el contenido de la 1ra a 3ra casilla
print(arreglo[:3],'\n') #Se muestra el contenido hasta la 3ra casilla
print(arreglo[2:],'\n') #Se muestra el contenido empezando desde la segunda casilla en adelante


###################################  Diccionarios ##################################################################################


'''
#### Arreglos ####

La direferencia entre una lista y una tupla es que la tupla es inmutable
osea que no puede cambiar, no se le puede quitar ni agregar elementos,
pero la lista si puede realizar varias funciones como la lista.

lista = [1, 2, 3, 4]
tupla = (1, 2, 3, 4)

##### Diccionarios #####

diccionario = { 
    'key1': value1,
    'Key2': value2,
    'Key3': value3,
    'Key4': value4,
}
'''



info_pokemon = { 
    'Raicuaza'  : 'Dragon',
    'Pikachu'   : 'Electrico', 
    'Metacross' : 'Acero',
    'Charizart' : 'Fuego',
}

for pokemon in info_pokemon.keys():
    print(pokemon)
print('\n')

for tipo in info_pokemon.values():
    print(tipo)
print('\n')

for pokemon_y_tipo in info_pokemon.items():
    print(pokemon_y_tipo)
print('\n')
  

print(info_pokemon['Metacross'])

