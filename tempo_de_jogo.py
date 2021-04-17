'''
Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

Exemplo 1:
Hora inicial: 16
Hora final: 2
O JOGO DUROU 10 HORA(S) 

Exemplo 2:
Hora inicial: 0
Hora final: 0
O JOGO DUROU 24 HORA(S)

Exemplo 3:
Hora inicial: 2
Hora final: 16
O JOGO DUROU 14 HORA(S)
'''
start_time = int(input('Hora inicial: '))
final_hour = int(input('Hora final: '))

if final_hour > start_time:
    total_hours = final_hour - start_time
else:
    total_hours = (24 -  start_time) + final_hour

print(f'O jogo durou {total_hours} hora(s)')

