idade = int(input('Digite a sua idade: '))

if idade >= 0 and idade < 16:
    print('Você não pode votar.')
elif idade >=16 and idade < 18 or idade >= 70:
    print('Seu voto é opcional.')
elif idade >=18 and idade < 70:
    print('Voto obrigatório.')
else:
    print('Idade inválida.')
