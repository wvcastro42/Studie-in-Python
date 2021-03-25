'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''

name = input("Digite seu nome: ")
psw = input("Digite sua senha: ")
#
# while True:
#     if name != psw:
#         print("Dados registrados...")
#         break
#     print('Nome e senha não podem ser iguais...')
#     name = input("Digite seu nome: ")
#     psw = input("Digite sua senha: ")


while name == psw:
    print('Senha deve ser diferente do Usuario')
    name = input("Digite seu nome: ")
    psw = input("Digite sua senha: ")
print('Dados registrados...')
