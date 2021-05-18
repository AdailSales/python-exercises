'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
'''
number = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
      [1] converter para binário;
      [2] converter para octal;
      [3] converter para hexadecimal.''')
option = int(input('Sua opção: '))

if option == 1:
    print(f'{number} convertido para binário é igual a {bin(number)}')
elif option  == 2:
    print(f'{number} convertido para octal é igual a {oct(number)}')
elif option == 3:
    print(f'{number} convertido para octal é igual a {hex(number)}')
else:
    print('Opção inválida. Tente novamente.')
    
