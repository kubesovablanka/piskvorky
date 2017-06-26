def tah(pole, pozice, symbol):
    "Vrati herni pole s danym symbolem umistenym na danou pozici"

    return pole[:pozice] + symbol + pole[pozice + 1:]
