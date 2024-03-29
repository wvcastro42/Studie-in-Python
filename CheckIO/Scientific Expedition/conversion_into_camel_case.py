def to_camel_case(name: str) -> str:

    # return name.title().replace('_', '')

    # return ''.join([x.capitalize() for x in name.split('_')])

    camel_word = ''
    name = name.split('_')

    for word in name:
        camel_word += word[0].upper() + word[1:]

    return camel_word

print(to_camel_case('my_function_name'))

# if __name__ == '__main__':
#     print("Example:")
#     print(to_camel_case('name'))
#
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert to_camel_case("my_function_name") == "MyFunctionName"
#     assert to_camel_case("i_phone") == "IPhone"
#     assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
#     assert to_camel_case("name") == "Name"
#     print("Coding complete? Click 'Check' to earn cool rewards!")
