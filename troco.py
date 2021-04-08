'''
Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
e o valor em dinheiro dado pelo cliente (suponha que haja dinheiro suficiente). Seu programa deve
mostrar o valor do troco a ser devolvido ao cliente.

'''

price = float(input('Digite o preço unitário do produto: '))
quantity = float(input('Digite a quantidade de unidades compradas deste produto: '))
payment = float(input('Digite o valor em dinheiro dado pelo cliente: '))

purchase_price = price * quantity

thing =   payment - purchase_price

print(f'O troco do cliente é de {thing:.2f} reais.')
