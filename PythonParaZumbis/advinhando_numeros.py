"""Advinhando número de 0 a 100."""
import random
print ('Bem vindo!')
numero = random.randint(0,101)
chute = 0

while chute != numero:
    chute = int(input ('Chute um número: '))
    if chute == numero:
        print ('Você venceu!')
    else:
        if chute > numero:
            print ('Alto!')
        else:
            print ('Baixo!')
print ('Fim do jogo')
