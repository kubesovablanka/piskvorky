pole = '--------oo------o----'
pozice = 30



    #if pole[pole.index('o', ((pole.index('o'))+1)) + 1] == '-':
    #    pozice = pole.index('o', ((pole.index('o'))+1)) + 1
if 'oo' in pole:
    if pole[pole.index('oo') + 1] == '-':
        pozice = pole.index('oo') + 1
    #elif pole[pole.index('oo') - 1] == '-':
    #    pozice = pole.index('oo') - 1
    elif pole[pole.index('oo') + 2] == '-':
        pozice = pole.index('oo') + 2
    elif pole[pole.index('oo') - 2] == '-':
        pozice = pole.index('oo') - 2

print(pozice)
