'''
Desenvolva um jogo no qual o computador vai "pensar" em um número entre 0 e 10.
O jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''
from random import randint
from time import sleep
computer = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
sleep(1.5)
print('Será que você consegue adivinhar qual foi?')
sleep(1.5)
hit = False
guess = 0
while not hit:
    player = int(input('Qual é o seu palpite? '))
    guess +=1
    if player == computer:
        hit = True
    else:
        if player < computer:
            print('Mais... Agora tente mais uma vez!')
        elif player > computer:
            print('Menos... Agora tente mais uma vez!')
sleep(1.5)
print(f'Acertou com {guess} palpites. Parabéns!')
