#!usr/bin/python

dinheiro_real = float(input('Quanto de dinheiro você tem na carteira? '))

dinheiro_dolar = dinheiro_real / 5.518

print(f'Com R$ {dinheiro_real:.2f} você pode comprar U$$ {dinheiro_dolar:.2f}.')
