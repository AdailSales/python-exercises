#!usr/bin/python3
'''
Faça um algoriTMO que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
'''

salary = float(input('Qual é o salário do funcionário? R$ '))
new_salary = salary + (salary * 15/100)
print(f'Um funcionário que ganhava R$ {salary:.2f}, com 15% de aumento, passa a receber R$ {new_salary:.2f}.')
