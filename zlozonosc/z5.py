ane = [1, 6, 5, 8, 2]
def sortuj_babelkowo(dane):
    n = len(dane)

n = len(dane)
    for i in range(n-1):
        for j in range(n-1-i):
            if dane[j] > dane[j+1]:
                dane[j], dane[j+1] = dane[j+1], dane[j]

# o(n) = n^2