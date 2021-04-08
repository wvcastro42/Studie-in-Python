'''
Questão C. Entre 1067 e 3627 (inclusive), quantos números são pares e
também divisíveis por 7?
Resposta: 183
'''
soma = 0

for i in range(1067, 3628):
    if i % 2 == 0 and i % 7 == 0:
        soma = soma + 1
print(soma)

print(len([i for i in range(1067, 3628) if i % 2 == 0 and i % 7 ==0]))
