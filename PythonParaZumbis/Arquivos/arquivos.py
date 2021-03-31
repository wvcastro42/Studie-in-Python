'''
f = open(r'/home/weverton/Documents/Estudos/PythonParaZumbis/x.txt', 'w') #lê o arquivo do diretório x

for linha in range(101): #laço de 1 a 100 para escrever {linha} no arquivo (cada linha terá 1 número de 0 a 100)
    f.write(f'{linha}\n') #grava/escreve no arquivo

f.close() #fecha o arquivo

'''

# f = open(r'/home/weverton/Documents/Estudos/PythonParaZumbis/x.txt')
# for linha in f.readlines(): #lê cada linha do arquivo
#     print(linha.strip())
# f.close()

# print('arquivo alterado com sucesso...')


# ''' Outra maneira de ler arquivo '''
# with open(r'/home/weverton/Documents/Estudos/PythonParaZumbis/x.txt') as f:
#     print(f.read())

texto = open(r'/home/weverton/Documents/Estudos/PythonParaZumbis/texto.txt', 'r')
cripto = open(r'/home/weverton/Documents/Estudos/PythonParaZumbis/cripto.txt', 'w')

for linha in texto.readlines():
    for letra in linha:
        if letra in 'aeiouõã':
            cripto.write('*')
        else:
            cripto.write(letra)

texto.close()
cripto.close()
