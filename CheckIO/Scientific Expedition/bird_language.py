VOWELS = "aeiouy"
def translate(text: str) -> str:

    human_phrase = []
    i = 0

    while i < len(text):

        human_phrase.append(text[i])

        if text[i] in VOWELS:
            i += 3
        elif text[i] == ' ':
            i += 1
        else:
            i += 2

    return ''.join(human_phrase)

if __name__ == "__main__":
    # print("Example:")
    # print(translate("hieeelalaooo"))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert translate("hieeelalaooo") == "hello"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
    # assert translate("aaa bo cy da eee fe") == "a b c d e f"
    # assert translate("sooooso aaaaaaaaa") == "sos aaa"
    print("Coding complete? Click 'Check' to earn cool rewards!")
