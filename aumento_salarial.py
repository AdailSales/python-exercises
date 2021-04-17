'''
Uma empresa vai conceder um aumento percentual de salário aos seus funcionários dependendo de quanto cada pessoa ganha, conforme tabela abaixo.
Fazer um programa para ler o salário de uma pessoa, daí mostrar qual o novo salário desta pessoa depois do aumento, quanto foi o aumento e qual foi a porcentagem de aumento.

Salário atual                                   Aumento
---------------------------------------------------------
Até R$ 1000.00                                  20%
---------------------------------------------------------
Acima de R$ 1000.00 até R$ 3000.00              15%
---------------------------------------------------------
Acima de R$ 3000.00 até R$ 8000.00              10%
---------------------------------------------------------
Acima de R$ 8000.00                             5%
---------------------------------------------------------

Exemplo 1:
Digite o salário da pessoa: 2500.00
Novo salário = R$ 2875.00
Aumento = R$ 375.00
Porcentagem = 15 %

Exemplo 2:
Digite o salário da pessoa: 8000.00
Novo salário = R$ 8800.00
Aumento = R$ 800.00
Porcentagem = 10 % 
'''
salary = float(input('Digite o salário da pessoa: '))

if salary <= 1000.00:
    new_salary = salary + (salary * 20 / 100)
    increase = salary * 20 / 100
    percentage = '20 %'
if salary > 1000.00 and salary <= 3000.00:
    new_salary = salary + (salary * 15 / 100)
    increase = salary * 15 / 100
    percentage = '15 %'
if salary > 3000.00 and salary <= 8000.00:
    new_salary = salary + (salary * 10 / 100)
    increase = salary * 10 / 100
    percentage = '10 %'
if salary > 8000.00:
    new_salary = salary + (salary * 5 / 100)
    increase = salary * 5 / 100
    percentage = '5 %'

print(f'Novo Salário = R$ {new_salary:.2f}\n'
      f'Aumento = R$ {increase:.2f}\n'
      f'Porcentagem = {percentage}'
      )
