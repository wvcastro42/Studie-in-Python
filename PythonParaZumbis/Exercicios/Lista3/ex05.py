'''
Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando
o algoritmo de Euclides
'''
a = int(input('número 1: '))
b = int(input('número 2: '))

while a % b !=0:
    a, b = b, a%b

print(f'mdc = {b}')
