from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
op = randint(0,2)
print ('''suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogo = int(input("sua jogada :"))
print("PEDRA")
sleep(1)
print("PAPEL")
sleep(1)
print("TESOURA")
print('!='*11)
print(f"oponente jogou: {itens[op]}")
print(f"você jogou: {itens[jogo]}")
print('!=' *11)
if op == 0:
   if jogo == 0:
    print('empate')
   elif jogo == 1:
       print(' você venceu!')
   elif jogo == 2:
       print(' você perdeu!')
   else:
       print('jogada inválida!')
if op == 1:
   if jogo == 0:
    print('Você perdeu!')
   elif jogo == 1:
       print('empate')
   elif jogo == 2:
       print('Você venceu!')
   else:
       print('jogada inválida!')
if op == 2:
   if jogo == 0:
    print('Você venceu!')
   elif jogo == 1:
       print(' você perdeu!')
   elif jogo == 2:
       print('empate')
   else:
       print('jogada inválida')

