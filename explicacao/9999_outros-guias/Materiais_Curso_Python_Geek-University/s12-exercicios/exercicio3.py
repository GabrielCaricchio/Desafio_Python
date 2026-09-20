"""
3. Faça um programa que receba do usuário o nome de um arquivo texto e mostre
na tela quantas linhas este arquivo possui.
"""

arquivo: str = input('Informe um nome de arquivo para abrir: ')

with open(arquivo, 'r') as arq:
    linhas = arq.readlines()


print(f'Existem {len(linhas)} linha(s) no arquivo.')
