def yaml(a):

    dict_a = {}
    a.strip()
    text = a.replace('\n', ':').strip().split(":")

    text = [x for x in text if x]

    for word in text[::2]:
        if text[text.index(word)+1].strip().isnumeric():
            dict_a[word] = int(text[text.index(word)+1].strip())
        else:
            dict_a[word] = text[text.index(word)+1].strip()

    return dict_a

if __name__ == '__main__':
    print("Example:")
    print(yaml("""name: Alex
age: 12"""))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml("""name: Alex
age: 12""") == {'age': 12, 'name': 'Alex'}

    assert yaml("""name: Alex Fox
age: 12
class: 12b""") == {'age': 12,
 'class': '12b',
 'name': 'Alex Fox'}

    print("Coding complete? Click 'Check' to earn cool rewards!")
