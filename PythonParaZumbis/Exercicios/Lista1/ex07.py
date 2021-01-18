'''
Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C /5 + 32
'''

celsius = float(input('Digite a temperatura em graus ºC: '))
fahrenheit = ((9 * celsius) / 5) + 32

print(f'A temperatura em Fahrenheit é {fahrenheit:.2f} ºF')
