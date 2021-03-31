from tatu import Cliente
from tatu import Conta

joao = Cliente('João da Silva', '777-1234')
maria = Cliente('Maria da Silva', '555-4321')

print (f'Nome: {joao.nome}. Telefone: {joao.telefone}.')
conta1 = Conta([joao], 1, 1000)
conta1.resumo()

print (f'Nome: {maria.nome}. Telefone: {maria.telefone}.')
conta2 = Conta([maria, joao], 2, 500)
conta2.resumo()
