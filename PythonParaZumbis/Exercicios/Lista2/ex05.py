'''
Faça um Programa que leia três números e mostre o maior e o menor deles.
'''
a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))
c = float(input('Digite um terceiro número: '))

if a >= b and a >= c:
    print(f'Número {a} é o maior')
elif b >= c:
    print(f'Número {b} é o maior')
else:
    print(f'Número {c} é o maior')

if a <= b and a <= c:
    print(f'Número {a} é o menor')
elif b <= c:
    print(f'Número {b} é o menor')
else:
    print(f'Número {c} é o menor')
