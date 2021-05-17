'''
Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado desprezando os centavos.
Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que nenhuma delas esteja em falta no caixa.
'''

notes = int(input())
print(notes)
print("{} nota(s) de R$ 100,00".format(int(notes/100)))
aux = (notes%100)
print("{} nota(s) de R$ 50,00".format(int(aux/50)))
aux = (aux%50)
print("{} nota(s) de R$ 20,00".format(int(aux/20)))
aux = (aux%20)
print("{} nota(s) de R$ 10,00".format(int(aux/10)))
aux = (aux%10)
print("{} nota(s) de R$ 5,00".format(int(aux/5)))
aux = (aux%5)
print("{} nota(s) de R$ 2,00".format(int(aux/2)))
aux = (aux%2)
print("{} nota(s) de R$ 1,00".format(int(aux/1)))
# total = int(input())
# n_total = total
# n100, n50, n20, n10, n5, n2, n1 = 0, 0, 0, 0, 0, 0, 0
#
# if (total > 0 and total < 1000000):
#     while total > 0:
#         if total//100 > 0:
#             n100 = total // 100
#             total = total%100
#         elif total//50 > 0:
#             n50 = total // 50
#             total = total%50
#         elif total//20 > 0:
#             n20 = total // 20
#             total = total%20
#         elif total//10 > 0:
#             n10 = total // 10
#             total = total%10
#         elif total//5 > 0:
#             n5 = total // 5
#             total = total%5
#         elif total//2 > 0:
#             n2 = total // 2
#             total = total%2
#         else:
#             n1 = total // 1
#             total = total%1
#
# print(f'{n_total}')
# print(f'{n100} nota(s) de 100,00')
# print(f'{n50} nota(s) de 50,00')
# print(f'{n20} nota(s) de 20,00')
# print(f'{n10} nota(s) de 10,00')
# print(f'{n5} nota(s) de 5,00')
# print(f'{n2} nota(s) de 2,00')
# print(f'{n1} nota(s) de 1,00')


# conta = int(input('Conta: '))
# pgto = int(input('Pagamento: '))
# troco = pgto - conta
# notas = [50, 20, 10, 5, 2, 1]
# for nota in notas:
#     while troco >= nota:
#         print(f'Uma nota de {nota}')
#         troco -= nota
