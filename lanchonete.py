'''
Uma lanchonete possui vários produtos. Cada produto possui um código e  um  preço.
Você  deve  fazer  um  programa  para  ler  o  código  e  a quantidade comprada de um produto (suponha um código válido), e daí informar qual o valor a ser pago, com duas casas decimais, conforme tabela de produtos abaixo.

Código do produto           Preço do produto
-----------------------------------------------
1                           R$ 5.00
-----------------------------------------------
2                           R$ 3.50
-----------------------------------------------
3                           R$ 4.80
-----------------------------------------------
4                           R$ 8.90
-----------------------------------------------
5                           R$ 7.32
-----------------------------------------------

Exemplo 1: 
Código do produto comprado: 1
Quantidade comprada: 3
Valor a pagar: R$ 15.00 

Exemplo 2: 
Código do produto comprado: 4
Quantidade comprada: 2
Valor a pagar: R$ 17.80
'''
def switch():
    code = int(input("Código do produto comprado : "))
    quantity = int(input("Quantidade comprada : "))

    if code == 1:
        amount_paid = 5.00 * quantity
        print(f'Valor a pagar: R$ {amount_paid:.2f} \n')
 
    elif code == 2:
        amount_paid = 3.50 * quantity
        print(f'Valor a pagar: R$ {amount_paid:.2f} \n')

    elif code == 3:
        amount_paid = 4.80 * quantity
        print(f'Valor a pagar: R$ {amount_paid:.2f} \n')

    elif code == 4:
        amount_paid = 8.90 * quantity
        print(f'Valor a pagar: R$ {amount_paid:.2f} \n')
    elif code == 5:
        amount_paid = 7.32 * quantity
        print(f'Valor a pagar: R$ {amount_paid:.2f} \n')


switch()

