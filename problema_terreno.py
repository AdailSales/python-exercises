#!/usr/bin/python3

# criar as variáveis largura, comprimento,metro_quadrado, area, preco: float

# entrada ('Digite a largura do terreno')
# leia (largura)

# entrada ('Digite o comprimento do terreno')
# leia (terreno)

# entrada ('Digite o valor de metro quadrado')
# leia (metro_quadrado)

largura = float(input('Digite a largura do terreno: '))

comprimento = float(input('Digite o comprimento do terreno: '))

metro_quadrado = float(input('Digite o valor do metro quadrado: '))

area = largura * comprimento
preco = area * metro_quadrado

# escreva ('Area do terreno = ' area)
# escreva ('Preço do terreno = ' preco)

print (f'Área do terreno = {area:.0f}m²' )
print (f'Preço do terreno = R$ {preco:.2f}' )
