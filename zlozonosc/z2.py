def przeksztalc_liste(liczby):
    for i in range(len(liczby)):
        if i % 2 == 0:
            liczby[i] = liczby[i] * 2
        else:
            liczby[i] = liczby[i] / 2
    return liczby

lista = [10, 20, 30, 40, 50, 60]
wynik = przeksztalc_liste(lista)
print(wynik)


o(n) = n