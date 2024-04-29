#algorytmy wyszukiwania wzorca
#algorytm boyera-moorea

def tabP(wr):
    m = len(wr)
    P = [m] * 256

    for i in range(m-1):
        P[ord(wr[i])] = m - 1 - i

    return P


def algorytmBM(txt, wr):
    n = len(txt)
    m = len(wr)

    P = tabP(wr)
    i = m - 1

    while i<n:
        k = 0
        while k<m and wr[m-1-k] == txt[i-k]:
            k+=1

        if k == m:
            return i-m+1

        i += max(1, P[ord(txt[i])])

    return -1


print(algorytmBM("ala ma kota i kiedys miala psa", "kot"))
print(algorytmBM("ala ma kota i kiedys miala psa", "pies"))