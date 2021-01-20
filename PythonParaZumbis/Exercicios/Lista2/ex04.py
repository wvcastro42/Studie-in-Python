'''
Faça um Programa que leia três números e mostre o maior deles.
'''
a = int(input('Digite 1 número: '))
b = int(input('Digite 1 número: '))
c = int(input('Digite 1 número: '))

if a >= b and a >= c:
    print(f'Número {a} é o maior')
elif b >= c:
    print(f'Número {b} é o maior')
else:
    print(f'Número {c} é o maior')
