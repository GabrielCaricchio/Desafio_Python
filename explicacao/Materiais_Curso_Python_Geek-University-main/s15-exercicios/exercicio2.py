"""
2. Crie uma classe Agenda que pode armazenar contatos e seja possível
realizar as seguintes operações:

a) armazenar_contato(contato: Contato);
b) remover_contato(contato: Contato);
c) buscar_contato(nome: str); // Informa em que posição da agenda está o contato.
d) imprimir_agenda(); // Imprime os dados de todos os contatos da agenda.
e) imprimir_contato(indice: int); // Imprime os dados do contato informado pelo índice.
"""
from datetime import date

from exercicio1 import Pessoa


class Agenda:

    def __init__(self):
        self.__agenda: list[Pessoa] = []

    @property
    def agenda(self) -> list[Pessoa]:
        return self.__agenda

    def armazenar_contato(self, contato: Pessoa):
        self.agenda.append(contato)

    def remover_contato(self, contato: Pessoa):
        self.agenda.remove(contato)

    def buscar_contato(self, nome: str) -> int:
        for indice, contato in enumerate(self.agenda):
            if contato.nome == nome:
                return indice
        return -1

    def imprimir_agenda(self):
        for contato in self.agenda:
            contato.imprimir()

    def imprimir_contato(self, indice: int):
        self.agenda[indice].imprimir()


if __name__ == '__main__':
    contato1: Pessoa = Pessoa("Felicity Jones", "felicity@gmail.com", date(1987, 7, 22))
    contato2: Pessoa = Pessoa("Angelina Jolie", "angelina@gmail.com", date(1984, 3, 6))
    contato3: Pessoa = Pessoa("Ray Sychev", "ray@gmail.com", date(1981, 8, 18))

    agenda: Agenda = Agenda()

    agenda.armazenar_contato(contato1)
    agenda.armazenar_contato(contato2)
    agenda.armazenar_contato(contato3)

    agenda.imprimir_agenda()

    print(agenda.buscar_contato("Ray Sychev"))

    agenda.imprimir_contato(2)

    agenda.remover_contato(contato3)

    agenda.imprimir_agenda()
