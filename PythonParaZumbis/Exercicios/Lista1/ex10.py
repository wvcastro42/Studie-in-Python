'''
Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.
'''

qtde_fumados_dia = int(input('Digite a quantidade de cigarros fumados por dia: '))

qtde_anos = int(input('Digite há quantos anos você fuma: '))

dias_perdidos = ((qtde_anos * 365 * qtde_fumados_dia * 10) / 1440)

print(f'A estimativa de dias de vida perdidos é de : {dias_perdidos:.2f}')
