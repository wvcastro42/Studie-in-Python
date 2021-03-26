'''
 Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os números ímpares na lista IMPAR. Imprima as três listas.
'''
import random

lista = sorted(random.sample(range(1,101), 20))
lista_par = []
lista_impar = []

for i in lista:
    print(i)
    if i % 2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)


print(f'A lista original é {lista}')
print(f'Lista par: {sorted(lista_par)}')
print(f'Lista impar: {sorted(lista_impar)}')
