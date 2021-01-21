'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''
name = input('Digite seu nome: ')
psw = input('Digite uma senha: ')

while name.lower().strip() == psw.lower().strip():
    if name.lower().strip() == psw.lower().strip():
        psw = input('Digite uma senha diferente de seu nome: ')
    else:
        break
print('Dados registrados.')
