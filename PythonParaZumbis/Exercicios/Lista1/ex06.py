'''
Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem
'''
distancia = float(input('Digite a distância em quilômetros: '))
velocidade = float(input('Digite a velocidade em Km/h: '))

tempo = distancia / velocidade

print(f'O tempo de viagem será de: {tempo:.2f} hora(s)')
