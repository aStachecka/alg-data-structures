#algorytmy wyszukiwania wzorca
#algorytm naiwny

def aNaiwny(txt, wr):
    for letterIndex in range(len(txt)):
        if txt[letterIndex] == wr[0]:
            if txt[letterIndex:(letterIndex + len(wr))] == wr:
                return letterIndex

    return -1

print(aNaiwny("ala miala kiedys kota", "kot"))
print(aNaiwny("ala miala kiedys kota", "ma"))
