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

def morse_decoder(code):

    splited = code.split(' ')
    response = ''

    for letter in splited:
        if letter in MORSE:

            if letter != '':
                response = response + MORSE[letter]
        else:
            if response[-1] != ' ':
                response = response + ' '

    return response.capitalize()



print(morse_decoder("... --- -- .   - . -..- -"))


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
