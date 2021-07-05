from typing import Union

def sun_angle(time: str) -> Union[int, str]:

    h, m = list(map(int, time.split(":")))
    angle = 15 * h + m / 4 - 90
    return angle if 0 <= angle <= 180 else "I don't see the sun!"
    # hora = int(time.split(':')[0])
    # minuto = int(time.split(':')[1])
    #
    # if hora < 6 or (hora >= 18 and minuto >= 1):
    #     return "I don't see the sun!"
    #
    # if hora == 6 and minuto == 0:
    #     return 0
    #
    # if hora == 18 and minuto == 0:
    #     return 180
    #
    # tempo = (((hora-6) * 60) + minuto)
    # grau = tempo * 0.25
    # return grau


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
