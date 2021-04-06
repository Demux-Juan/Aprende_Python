'''
La direferencia entre una lista y una tupla es que la tupla es inmutable
osea que no puede cambiar, pero la lista si puede realizar varias funciones
lista = [1, 2, 3, 4]
tupla = (1, 2, 3, 4)

Diccionarios:

diccionario = { 
    'key1': value1,
    'Key2': value2,
    'Key3': value3,
    'Key4': value4,
}



'''

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


# Diccionarios

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



