"""Teste para os exercícios do Python Para Zumbis."""


# J. zeros finais
# Verifique quantos zeros há no final de um número inteiro positivo
# Exemplo: 10010 tem 1 zero no fim e 908007000 possui três

def zf(n):
    s = str(n)
    count = 0
    for i in range(len(s)):
        print(s[i])
        if s[i] == '0' and s[i+1:] == (len(s[i+1:]))*'0':
            count += 1
    return count





print (zf(908007000))
