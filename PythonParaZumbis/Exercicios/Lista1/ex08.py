'''
Faça agora o contrário, de Fahrenheit para Celsius. F = 9*C /5 + 32
'''
fahrenheit = float(input('Digite a temperatura em ºF: '))

celsius = ((fahrenheit - 32) * 5) / 9

print(f'A temperatura convertida em Celsius é {celsius} ºC')
