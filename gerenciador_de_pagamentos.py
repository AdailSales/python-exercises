'''
Elabore um programa que calcule um valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto.
- à vista no cartão: 5% de desconto.
- em até 2x no cartão: preço normal.
- 3x ou mais no cartão: 20% de juros.
'''
print(f' {" LOJAS CYSSALES ":=^40}')
price = float(input('Preço das compras: '))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
''')
option = int(input('Qual é a opção? '))

if option == 1:
    total_price = price - (price * 10/100)
    print(f'O valor total é: R$ {total_price:.2f}')
elif option == 2:
    total_price = price - (price * 5/100)
    print(f'O valor total é: R$ {total_price:.2f}')
elif option == 3:
    total_price = price
    parcel = price / 2
    print(f'Sua compra será parcelada em 2x de R$ {parcel:.2f}, sem juros.\n'
    f'O valor total é: R$ {total_price:.2f}')
elif option == 4:
    amount_plots = int(input("Quantas parcelas? "))
    total_price = price + (price * 20/100)
    parcel = total_price / amount_plots
    if amount_plots >= 3:
        print(f'Sua compra será parcelada em {amount_plots}x de R$ {parcel:.2f}, com juros.\n'
    f'O valor total é: R$ {total_price:.2f}')
    else:
        print('OPÇÃO INVÁLIDA\nO limite mínimo de parcelas é 3! Escolha novamente a quantidade de parcelas!')
else:
    print('ERRO\nOPÇÃO INVÁLIDA de pagamento. Tente novamente!')
