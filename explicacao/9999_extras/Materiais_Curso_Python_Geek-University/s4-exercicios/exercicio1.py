"""
1. Faça um programa que receba dois números inteiros e mostre qual deles é o maior.
"""

numero1: int = int(input("Informe o primeiro número inteiro: "))
numero2: int = int(input("Informe o segundo número inteiro: "))

if numero1 > numero2:
    print(f"O número {numero1} é maior que {numero2}")
elif numero1 == numero2:
    print(f"Os números {numero1} e {numero2} são iguais.")
else:
    print(f"O número {numero2} é maior que {numero1}")

