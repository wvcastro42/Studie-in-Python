'''
1. Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as funções max e min.
'''
import random

lista = random.sample(range(1,101), 10)
menor = 100
maior = 0

for i in lista:
    if i > maior:
        maior = i
    elif i < menor:
        menor = i

# sorted = lista.sort()
print(sorted(lista))
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')
