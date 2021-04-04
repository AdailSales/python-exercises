'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas e minúsculas.
Quantas letras ao todo sem considerar espaços.
Quantas letras tem o primeiro nome.

'''
name = str(input('Digite seu nome completo: ')).strip()
print('Analisando o seu nome...')
print(f'Seu nome em maiúsculas é {name.upper()}.\n'
      f'Seu nome em minúsculas é {name.lower()}\n'
      f'Seu nome tem ao todo {len(name) - name.count(" ")} letras.'
      # f'Seu primeiro nome tem {name.find(" ")} letras\n.'
      # Preferi usar o método split() para separar os nomes do que usar o find().
      )
break_apart_names = name.split(' ')
print(f'Seu primeiro nome é {break_apart_names[0].capitalize()} e ele tem {len(break_apart_names[0])} letras.')

