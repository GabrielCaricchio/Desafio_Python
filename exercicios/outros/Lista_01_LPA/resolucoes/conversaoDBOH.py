while True:
 ac = int(input("digite qual base numérica quer colocar:\n[0] decimal \n[1] binário \n[2] octal \n[3]hexadecimal\n: "))
 num = input("digite o valor: ")
 if ac == 0:
    deci = int(num)
    tt = int(input("digite qual valor deseja converter; \n[0] binario\n[1] octal \n[2] hexadecimal\n: "))
    if tt == 0:
        bi = bin(deci)
        print(f" seu valor em binário e: {bi}")
    elif tt == 1:
        oc = oct(deci)
        print(f"seu valor em octal e: {oc}")
    elif tt == 2:
        he = hex(deci)
        print(f"seu valor em hexadecimal e: {he}")
 elif ac == 1:
   tt = int(input("digite qual valor deseja converter; \n[0] decimal\n[1] octal \n[2] hexadecimal\n: "))
   deci = int(num, 2)
   if tt ==  0:
      print(f"seu numero em decimal e: {deci}") 
   elif tt == 1:
       oc = oct(deci)
       print(f" seu numero em octal e: {oc}")
   elif tt == 2:
       he = hex(deci)
       print(f"seu numero em hexadecimal e: {he}")
 elif ac == 2:
    deci = int(num,8)
    tt = int(input("digite qual valor deseja converter; \n[0] decimal\n[1] binario \n[2] hexadecimal\n: "))
    if tt == 0:
        print(f"o numero em decimal e: {deci}")
    elif tt == 1:
        bi = bin(deci)
        print(f"o numero em binário  e: {bi}")    
    elif tt == 2:
        he = hex(deci)
        print(f"o numero em hexadecimal e: {he}")
 elif ac == 3:
    tt = int(input("digite qual valor deseja converter; \n[0] decimal\n[1] binario \n[2] octal\n: "))                
    deci =int(num,16)
    if tt == 0:
        print(f"o numero em decimal e: {deci}")
    elif tt == 1:
        bi = bin(deci)
        print(f"o numero em binário e: {bi}")
    elif tt == 2:
        oc = oct(deci)
        print(f"oo numero em octal e: {oc}")
 se = int(input("deseja continuar:\n[0]sim  [1]nao\n:"))
 if se == 1:
     break
 
        
                       