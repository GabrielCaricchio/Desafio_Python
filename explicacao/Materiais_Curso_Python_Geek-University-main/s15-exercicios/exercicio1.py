"""
1. Crie uma classe Pessoa, contendo nome, data de nascimento e email.
Crie as propriedades getters e setters para os atributos e um método
para imprimir os dados de uma pessoa.
"""

from datetime import date


class Pessoa:

    def __init__(self, nome: str, email: str, data_nascimento: date):
        self.__nome: str = nome
        self.__email: str = email
        self.__data_nascimento: date = data_nascimento

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def data_nascimento(self) -> date:
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: date):
        self.__data_nascimento = data_nascimento

    def imprimir(self) -> None:
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Data Nascimento: {self.data_nascimento.strftime('%d/%m/%Y')}")


if __name__ == '__main__':
    p: Pessoa = Pessoa("Felicity Jones", "felicity@gmail.com", date(1987, 7, 22))

    p.imprimir()
