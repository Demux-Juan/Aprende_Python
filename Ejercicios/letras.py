import string

alfabeto = string.ascii_lowercase

# TODAS LAS COMBINACIONACIONES POSIBLES DE LETRAS ADYACENTES
for letra in range(0,26):
    if alfabeto[letra] == "z" :
        print("\n\n\n")
        break

    else:
        print (f"{ alfabeto[letra] }{ alfabeto[letra] }")
        print (f"{ alfabeto[letra] }{ alfabeto[letra + 1] }")
        print (f"{ alfabeto[letra + 1] }{ alfabeto[letra]}")
        print (f"{ alfabeto[letra + 1] }{ alfabeto[letra + 1]}")


# TODAS LAS COMBINACIONES POSIBLES DE TODAS LAS LETRAS
for lista1 in range( 0,26):
    
    for lista2 in range( 0,26):
        
        print(str(alfabeto[lista1]) + str(alfabeto[lista2]))
       
