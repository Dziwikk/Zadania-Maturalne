plik = open("napis.txt", "r")
dane = plik.readlines()

def pierwsza(n):
    if n == 1:
        return True
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


licznik = 0
for line in dane:

    line = line.strip()
    suma = 0

    for x in line:
        suma += ord(x)
    if pierwsza(suma):
        licznik += 1
print(f"w pliku jest {licznik} napisów pierwszych")