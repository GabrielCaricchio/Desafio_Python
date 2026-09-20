# operadores lógicos (and, or, not) é usado para verificar se duas ou mais sentenças são verdadeiras

# operadores and e or

temperatura = int( input("Qual a temperatura nesse momento?") )

if temperatura >= 30 and temperatura <= 45:
    print("Está bem quente hoje.")
    print("Saia somente se for necessário.")
elif temperatura >= 16 and temperatura < 30:
    print("Temperatura está boa hoje.")
    print("Podemos sair.")
elif temperatura >= 0 and temperatura < 16:
    print("Está frio hoje.")
    print("Saia somente se for necessário.")
elif temperatura < 0 or temperatura > 45:
    print("Insano!!!")
    print("Não saia de casa.")

# operador not 

temperatura = 0 # qualquer falsy value

if not(temperatura):
    print("O termômetro está funcionando.")