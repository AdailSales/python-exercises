#usr/bin/python3
'''
Título: calculadora_aritmetica.py

Função: Efetua somas, subtrações, multiplicações e divisões.
'''
print('Calculadora')

sair = False

while sair == False:

    numero1 = int(input('\nDigite o primeiro número: '))
    operador = input('Escolha a operação desejada:\n+ para soma;\n- para subtração;\n* para multiplicação;\n/ para divisão.\nDigite o operador: ')
    numero2 = int(input('Digite o segundo número: '))
    
    # Determinando qual operador foi utilizado.
    
    if operador == '+':
        operacao = numero1 + numero2
    elif operador == '-':
        operacao = numero1 - numero2
    elif operador == '*':
        operacao = numero1 * numero2
    elif operador == '/':
        operacao = numero1 / numero2
    else:
        operacao = 'Operador inválido. Use +, -, * ou /.'
    
    print('\nResultado: ', operacao, '\n')
    
    opcao = int(input('Digite 1 para encerrar a calculadora ou 2 para realizar outra operação: '))
    
    if opcao == 1:
        sair = True

