'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa mostre:
- a média de idade do grupo;
- qual é o nome do homem mais velho;
- quantas mulheres têm menos de 20 anos de idade.
'''
add_age = 0
average_age = 0
man_older_age = 0
older_man_name = ' '
women_quantity  = 0

for person_name in range(1,5):
    print(f'----- {person_name}ª PESSOA -----')
    name = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    gender = str(input('Sexo [M/F]: ')).strip()
    add_age += age
    if person_name == 1 and gender in 'Mm':
        man_older_age = age
        older_man_name = name
    if gender in 'Mm' and age > man_older_age:
        man_older_age = age
        older_man_name = name
    if gender in 'Ff' and age < 20:
        women_quantity  += 1
        
average_age = add_age/4
print(f'A média de idade do grupo é de {average_age:.0f} anos.\n'
f'O homem mais velho tem {man_older_age} anos e se chama {older_man_name}.\n'
f'Ao todo, no grupo, tem {women_quantity} mulher(es) com menos de 20 anos.')
