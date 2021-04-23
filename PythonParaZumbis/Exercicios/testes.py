"""Teste para os exercícios do Python Para Zumbis."""
# L. inicio em potencia de 2
# Dado um número inteiro positivo n retorne a primeira potência de 2
# que tenha o início igual a n
# Exemplo: para n = 65 retornará 16 pois 2**16 = 65536

def inip2(n):
    for i in range(1_000_000):
        num = str(2**i)
        if num[:len(str(n))] == str(n):
            return i





print (inip2(7))
