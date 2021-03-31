'''
3. Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um terceiro vetor de 20 elementos,
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. Imprima os três vetores.
'''
import random

lista1 = random.sample(range(1, 101), 20)
lista2 = random.sample(range(1, 101), 20)
lista3 = []

print((lista1))
print((lista2))

j = 0
for i in lista1:
    lista3.append(i)
    while j < len(lista2):
        lista3.append(lista2[j])
        j += 1
        break


print((lista3))

'''
Solução Zip, Masanori

from random import sample
v1 = sample(range(100), 10)
v2 = sample(range(100), 10)
v3 = []

for x in zip(v1, v2):
    v3.extend(list(x))
print('v1: ', v1)
print('v2: ', v2)
print('v3: ', v3)
'''
