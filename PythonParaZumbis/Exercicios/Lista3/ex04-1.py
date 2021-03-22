'''
A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de formação é simples: os dois primeiros elementos são 1;
a partir de então, cada elemento é a soma dos dois anteriores.
Faça um algoritmo que leia um número inteiro calcule o seu número de Fibonacci. F 1 = 1, F 2 = 1, F 3 = 2, etc.
'''
i = int(input("Número: "))

a, b, k = 1, 1, 1

while k <= i-2:
    a, b = b, a + b
    k += 1

print(b)

# def fat_recursivo(i):
#     if i == 1 or i == 2:
#         return 1
#     return fat_recursivo(i-1) + fat_recursivo(i-2)
#
# print(fat_recursivo(i))
