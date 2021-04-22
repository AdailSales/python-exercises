'''
Faça um programa que leia uma frase e mostre:
- quantas vezes aparece a letra "A";
- em que posição ela aparece pela primeira vez;
- em que posição ela aparece pela última vez.
'''
phrase = input('Digite uma frase: ').upper().strip()
print(f'A letra "A" aparece {phrase.count("A")} vezes na frase.\n'
      f'A primeira letra "A" apareceu na posição {phrase.find("A")+1}\n'
      f'A última letra "A apareceu na posição {phrase.rfind("A")+1}.'
      )

