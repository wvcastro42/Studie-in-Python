"""
Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos,
sempre escrevendo uma mensagem adequada:
se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
Entrada
A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).

Saída
Imprima todas as classificações do triângulo especificado na entrada.
"""

nums = list(map(float, input().split()))
nums.sort(reverse=True)
a, b, c = nums[0], nums[1], nums[2]

if a**2 == (b**2 + c**2):
    print('TRIANGULO RETANGULO')

if a**2 < (b**2 + c**2):
    print('TRIANGULO ACUTANGULO')

if not a >= (b+c) and a**2 > (b**2 + c**2):
    print('TRIANGULO OBTUSANGULO')

if a == b == c:
    print('TRIANGULO EQUILATERO')

if (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
    print('TRIANGULO ISOSCELES')

if a >= (b+c):
    print('NAO FORMA TRIANGULO')
