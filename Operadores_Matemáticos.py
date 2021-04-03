# comentario, guardar es ctrl + s
# Para abrir una terminal oprime Ctrl + shift + ñ
# Si quieres ejecutar el código en la terminal solo typea "python [Nombre del archivo.py] y da enter"
# Aqui no hay punto y coma al final de cada instrucción


A = input("Inserta el primer cantidad\n") #Cuando se inserta la cantidad toma el formato string
B = input("Inserta el segundo cantidad\n")
A = int(A) #Aqui lo convertimos a entero
B = int(B)

suma = A + B
print("La suma de las cantidades es: \n", suma)

resta = A - B
print("La resta de las cantidades es: \n", resta)

multiplicacion = A * B
print("La multiplicación de las cantidades es: \n", multiplicacion)

division = A / B
print("La división de las cantidades es: \n", division)

flotante = float(division)
print("División convertida en float: \n", flotante)

cociente = A // B
print("El cociente de las cantidades es: \n", cociente)

residuo = A % B 
print("El residuo de las cantidades es: \n", residuo)

potencia = A ** B 
print("La potencia de la primera cantidad elevada a la segunda cantidad es: \n", potencia)

import math
raiz_cuadrada = math.sqrt(A) 
print("La raíz cuadrada de la primera cantidad es: \n", raiz_cuadrada)

string = str(raiz_cuadrada)
print("Raíz cuadrada convertida a string: \n", string)

redondeo = round(raiz_cuadrada, 2)
print("Redondeo de la raíz cuadrada a dos digitos: \n", redondeo)

