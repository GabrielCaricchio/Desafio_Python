numero=int(input("Informe um valor: "))
if numero%10==0:
    print("É divisivel por 10")
if numero%5==0:
    print("É divisivel por 5")
if numero%2==0:
    print("É divisivel por 2")
if numero%10!=0 and numero%5!=0 and numero%2!=0:
    print("Não é divisivel por 10, 5 ou 2")
