salario = float(input())

if 0 < salario <= 400:
    print(f'Novo salario: {((salario*0.15) + salario):.2f}\nReajuste ganho: {(salario*0.15):.2f}\nEm percentual: 15 %')

elif 400.01 <= salario <= 800:
    print(f'Novo salario: {((salario*0.12) + salario):.2f}\nReajuste ganho: {(salario*0.12):.2f}\nEm percentual: 12 %')

elif 800.01 <= salario <= 1200:
    print(f'Novo salario: {((salario*0.10) + salario):.2f}\nReajuste ganho: {(salario*0.10):.2f}\nEm percentual: 10 %')

elif 1200.01 <= salario <= 2000:
    print(f'Novo salario: {((salario*0.07) + salario):.2f}\nReajuste ganho: {(salario*0.07):.2f}\nEm percentual: 7 %')

else:
    print(f'Novo salario: {((salario*0.04) + salario):.2f}\nReajuste ganho: {(salario*0.04):.2f}\nEm percentual: 4 %')
