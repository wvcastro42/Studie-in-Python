'''
Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado desprezando os centavos.
Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que nenhuma delas esteja em falta no caixa.
'''
import math

total = math.trunc(float(input("Digite o valor total: ")))
n50, n20, n10, n5, n2, n1 = 0, 0, 0, 0, 0, 0

while total > 0:
    if total//50 > 0:
        n50 = total // 50
        total = total%50
    elif total//20 > 0:
        n20 = total // 20
        total = total%20
    elif total//10 > 0:
        n10 = total // 10
        total = total%10
    elif total//5 > 0:
        n5 = total // 5
        total = total%5
    elif total//2 > 0:
        n2 = total // 2
        total = total%2
    else:
        n1 = total // 1
        total = total%1

print('O troco será: ')
print(f'{n50} nota(s) de 50')
print(f'{n20} nota(s) de 20')
print(f'{n10} nota(s) de 10')
print(f'{n5} nota(s) de 5')
print(f'{n2} nota(s) de 2')
print(f'{n1} nota(s) de 1')
