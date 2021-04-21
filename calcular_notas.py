'''
Fazer um programa para ler as duas notas que um aluno obteve no primeiro e segundo semestres de uma disciplina anual.
Em seguida, mostrar a nota final que o aluno obteve (com uma casa decimal) no ano juntamente com um texto explicativo.
Caso a nota final do aluno seja inferior a 60.00, mostrar a mensagem "REPROVADO", conforme exemplos.  

Exemplo 1:
Digite a primeira nota: 45.5
Digite a segunda nota: 31.3
NOTA FINAL = 76.8

Exemplo 2: Digite a primeira nota: 34.0
Digite a segunda nota: 23.5
NOTA FINAL = 57.5 REPROVADO
'''

first_note = float(input('Digite a primeira nota: '))
second_note = float(input('Digite a segunda nota: '))
final_grade = (first_note + second_note) / 2

if final_grade >= 60.0:
    print(f'NOTA FINAL = {final_grade:.1f} APROVADO')
else:
    print(f'NOTA FINAL = {final_grade:.1f} REPROVADO')

