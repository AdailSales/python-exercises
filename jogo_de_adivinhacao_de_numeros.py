import random
random_number = random.randint(1,100)
win = False
turns = 0
while win == False:
    your_guess = input("\nDigite um número de 1 a 100: ")
    turns += 1
    if random_number == int(your_guess):
        print('Você ganhou!')
        print('Número de voltas que você usou:',turns)
        win == True
        break
    else:
     if random_number>int(your_guess):
        print('Sua estimativa foi baixa, digite um número maior.')
     else:
        print('Seu palpite foi alto, digite um número menor.')

