plik = open("napis.txt", "r")
dane = plik.readlines()


def rosnacy(napis):

    for i in range(1,len(napis)):
        if napis[i-1] > napis[i]:
            return False
    return True





licznik = 0
for line in dane:

    line = line.strip()

    if rosnacy(line):
        print(line)
print(f"w pliku jest {licznik} napisów rosnących")