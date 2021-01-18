'''
Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar
'''
preco = float(input('Digite o preço da mercadoria: '))
percentual = float(input('Digite o percentual de desconto: '))

novo_preco = (preco - (preco * (percentual / 100)))

print(f'O preço da mercadoria com desconto é de R$ {novo_preco:.2f} reais')
