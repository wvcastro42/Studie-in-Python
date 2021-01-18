'''
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade
de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado
'''

kms = float(input('Digite a quantidade de Kms percorridos: '))
dias = int(input('Digite a quantidade de dias de aluguel: '))

total = (dias * 60) + (kms * 0.15)

print(f'O total do aluguel é de R$ {total:.2f} reais')
