'''
A Confederação Nacional de Natação precisa de um programa que leai o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Júnior
- Até 25 anos: Sênior
- Acima: Master
'''
from datetime import date
current_year = date.today().year
year_of_birth = int(input('Digite o ano de nascimento: '))
age_of_the_athlete = current_year - year_of_birth
print(f'O atleta tem {age_of_the_athlete} anos.')

if age_of_the_athlete <= 9:
    print('Classificação: MIRIM')
elif age_of_the_athlete <= 14:
    print('Classificação: INFANTIL')
elif age_of_the_athlete <= 19:
    print('Classificação: JÚNIOR')
elif age_of_the_athlete <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
    
    
    
