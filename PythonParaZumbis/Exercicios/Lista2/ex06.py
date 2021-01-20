'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido.
Calcule os descontos e o salário líquido, conforme a tabela abaixo:
a. + Salário Bruto : R$
b. - IR (11%) : R$
c. - INSS (8%) : R$
d. - Sindicato ( 5%) : R$
e. = Salário Liquido : R$ '''

valor_hora = float(input('Digite seu salário: R$ '))
horas_trabalhadas = float(input('Digite quantas horas trabalhadas no mês: '))

bruto = valor_hora * horas_trabalhadas
ir = bruto * 0.11
inss = bruto * 0.08
sindicato = bruto * 0.05
liquido = bruto - ir - inss - sindicato

print(f'a. + Salário Bruto :\t\t R$ {bruto:.2f} reais')
print(f'b. - IR (11%):\t\t\t R$ {ir:.2f} reais')
print(f'c. - INSS (8%):\t\t\t R$ {inss:.2f} reais')
print(f'd. - Sindicato (5%):\t\t R$ {sindicato:.2f} reais')
print(f'e. = Salário Liquido:\t\t R$ {liquido:.2f} reais')
