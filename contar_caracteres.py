#!usr/bin/python3
def contar_caracteres(s):
    """Função que conta os carcteres de uma string.
    Ex:
        >>> contar_caracteres('adail')
        a: 2
        d: 1
        i: 1
        l: 1

    :param s: String a ser contada.
    """
    caracteres_ordenados = sorted(s)
    caracter_anterior = caracteres_ordenados[0]
    contagem = 1
    
    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior}: {contagem}')
            caracter_anterior = caracter
            contagem = 1
    print(f'{caracter_anterior}: {contagem}')

if __name__ == '__main__':
    contar_caracteres('paralepípedo de pedra')
