def check_inline(line, word):
    return word in line

def check_vertical(lines, word, line_idx, letra_idx):
    encontrei = True

    for item_idx, letter in enumerate(word):

        if encontrei and not letter == (lines[line_idx + item_idx])[letra_idx]:
            encontrei = False

    return encontrei

def checkio(text, word):
    text = text.replace(' ', '').upper()
    word = word.upper()
    lines = text.split('\n')

    result = []

    for line_idx, line in enumerate(lines):
        for letra_idx, letra in enumerate(line):
            if letra == word[0]:
                if check_inline(line, word):
                    return [line_idx+1, line.find(letra)+1, line_idx+1, line.find(letra) + len(word)]
                elif check_vertical(lines, word, line_idx, letra_idx):
                    return [line_idx+1, letra_idx+1, line_idx + len(word), letra_idx+1]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
print("Coding complete? Click 'Check' to earn cool rewards!")
