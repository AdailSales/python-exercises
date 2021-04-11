'''
Fazer um programa para ler uma duração de tempo em segundos, daí imprimir na tela esta duração no
formato horas:minutos:segundos.

Resolução:
variáveis:
    duration, rest, hours, minutes, seconds: integer

duration <- stdin
hours <- duration \ 3600
rest <- duration % 3600
minutes <-  rest \ 60
seconds <- rest % 60

'''
duration = int(input('Escreva a duração em segundos: '))
hours = duration // 3600
rest = duration % 3600
minutes = rest // 60
seconds = rest % 60

print(hours, ':', minutes, ':', seconds)
