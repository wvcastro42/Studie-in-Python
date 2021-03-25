'''
This Script should counting which and how many characters exists in a determined string.

Ex.:
>>> contar_caracteres('Oi')
i: 1
o: 1
>>> contar_caracteres('Hello')
e: 1
h: 1
l: 2
o: 1

'''
def contar_caracteres(s):
    caracteres_ordenados = sorted(s.lower())
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
    contar_caracteres("aaaaAAAa")
    print()
    contar_caracteres("bananA")
    print()
    contar_caracteres("Weverton")
