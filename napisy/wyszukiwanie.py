def wyszukaj_naiwnie(sprawdzamy, szukamy):
    for i in range(len(sprawdzamy) - len(szukamy) + 1):
        if sprawdzamy[i:i + len(szukamy)] == szukamy:
            return i
    return None

if __name__ == '__main__':
    sprawdzamy = "ala ma kota"
    szukamy = "ko"
    print(wyszukaj_naiwnie(sprawdzamy, szukamy))


