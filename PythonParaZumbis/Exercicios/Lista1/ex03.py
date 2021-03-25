'''
Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
'''

dias = int(input('Digite a quantidade em Dias: '))
horas = int(input('Digite a quantidade em Horas: '))
minutos = int(input('Digite a quantidade em Minutos: '))
segundos = int(input('Digite a quantidade em Segundos: '))

seg_dias = dias * 86400
seg_horas = horas * 3600
seg_minutos = minutos * 60

print(f'A quantidade de tempo em Segundos (s) é: {seg_dias + seg_horas + seg_minutos + segundos}')
