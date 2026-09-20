import random

# x = random.randint(1, 6)
# y = random.random()

# uma_lista = ['pedra', 'papel', 'tesoura']
# escolha = random.choice(uma_lista)
# print(escolha)

cartas = [1,2,3,4,5,6,7,8,9, "J", "Q", "K", "A"]

random.shuffle(cartas)

print(cartas)