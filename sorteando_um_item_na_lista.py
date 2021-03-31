'''
Um professor quer sortear um dos seus oito alunos para apagar o quadro.
Faça um programa que o ajude, lendo o nome deles e escrevendo o nome do escolhido.

'''
import random
students = input('Digite o nome de quatro alunos(as) para o sorteio. Use a vígula para separar cada nome: ').split(',')

student1 = students[0]
student2 = students[1]
student3 = students[2]
student4 = students[3]

roster = [student1, student2, student3, student4]
chosen = random.choice(roster)

print(f'O aluno escolhido foi {chosen}.')





