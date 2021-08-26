def from_camel_case(name):
    words = []
    for ch in name:
        if ch.isupper():
            words.append(ch.lower())
        else:
            words[-1] += ch
    return '_'.join(words)

# import re
#
# def from_CamelCase(name):
#     return '_'.join(re.findall('([A-Z][^A-Z]*)', name)).lower()


if __name__ == '__main__':
    print("Example:")
    print(from_camel_case("Name"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
    print("Coding complete? Click 'Check' to earn cool rewards!")
