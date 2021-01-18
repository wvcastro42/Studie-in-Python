'''
Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento.
Exiba o valor do aumento e do novo salário.
'''
salario = float(input('Digite o salário: '))
porcentagem = float(input('Digite a porcentagem: '))

aumento = (salario * porcentagem) / 100
novo_salario = salario + aumento

print(f'O aumento será R$ {aumento:.2f}.\nO novo salário será R$ {novo_salario:.2f}')
