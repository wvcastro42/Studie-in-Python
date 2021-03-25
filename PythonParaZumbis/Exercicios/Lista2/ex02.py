'''
Determine se um ano é bissexto. Verifique no Google como fazer isso...
'''
ano = int(input('Digite um ano: '))

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print(f'Este ano ({ano}) é bissexto')
else:
    print('Ano não bissexto')
