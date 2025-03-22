dane = [1, 6, 8, 5, 3, 4, 2]
n = len(dane)

for i in range (1, n):
    czerwony = dane [i]
    for j in range (0,i):
        if czerwony < dane[j]:
            dane.pop(i)
            dane.insert (j, czerwony)
            break
print(dane)