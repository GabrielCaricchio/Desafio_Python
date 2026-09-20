"""
3. Faça um programa que tenha uma função que receba uma lista de inteiros
e retorne o maior valor.
"""


def maior(inteiros: list[int]) -> int:
    return max(inteiros)


if __name__ == '__main__':
    lista: list[int] = [2, 5, 1, 0, 89, 23]
    print(f'O maior valor na lista {lista} é {maior(lista)}')
