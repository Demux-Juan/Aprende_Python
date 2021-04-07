#####################  Encuentra el número más grande ##############################################################################
lista = [
     143266561,
    1738152473,
     312377936,
    1027708881,
    1495785517,
    1858250798,
    1693786723,
    1871655963,
     374455497,
     430158267,
]

mayor = 0
biggest = 0
for elemento in range( 0, 9, 1):
    
    for invertida in range( 9, -1, -1):
        
        #print("lista1 " + str(lista[elemento]) + " lista2 " + str(lista[invertida]))
       
        if lista[elemento] <= lista[invertida]: 
            mayor = lista[invertida] 
            if biggest <= mayor:
                biggest = mayor
                #print('*** Ahora el número más grande es ',biggest)
        #else:
            
            #print("*** El mayor sigue siendo", biggest)
     
print(f"El número más grande es: {biggest}") 