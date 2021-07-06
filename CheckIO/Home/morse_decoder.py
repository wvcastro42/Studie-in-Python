MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
        }
def spaces3(text):
    list_3spaces = []

    for i in range(len(text)):
        if text[i:i+3] == '   ':
            list_3spaces.append(i)
    return list_3spaces


def morse_decoder(code):

    list_text = code.replace('   ', ' ').split(' ')
    text = ''
    spaces = spaces3(code)

    for s in code:

        for i in list_text:
            if i in MORSE:
                print(i)
                text = text + MORSE[i]

    return text


print(morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--"))
print(spaces3(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--"))


#
# if __name__ == '__main__':
#     print("Example:")
#     print(morse_decoder('... --- ...'))
#
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
#     assert morse_decoder("..--- ----- .---- ---..") == "2018"
#     assert morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"
#     print("Coding complete? Click 'Check' to earn cool rewards!")
