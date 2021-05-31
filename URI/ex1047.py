"""
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .
"""
hora_ini, min_ini, hora_fim, min_fim = (map(int, input().split()))
horas = 0
minutos = 0

horas = abs(hora_fim - hora_ini)
minutos = min_fim - min_ini

if hora_ini > hora_fim:
    horas = 24 - abs(hora_fim-hora_ini)

if hora_ini == hora_fim:
    horas = 24


if min_ini == min_fim:
    minutos = 0

if min_ini != min_fim and min_ini > min_fim:
    minutos = 60 - abs(min_fim-min_ini)

if minutos == 59 and horas == 1:
    print(f'O JOGO DUROU {0} HORA(S) E {minutos} MINUTO(S)')
else:
    print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')
