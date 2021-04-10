'''
Fazer um programa para ler o nome de um(a) funcionário(a), o valor que ele(a) recebe por hora, e a
quantidade de horas trabalhadas por ele(a). Ao final, mostrar o valor do pagamento do funcionário com
uma mensagem explicativa, conforme exemplo.

Exemplo 1:
Nome: Joao Silva
Valor por hora: 50.00
Horas trabalhadas: 60
O pagamento para Joao Silva deve ser 3000.00

Exemplo 2:
Nome: Maria Dias
Valor por hora: 60.00
Horas trabalhadas: 100
O pagamento para Maria Dias deve ser 6000.00

'''

name = input('Digite um nome: ')
hourly_value = float(input('Digite um valor em real (use ponto para casa decimal, em vez de vírgula): '))
worked_hours = int(input('Digite a quantidade de horas trabalhadas: '))
payment = hourly_value * worked_hours
print(f'O pagamento para {name} deve ser R$ {payment:.2f}')

