contador=0
menor=10000000000
maior=0
while contador<4:
  numero=float(input("Informe o número: "))
  menor= min(numero,menor)
  maior= max(numero,maior)
  contador+=1
print("O maior número é ",maior,"e o menor é ",menor)