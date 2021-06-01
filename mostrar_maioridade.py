'''
Crie um programa que pergunta o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas atingiram a maioridade e quantas ainda são menores.
'''
from datetime import date
current_year = date.today().year
count_major = 0
count_minor = 0
for person in range(1, 8):
    year_of_birth = int(input('Digite o ano de nascimento: '))
    age = current_year - year_of_birth
    if age >= 18:
        count_major += 1
    else:
        count_minor += 1
print(f'Ao todo tivemos {count_major} pessoas maiores de idade.\n'
    f'E também tivemos {count_minor} pessoas menores de idade.')
