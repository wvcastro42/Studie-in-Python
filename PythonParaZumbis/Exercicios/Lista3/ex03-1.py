'''
Supondo que a população de um país A seja da ordem de 80_000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200_000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento
'''
cid_a = 80_000
cid_b = 200_000
anos = 0

while cid_a <= cid_b:
    cid_a = cid_a + (cid_a * 0.03)
    cid_b = cid_b + (cid_b * 0.015)
    anos += 1
print(f'A população da cidade A levará {anos} anos para igualar ou ultrapassar a população da cidade B')
