#algorytmy wyszukiwania wzorca
#algorytm knutha-morrisa-pratta

def tabP(wr):
    P = [0] * len(wr)
    i = 0

    for j in range(1, len(wr)):
        while i > 0 and wr[i] != wr[j]:
            i = P[i - 1]
        if wr[i] == wr[j]:
            i += 1
        P[j] = i

    return P


def algorytmKMP(txt, wr):
    P = tabP(wr)
    i = 0
    j = 0

    n = len(txt)
    m = len(wr)

    while i < n:
        if wr[j] == txt[i]:
            i += 1
            j += 1

            if j == m:
                return i - j
        else:
            if j != 0:
                j = P[j-1]
            else:
                i += 1

    return -1


print(algorytmKMP("ala miala kiedys malego kota", "ala"))
print(algorytmKMP("ala miala kiedys malego kota", "ania"))