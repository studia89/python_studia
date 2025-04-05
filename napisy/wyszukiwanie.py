def wyszukaj_naiwnie(sprawdzamy, szukamy):
    for i in range(len(sprawdzamy) - len(szukamy) + 1):
        znaleziono = True
        for j in range (len(szukamy)):
            if not sprawdzamy[i+j] == szukamy[j]:
                znaleziono = False
                break
        if znaleziono:
            return i
    return None


if __name__ == '__main__':
    sprawdzamy = "ala ma kota"
    szukamy = "ko"
    print(wyszukaj_naiwnie(sprawdzamy, szukamy))



