'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''
n = int(input('Digite uma nota entre 0 e 10: '))

# lista_notas = list(range(0, 11))

while n < 0 or n > 10:
    n = int(input('Digite um valor válido entre 0 e 10: '))
    if n >= 0 and n <= 10:
        break

print(f'A nota digitada foi {n}!')
