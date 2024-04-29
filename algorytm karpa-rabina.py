#algorytmy wyszukiwania wzorca
#algorytm karpa-rabina

def fHasz(s):
    prime = 101
    value = 0

    for char in s:
        value = (value * prime + ord(char)) % 256

    return value


def algorytmKR(txt, wr):
    prime = 101
    n = len(txt)
    m = len(wr)
    wrHasz = fHasz(wr)
    txtHasz = fHasz(txt[:m])

    for i in range(n - m + 1):
        if wrHasz == txtHasz and wr == txt[i:i + m]:
            return i
        if i < n - m:
            txtHasz = (txtHasz - ord(txt[i]) * pow(prime, m - 1, 256)) % 256
            txtHasz = (txtHasz * prime + ord(txt[i + m])) % 256

    return -1


print(algorytmKR("ala ma nowego duzego kota", "ma"))