"""Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.
"""
notes = float(input())
print('NOTAS:')
print("{} nota(s) de R$ 100.00".format(int(notes/100)))
aux = (notes%100)
print("{} nota(s) de R$ 50.00".format(int(aux/50)))
aux = (aux%50)
print("{} nota(s) de R$ 20.00".format(int(aux/20)))
aux = (aux%20)
print("{} nota(s) de R$ 10.00".format(int(aux/10)))
aux = (aux%10)
print("{} nota(s) de R$ 5.00".format(int(aux/5)))
aux = (aux%5)
print("{} nota(s) de R$ 2.00".format(int(aux/2)))
aux = (aux%2)
print('MOEDAS:')
print("{} moeda(s) de R$ 1.00".format(int(aux/1)))
aux = (aux%1)
print("{} moeda(s) de R$ 0.50".format(int(aux/0.5)))
aux = (aux%0.5)
print("{} moeda(s) de R$ 0.25".format(int(aux/0.25)))
aux = (aux%0.25)
print("{} moeda(s) de R$ 0.10".format(int(aux/0.10)))
aux = (aux%0.10)
print("{} moeda(s) de R$ 0.05".format(int(aux/0.05)))
aux = (aux%0.05)
print("{} moeda(s) de R$ 0.01".format(int(round(aux,2)/0.01)))
aux = (aux%0.01)
