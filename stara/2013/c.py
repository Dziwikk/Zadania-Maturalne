plik = open("dane.txt","r")
dane = plik.readlines()

def sprawdz(liczba):
    liczba = str(liczba)
    for i in range(1,len(liczba)):
        if liczba[i] < liczba[i-1]:
            return False
    return True


max = 0
min = int(dane[0].strip(),8)
licznik = 0
for line in dane:
    liczba = line.strip()
    if sprawdz(liczba):
       licznik += 1
       if max < int(liczba,8):
           max = int(liczba,8)
       if min > int(liczba,8):
           min = int(liczba,8)
print(licznik)
print(oct(max))
print(oct(min))
