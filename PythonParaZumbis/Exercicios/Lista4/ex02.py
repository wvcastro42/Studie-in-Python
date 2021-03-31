'''
 Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os números ímpares na lista IMPAR. Imprima as três listas.

import random

lista = sorted(random.sample(range(100), 20))
pares = []
impares = []

for i in lista:
    print(i)
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)


print(f'A lista original é {lista}')
print(f'Lista par: {sorted(pares)}')
print(f'Lista impar: {sorted(impares)}')


'''

''' Usando list comprehension '''

from random import sample

vetor = sample(range(100), 20)
par = [x for x in vetor if x % 2 == 0]
impar = [x for x in vetor if x % 2 == 1]
print('Vetor', vetor)
print('Pares', par)
print('Ímpares', impar)
