

plik = open("liczby.txt","r")
dane = plik.readlines()


licznik = 0
for line in dane:
    line = int(line.strip(),2)
    if line % 2 == 0:
        licznik += 1
print(f"liczba liczb parzystych w pliku {licznik}")
