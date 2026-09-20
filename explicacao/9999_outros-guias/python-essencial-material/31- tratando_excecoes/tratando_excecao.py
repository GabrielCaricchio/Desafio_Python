
try:
    numerador = int(input("Digite o numerador: "))
    denominador = int(input("Digite o número a ser dividido: "))
    resultado = numerador / denominador    
except ValueError as e:
    print(e)
    print("Somente números são permitidos.")
except ZeroDivisionError as e:
    print(e)
    print("Deu erro na divisão por 0. Não pode!")
except Exception as e:
    print(e)
    print("Deu erro")
else:
    print(resultado)
finally:
    print("Isso irá executar sempre!")