'''
Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno
'''
a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

if a + b > c or a + c > b or b + c > a:
    if a == b == c:
        print('Este é um triângulo Equilátero!')
    elif a == b or b == c or a == c:
        print('Este é um triângulo Isósceles!')
    else:
        print('Este é um triângulo Escaleno!')
else:
    print('Os valores digitados não são válidos para constituir um triângulo')
