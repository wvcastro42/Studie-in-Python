import re
def checkio(text: str) -> str:
    text = filter(re.compile("[a-z]").match, text.lower())
    # text = text.lower().strip('.,?!')
    # text = ''.join(text.split(' '))
    # re
    numero_ocorrencias = [text.count(char) for char in text]

    set_zip = set(zip(text, numero_ocorrencias))

    z = sorted(set_zip, key=lambda indice: indice[1])
    # print(z[-1][0])
    return z[-1][0]

if __name__ == '__main__':
    # print("Example:")
    # print(checkio("Hello World!"))
    # #
    # # #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    # assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    # assert checkio("Oops!") == "o", "Don't forget about lower case."
    # assert checkio("AAaooo!!!!") == "a", "Only letters."
    # assert checkio("abe") == "a", "The First."
    # print("Start the long test")
    # assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    # print("The local tests are done.")
