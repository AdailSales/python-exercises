'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai
se alistar ao seviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que passa ou que passou do prazo.
'''
from datetime import date
current_year = date.today().year
birth =  int(input('Digite o ano de seu nascimento: '))
current_age = current_year - birth
print(f'Quem nasceu em {birth} tem {current_age} anos em {current_year}.')

if current_age == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif current_age < 18:
    balance = 18 - current_age
    enlistment = current_year + balance
    print(f'Ainda faltam {balance} anos para o seu alistamento.\n'
    f'Seu alistamento será em {enlistment}.'
    )
else:
    balance = current_age - 18
    enlistment = current_year - balance
    print(f'Você já deveria ter se alistado a {balance} anos.\n'
    f'Seu alistamento foi em {enlistment}.'
    )
