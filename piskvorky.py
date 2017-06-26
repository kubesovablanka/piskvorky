from random import randrange
from util import tah
from ai import tah_pocitace



def vyhodnot(pole):
    if 'xxx' in pole:
        return('x')
    elif 'ooo' in pole:
        return('o')
    elif '-' not in pole:
        return('!')
    else:
        return('-')


def tah_hrace(pole):

    while True:
        try:
            pozice = int(input('Kam chces hrat?'))
        except ValueError:
            print('To nebylo číslo!')
        else:
            if pozice < 0:
                print('Zaporna policka nemam.')
            elif pozice >= len(pole):
                print('To je moc.')
            elif pole[pozice] != '-':
                print('Tam uz to nejde.')
            else:
                break
    return tah(pole, pozice, 'o')


def piskvorky1d():
    pole = '-' * 20

    while True:
        print(pole)
        pole = tah_hrace(pole)
        if vyhodnot(pole) != '-':
            break
        print(pole)
        pole = tah_pocitace(pole, 'x')
        if vyhodnot(pole) != '-':
            break

    print(pole)
    if vyhodnot(pole) == "!":
        print('Remiza')
    else:
        print('Vyhral hrac se znakem ', vyhodnot(pole))
