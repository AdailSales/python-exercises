'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Exemplo:
Digite o seu nome: Maria Rita de Sousa e Silva.
Primeiro nome = Maria
Último nome = Silva
'''
full_name = input('Digite o seu nome: ').strip()
name = full_name.split()
print(f'Seu primeiro nome é: {name[0]}\n'
      f'Seu último nome é: {name[len(name)-1]}'
      )


