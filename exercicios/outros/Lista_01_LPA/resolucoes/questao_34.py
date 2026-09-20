salario=float(input("Informe o salário bruto: "))
prestacao=float(input("Informe o valor da prestação: "))
if prestacao<=salario*0.3:
    print("Empréstimo liberado.")
else:
    print("Emprestimo negado, o valor excede 30% do salário bruto!")
    