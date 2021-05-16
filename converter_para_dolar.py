# Faça um programa que converte um valor em dólar para real.

dolar = 5.48
value = float(input('Quantos dólares você quer converter?\n'))
total = value * dolar
total_value = int(total)
print (f"O valor de ${value:.2f} em real é R${total_value:.2f}.")
