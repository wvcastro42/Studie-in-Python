'''
Supondo que a população de um país A seja da ordem de 80_000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200_000 habitantes com uma taxa de
crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento
'''

a = 80_000
a_taxa = 0.03
b = 200_000
b_taxa = 0.015
anos = 0

while a < b:
    if a < b:
        a = a * a_taxa + a
        b = b * b_taxa + b
        anos += 1

print(anos)
