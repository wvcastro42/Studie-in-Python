'''
Verifique se um inteiro positivo n é primo.
'''
n = int(input("Digite um número: "))
i = 2
divisores = 1

while i <= n:
    if n % i == 0:
        divisores += 1
    i += 1

print(f'O número {n} é primo? Resp.: {divisores == 2}')
