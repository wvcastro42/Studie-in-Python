def from_camel_case(name: str) -> str:

    camel_word = ''

    for current_item, next_item in zip(name, name[1:]):

        if not camel_word:
            if next_item.isupper():
                camel_word = current_item.lower() + '_'
            else:
                camel_word = current_item.lower()

        elif current_item.isupper() and next_item.isupper():
            print(current_item.isupper() and next_item.isupper())
            camel_word += current_item.lower() + '_'

        elif current_item.islower() and next_item.isupper():
            camel_word += current_item.lower() + "_"

        else:
            camel_word += current_item.lower()

    return camel_word + name[-1].lower()
# print(from_camel_case("MFunctionName"))
if __name__ == '__main__':
    print("Example:")
    print(from_camel_case("Name"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
    print("Coding complete? Click 'Check' to earn cool rewards!")
