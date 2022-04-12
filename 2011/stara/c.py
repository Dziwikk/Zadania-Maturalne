
plik = open("liczby.txt","r")
dane = plik.readlines()

suma = 0

for line in dane:
    line = line.strip()
    if len(line) == 9:
        suma += int(line,2)

print(f"suma liczba w systemie 2: {bin(suma)[2:]}")