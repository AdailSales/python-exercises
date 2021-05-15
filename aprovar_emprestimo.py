'''
Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.
'''
value_of_the_house = float(input('Valor da casa: '))
buyer_salary = float(input('Salário do comprador: '))
years_of_funding = float(input('Quantos anos de financiamento? '))

maximum_performance = buyer_salary * 0.3
months_of_benefit = years_of_funding * 12
amount_of_benefit = value_of_the_house / months_of_benefit

print(f'Para pagar uma casa de R$ {value_of_the_house:.2f} em {years_of_funding} anos a prestação será de R$ {amount_of_benefit:.2f}')

if amount_of_benefit > maximum_performance:
    print('Empéstimo negado.')
else:
    print('Empréstimo pode ser concedido.')
