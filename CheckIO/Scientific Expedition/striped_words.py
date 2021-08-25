import re
CONSONANTS = 'bcdfghjklmnpqrstvwxz'
VOWELS = 'aeiouy'

def checkio(line: str) -> str:
    count = 0
    line = re.sub(r'[^\w\s]',' ',line.lower()).strip().split()

    for word in line:
        valida = True

        for current_item, next_item in zip(word, word[1::]):

            if valida and not (current_item in CONSONANTS and next_item in VOWELS or current_item in VOWELS and next_item in CONSONANTS):
                valida = False

        if valida and len(word) > 1:
            count += 1

    return count


if __name__ == '__main__':
    print("Example:")
    print(checkio('My name is ...'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio('My name is ...') == 3
    assert checkio('Hello world') == 0
    assert checkio('A quantity of striped words.') == 1
    assert checkio('Dog,cat,mouse,bird.Human.') == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")
