# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
#
# if a > b:
#     print('O primeiro número é o maior!')
# if b > a:
#     print('O segundo número é o maior!')

# idade = int(input('Digite a idade de seu carro: '))
# if idade <= 3:
#     print('Seu carro é novo')
# else:
#     print('Seu carro é velho')

# velocidade = int(input('velocidade: '))
#
# if velocidade > 110:
#     print('Você foi multado...')
#     multa = 5 * velocidade % 110
#     print(f'Sua multa é de R$ {multa:.2f} reais')
# else:
#     print('Siga em frente...')

minutos = int(input('Digite a quantidade em minutos: '))

if minutos < 200:
    taxa = 0.20
elif minutos <= 400:
    taxa = 0.18
elif minutos <= 800:
    taxa = 0.15
else:
    taxa = 0.08
print(f'Sua conta deu R$ {minutos * taxa:.2f} reais')



























#.
