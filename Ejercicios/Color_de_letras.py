#En mayusculas se escriben las contantes
from colorama import Fore, init, Style
init()

lista = ['''
▓█████▄ 
▒██▀ ██▌
░██   █▌
░▓█▄   ▌
░▒████▓
 ▒▒▓  ▒ 
 ░ ▒  ▒  
 ░ ░  ░   
   ░      
 ░                                     
''', '''
▓█████  
▓█   ▀ 
▒███  
▒▓█  ▄ 
░▒████▒
░░ ▒░ ░
 ░ ░ 
   ░  
   ░   
''', '''
 ███▄ ▄███▓ 
▓██▒▀█▀ ██▒ 
▓██    ▓██░
▒██    ▒██ 
▒██▒   ░██▒
░ ▒░   ░  ░
░  ░      ░
░      ░   
       ░                                                                              
''', '''
  █    ██ 
  ██  ▓██▒
 ▓██  ▒██░
 ▓▓█  ░██░ 
 ▒▒█████▓ 
 ░▒▓▒ ▒ ▒ 
 ░░▒░ ░ ░ 
  ░░░ ░ ░  
    ░      
 ''','''
 ▒██   ██▒
 ▒▒ █ █ ▒░
 ░░  █   ░
  ░ █ █ ▒ 
 ▒██▒ ▒██▒
 ▒▒ ░ ░▓ ░
 ░░   ░▒ ░
  ░    ░  
  ░    ░     
 ''',]


#print(Fore.GREEN + imag[0] + imag[1])


print( Fore.RED + lista[0] + Fore.GREEN + lista[1] + Fore.CYAN + lista[2] + Fore.YELLOW + lista[3] +Fore.MAGENTA + lista[4]  )