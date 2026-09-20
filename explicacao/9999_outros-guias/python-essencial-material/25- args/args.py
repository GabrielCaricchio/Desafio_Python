def soma(*argumentos):
    soma = 0
    argumentos = list(argumentos)
    argumentos[0] = 5
    for i in argumentos:
        soma += i
    return soma

print(soma(1,2, 4, 5))