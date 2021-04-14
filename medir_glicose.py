'''
Fazer um programa para ler a quantidade de glicose no sangue de uma pessoa e depois mostrar na tela a classificação desta glicose de acordo com a tabela de referência abaixo.

Classificação        Glicose
--------------------------------------------------
Normal               Até 100 mg/dl
--------------------------------------------------
Elevado              Maior que 100 até  140 mg/dl
--------------------------------------------------
Diabetes             Maior de 140 mg/dl
--------------------------------------------------

Exemplo 1:
Digite a medida da glicose: 90.0
Classificação: normal

Exemplo 2:
Digite a medida da glicose: 140.0
Classificação: elevado

Exemplo 3:
Digite a medida da glicose: 143.2
Classificação: diabetes
'''
amount_of_glucose = float(input('Digite a quantidade de glicose: '))

if amount_of_glucose <= 100:
    print('Classificação: normal.')
elif amount_of_glucose <= 140:
    print('Classificação: elevado.')
else:
    print('Classificação: diabetes.')

