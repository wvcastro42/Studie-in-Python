"""Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1.
A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000)."""

notes = int(input())
print(notes)
print("{} nota(s) de R$ 100,00".format(int(notes/100)))
aux = (notes%100)
print("{} nota(s) de R$ 50,00".format(int(aux/50)))
aux = (aux%50)
print("{} nota(s) de R$ 20,00".format(int(aux/20)))
aux = (aux%20)
print("{} nota(s) de R$ 10,00".format(int(aux/10)))
aux = (aux%10)
print("{} nota(s) de R$ 5,00".format(int(aux/5)))
aux = (aux%5)
print("{} nota(s) de R$ 2,00".format(int(aux/2)))
aux = (aux%2)
print("{} nota(s) de R$ 1,00".format(int(aux/1)))
