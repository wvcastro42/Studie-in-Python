t = int(input("Digite uma tabuada: "))
i = 1
aux = 1

while aux <= t:
    if i <= aux:
        print(f'\t\t\t#### Tabuada do {i} ####')
        n = 0
        while n <= 10:
            print(f'{i} x {n} = {i * n}')
            n += 1
    i += 1
    aux += 1
