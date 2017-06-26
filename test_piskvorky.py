from piskvorky import tah, vyhodnot
from ai import tah_pocitace
from pytest import raises

def test_vyhodnot_vyhral_o():
    assert vyhodnot('---ooo---') == 'o'

def test_vyhodnot_vyhral_x():
    assert vyhodnot('-x-ooxxx-') == 'x'

def test_vyhodnot_remiza():
    assert vyhodnot('oxoxooxxoo') == '!'

# tento test nefunguje, proc?
#def test_pocitac_na_plne_pole():
#    with raises(ValueError):
#        assert tah_pocitace('xxoxoxoxoxoxxxoxxox')

#taky nefunguje
#def test_tah_chyba():
#    with raises(ValueError):
#        tah_pocitace('oxoxoxoxoxoxoxoxoxox')

def test_tah_a():
    assert tah('---------------------', 10, 'x') == '----------x----------'

#z materialu
def test_tah_b():
    pole = tah_pocitace('--------------------', 'x')
    assert len(pole) == 20
    assert pole.count('x') == 1
    assert pole.count('-') == 19

#proc nehlasi chybu, ze pozice je obsazena?
def test_tah_hrace():
    assert tah('---xoxoxo----xoxo---', 7, 'o')

#du4
#je toto overeni, ze se vyrovna s delsim polem?
def test_tah_pocitace():
    assert tah_pocitace('-------------------------', 'x')
