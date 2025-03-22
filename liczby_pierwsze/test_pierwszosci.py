def czy_pierwsza(liczba : int):

    for i in range(2, int(liczba ** 0,5)):
        if liczba % i == 0:
            return False
    return True

if __name__ == '__main__':
    liczba = int(input())
    wynik = czy_pierwsza(liczba)
    print(wynik)

