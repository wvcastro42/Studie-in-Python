'''
Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120.
Dado um inteiro não-negativo n, verificar se n é triangular.
'''

n = int(input("Digite um número: "))
aux = 1

if (n * (n + 1) ) / 2 % 2 == 0:
    print(f'O número {n} é triangular')
else:
    print(f'O número digitado não é triangular')
