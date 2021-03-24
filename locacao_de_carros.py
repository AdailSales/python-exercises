#!usr/bin/python3
# Escreva um programa que pergunta a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcular pelo preço a pagar, sabendo que a diária custa R$ 60,00 mais R$ 0.15 por Km rodado.

days = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km rodados? '))
pay = (days * 60) + (km * 0.15)
print(f'\nO total a pagar pelo aluguel é R$ {pay:.2f}.\n')
