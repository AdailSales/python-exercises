list_of_weights =[]  #lista vazia

for weight in range(1, 6):

    weight_value =float(input(f'Peso da {weight}ª pessoa: '))

    list_of_weights += [weight_value] #adicionando os valores de peso na lista

print(' ')
print(f'O Maior peso foi: {max(list_of_weights)} Kg') #maximo valor da lista
print(f'O Menor peso foi: {min(list_of_weights)} Kg') #minimo valor da lista
