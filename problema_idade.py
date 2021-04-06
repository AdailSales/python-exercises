'''
Fazer um programa para ler o nome e a idade de duas pessoas.
Ao final mostrar o nome e a idade média entre essas pessoas, com uma casa decimal, conforme o exemplo.

Exemplo:
    Dados da primeira pessoa:
    Nome: input()
    Idade: 19
    Dados da segunda pessoa:
    Nome: input()
    Idade: 20
    
    A idade média de {primeira pessoa} e {segunda pessoa} é de 19.5 anos.
    
Variáveis:
    primeira_pessoa, segunda_pessoa : caractere
    idade_primeira_pessoa, idade_segunda_pessoa : inteiro
'''

first_person = input('Digite o nome da primeira pessoa: ')
age_first_person = int(input(f'Digite a idade de {first_person}: '))
second_person = input('Digite o nome da segunda pessoa: ')
age_second_person = int(input(f'Digite a idade de {second_person}: '))

middle_ages = (age_first_person + age_second_person) / 2

print(f'A idade média de {first_person} e {second_person} é de {middle_ages} anos.')
