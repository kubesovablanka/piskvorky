from random import randrange
from util import tah


def tah_pocitace(pole, symbol):
    pozice = 30
    while True:
        if 'xx' in pole:
            if pole[pole.index('xx') + 1] == '-':
                pozice = pole.index('xx') + 1
            elif pole[pole.index('xx') - 1] == '-':
                pozice = pole.index('xx') - 1
            elif pole[pole.index('xx') + 2] == '-':
                pozice = pole.index('xx') + 2
            elif pole[pole.index('xx') - 2] == '-':
                pozice = pole.index('xx') - 2

        elif 'oo' in pole:
            if pole.index('oo') == 18:
                if pole[pole.index('oo') - 1] == '-':
                    pozice = 17
            elif pole[pole.index('oo') + 1] == '-':
                pozice = pole.index('oo') + 1
            elif pole[pole.index('oo') - 1] == '-':
                pozice = pole.index('oo') - 1
            elif pole[pole.index('oo') + 2] == '-':
                pozice = pole.index('oo') + 2
            elif pole[pole.index('oo') - 2] == '-':
                pozice = pole.index('oo') - 2

        elif 'o' in pole:
            if pole.index('o') == 19:
                if pole[pole.index('o') - 1] == '-':
                    pozice = 18
            elif pole[pole.index('o') + 1] == '-':
                pozice = pole.index('o') + 1
            elif pole[pole.index('o') - 1] == '-':
                pozice = pole.index('o') - 1
            elif pole[pole.index('o') + 2] == '-':
                pozice = pole.index('o') + 2
            elif pole[pole.index('o') - 2] == '-':
                pozice = pole.index('o') - 2

        elif 'o' in pole:
            if pole[pole.index('o', ((pole.index('o'))+1)) + 1] == '-':
                pozice = pole.index('o') + 1
            elif pole[pole.index('o', ((pole.index('o'))+1)) - 1] == '-':
                pozice = pole.index('o') - 1
            elif pole[pole.index('o', ((pole.index('o'))+1)) + 2] == '-':
                pozice = pole.index('o') + 2
            elif pole[pole.index('o', ((pole.index('o'))+1)) - 2] == '-':
                pozice = pole.index('o') - 2

        elif 'x' in pole:
            if pole[pole.index('x') + 1] == '-':
                pozice = pole.index('x') + 1
            elif pole[pole.index('x') - 1] == '-':
                pozice = pole.index('x') - 1
            elif pole[pole.index('x') + 2] == '-':
                pozice = pole.index('x') + 2
            elif pole[pole.index('x') - 2] == '-':
                pozice = pole.index('x') - 2

        elif 'x' in pole:
            if pole[pole.index('x', (pole.index('x')+1)) + 1] == '-':
                pozice = pole.index('x') + 1
            elif pole[pole.index('x', (pole.index('x')+1)) - 1] == '-':
                pozice = pole.index('x') - 1
            elif pole[pole.index('x', (pole.index('x')+1)) + 2] == '-':
                pozice = pole.index('x') + 2
            elif pole[pole.index('x', (pole.index('x')+1)) - 2] == '-':
                pozice = pole.index('x') - 2

        else:
            pozice = randrange(20)
            if pole[pozice] == '-':
                return tah(pole, pozice, symbol)

        if pozice <= 19:
            return tah(pole, pozice, symbol)
        else:
            continue
