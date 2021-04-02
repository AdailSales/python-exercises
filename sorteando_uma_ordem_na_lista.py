'''
Um professor quer sortear a ordem de apresentação de trabalho dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''

from random import shuffle
students = input('Digite o nome dos(as) quatro alunos(as) para o sorteio. Use a vígula para separar cada nome: ').split(',')

student1 = students[0]
student2 = students[1]
student3 = students[2]
student4 = students[3]

roster = [student1, student2, student3, student4]
shuffle(roster)

print(f'A ordem de apresentação será:\n{roster}')
