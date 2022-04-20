plik = open("dane.txt","r")
dane = plik.readlines()

licznik = 0
for line in dane:
    liczba = str(int(line.strip(),8))
    if liczba[0] == liczba[-1]:
        licznik += 1

print(licznik)