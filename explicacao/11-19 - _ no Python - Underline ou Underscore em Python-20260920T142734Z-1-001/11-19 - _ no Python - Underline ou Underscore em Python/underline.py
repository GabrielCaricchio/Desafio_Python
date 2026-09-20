# usos do underline/underscore em Python

# Não serve para nada, e isso é muito bom

# Separador de milhar
faturamento = 1_000_000_000

# # Variáveis "inúteis"
def calcular_imposto(faturamento):
    if faturamento < 1000:
        taxa = 0
    elif faturamento < 10000:
        taxa = 0.1
    elif faturamento < 500000:
        taxa = 0.15
    else:
        taxa = 0.2
    
    if taxa == 0:
        isento_imposto = True
    else:
        isento_imposto = False

    imposto = taxa * faturamento
    
    return imposto, isento_imposto

faturamento = 15000
valor_imposto, _ = calcular_imposto(faturamento)

lucro = faturamento - valor_imposto
print(lucro)


# # Sinalizações de métodos/variáveis privados
class Filme():
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
    
    def detalhar_filme(self):
        print("Titulo", self.titulo)
        print("Descrição", self.descricao)


meu_filme = Filme("Avatar", "Carinhas azuis defendendo o planeta deles")
meu_filme.detalhar_filme()
