"""
1. Crie a classe Veiculo, contendo marca e modelo.
Crie as propriedades getters e setters para os atributos e
um método para imprimir os dados de um veículo. Crie também o construtor da classe.
"""


class Veiculo:

    def __init__(self, marca: str, modelo: str) -> None:
        self.__marca: str = marca
        self.__modelo: str = modelo

    @property
    def marca(self) -> str:
        return self.__marca

    @marca.setter
    def marca(self, marca: str) -> None:
        self.__marca = marca

    @property
    def modelo(self) -> str:
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo: str) -> None:
        self.__modelo = modelo

    def imprimir(self) -> None:
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')

