'''
3. Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um terceiro vetor de 20 elementos,
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. Imprima os três vetores.
'''
import random

lista1 = random.sample(range(1, 101), 10)
lista2 = random.sample(range(1, 101), 10)

print(lista1)
print(lista2)
