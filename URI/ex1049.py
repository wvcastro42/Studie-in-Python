subfilo = input()
classe = input()
alimetacao = input()

if subfilo.lower() == 'vertebrado':
    if classe.lower() == 'ave':
        print(f'aguia' if alimetacao.lower() == 'carnivoro' else 'pomba')
    else:
        print(f'homem' if alimetacao.lower() == 'onivoro' else 'vaca')

if subfilo.lower() == 'invertebrado':
    if classe.lower() == 'inseto':
        print(f'pulga' if alimetacao.lower() == 'hematofago' else 'lagarta')
    else:
        print(f'sanguessuga' if alimetacao.lower() == 'hematofago' else 'minhoca')
