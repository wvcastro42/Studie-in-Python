'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''

n = int(input("Digite um número entre 0 e 10: "))
while True:
    if n in range(0, 11):
        print(f'A nota digitada foi: {n}')
        break
    n = int(input("Digite um número entre 0 e 10: "))
