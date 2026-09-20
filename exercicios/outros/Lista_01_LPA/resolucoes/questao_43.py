peso=float(input("Informe o seu peso em kg:"))
altura=float(input("Informe sua altura em metro: "))
imc=peso/altura**2
if imc<20:
    print("Abaixo do peso")
if imc>=20 and imc<25:
    print("Peso normal")
if imc>=25 and imc<30:
    print("Sobre peso")
if imc>=30 and imc<40:
    print("Obeso")
if imc>=40:
    print("Obeso mórbido")
   