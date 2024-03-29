def time_converter(time):

    if int(time.split(':')[0]) <= 12:
        if int(time.split(':')[0]) == 12:
            return (str(int(time.split(':')[0])) + ':' + time.split(':')[1] + ' p.m.')
        else:
            return (str(int(time.split(':')[0])) + ':' + time.split(':')[1] + ' a.m.')

    if int(time.split(':')[0]) > 12:
        return (str(int(time.split(':')[0])-12) + ':' + time.split(':')[1] + ' p.m.')


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
