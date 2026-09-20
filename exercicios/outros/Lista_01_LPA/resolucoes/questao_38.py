print("Informe 3 números diferentes!")
numero0=float(input("Informe o valor: "))
numero1=float(input("Informe o valor: "))
numero2=float(input("Informe o valor: "))
if numero2>numero1 and numero1>numero0:
    maior=numero2
    inter=numero1
    menor=numero0
    print("O maior é:",maior,"\nO do meio é:",inter,"\nO menor é:",menor)
if numero2>numero0 and numero0>numero1:
    maior=numero2
    inter=numero0
    menor=numero1
    print("O maior é:",maior,"\nO do meio é:",inter,"\nO menor é:",menor)
if numero1>numero2 and numero2>numero0:
    maior=numero1
    inter=numero2
    menor=numero0
    print("O maior é:",maior,"\nO do meio é:",inter,"\nO menor é:",menor)
if numero1>numero0 and numero0>numero2:
    maior=numero1
    inter=numero0
    menor=numero2
    print("O maior é:",maior,"\nO do meio é:",inter,"\nO menor é:",menor)
if numero0>numero1 and numero1>numero2:
    maior=numero0
    inter=numero1
    menor=numero2
    print("O menor é:",maior,"\nO do meio é:",inter,"\nO menor é:",menor)
if numero0>numero2 and numero2>numero1:
    maior=numero0
    inter=numero2
    menor=numero1
    print("O maior é:",maior,"\nO do meio é:",inter,"\nO menor é:",menor)