'''
Dado um número inteiro positivo, determine a sua decomposição em fatores primos
calculando também a multiplicidade de cada fator.
'''
n = int(input('Numero: '))

for k in range(2, n):
    while n % k == 0:
        print(k)
        n = n / k
