import random
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
print('Vamos jogar jokenpo? ^_^')
print('Suas opções: \n[ 0 ] PEDRA \n[ 1 ] PAPEL \n[ 2 ] TESOURA')
jog = int(input('Qual é a sua jogada? '))
pc = random.choice([0, 1, 2])
print('')
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-'*30)
print('Computador jogou {}'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[jog]))
print('-'*30)
if jog == 0:
    if pc == 0:
        print('EMPATE')
    elif pc == 1:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADOR VENCE')
elif jog == 1:
    if pc == 0:
        print('JOGADOR VENCE')
    elif pc == 1:
        print('EMPATE')
    else:
        print('COMPUTADOR VENCE')
else:
    if pc == 0:
        print('COMPUTADOR VENCE')
    elif pc == 1:
        print('JOGADOR VENCE')
    else:
        print('EMPATE')
