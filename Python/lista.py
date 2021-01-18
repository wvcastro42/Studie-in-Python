'''
Exemplos de como cria listas e suas interações
'''

[1,2,3]
print(type([]))

lista = list(range(10)) #cria uma lista usando o metodo LIST com o range de 0 a 9
print(lista)

lista2 = list(range(1,10))
print(lista2)

lista3 = list(range(1,10,2)) #lista de 1 a 10, excluindo o último item (10) pulando de 2 em 2
print(lista3)

lista4 = list(range(2,11,2)) #lista com os números pares de 1 a 10
print(lista4)

lista56 = [2, 1, 42, 36, 25, 31, 29, 12, 13, 666]
print(lista56)
lista56.sort()
print(lista56)
lista56.append(7) #adicionar um número na última posição
print(lista56)
lista56.pop() #remove elemento da última posição
lista56.pop(0) #remove elemento na posição desejada
print(lista56)
