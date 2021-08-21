import re
CONSONANTS = 'bcdfghjklmnpqrstvwxz'
VOWELS = 'aeiouy'

def checkio(line: str) -> str:

    line = re.sub(r'[^\w\s]','',line.lower()).split(' ')

    for word in line:
        if word.isalpha():
            for idx, letter in enumerate(word):
                print(idx, letter)

                SE índice (a partir do primeiro) for vogal/consoante, verificando o índice %2 par/impar, se está em consoantes ou vogais

if __name__ == '__main__':
    print("Example:")
    print(checkio('My name is ...'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio('My name is ...') == 3
    assert checkio('Hello world') == 0
    assert checkio('A quantity of striped words.') == 1
    assert checkio('Dog,cat,mouse,bird.Human.') == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")
