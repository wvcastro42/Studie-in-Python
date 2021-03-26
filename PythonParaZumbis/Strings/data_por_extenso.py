dia, mes, ano = input('Digite uma data - dd/mm/aaaa: ').split('/')

meses = ['', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

print(f'{dia} de {meses[int(mes)]} de {ano}')

    
