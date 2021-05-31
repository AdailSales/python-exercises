'''
Crie um programa que leia uma frase e diga se elee é um palíndromo, desconsiderando os espaços.

Exemplos:
Após a sopa
A sacada da casa
A torre da derrota
O lobo ama o bolo
Anotaram a data da maratona
'''
phrase = str(input('Digite uma frase: ')).strip(). upper()
words = phrase.split()
join_words = ''.join(words)
inverted_word = ''
for letter in range(len(join_words) -1, -1, -1):
    inverted_word += join_words[letter]
print(f'O inverso de {join_words} é {inverted_word}')
if inverted_word == join_words:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')
