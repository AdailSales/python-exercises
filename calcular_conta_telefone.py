'''
Uma operadora de telefonia cobra R$ 50.00 por um plano básico que dá direito a 100 minutos de telefone. Cada minuto que exceder a franquia de 100 minutos custa R$ 2.00. Fazer um programa para ler a quantidade de minutos que uma pessoa consumiu, daí mostrar o valor a ser pago. 

Exemplo 1:
Digite a quantidade de minutos: 22
Valor a pagar: R$ 50.00

Exemplo 2:
Digite a quantidade de minutos: 103
Valor a pagar: R$ 56.00

'''
minutes = int(input('Digite a quantidade de minutos: '))
amount_paid = 50.00
if minutes > 100:
    amount_paid = amount_paid + 2 * (minutes - 100)

print('Valor a pagar: R$', '%.2f' % amount_paid)

