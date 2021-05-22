"""
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.
Saída
Imprima a saída conforme foi especificado."""

valores = list(map(int, input().split()))
[print(x) for x in sorted(valores)]
print()
[print(x) for x in valores]
