def znajdz_sume(lista, cel):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == cel:
                return (i, j)
    return None

liczby = [2, 7, 11, 15]
print(znajdz_sume(liczby, 9))

o = n^2