'''
1. Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as funções max e min.
'''
from random import sample

lista = sample(range(1,101), 10)
menor = 100
maior = 0

for i in lista:
    if i > maior:
        maior = i
    elif i < menor:
        menor = i

print(sorted(lista))
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')


'''
Resolução Masanori:

from random import sample
vetor = sample(range(100), 10)
maior = menor = vetor[0]

for x in vetor[1:]:
    if x > maior: maior = x
    if x < menor: menor = x

print('Vetor: ', vetor)
print(f'Maior: {maior}')
print(f'Menor: {menor}')
'''
