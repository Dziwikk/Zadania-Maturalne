plik = open("anagram.txt")
dane = plik.readlines()

for line in dane:
    wyrazy = line.split()

    if len(wyrazy[0]) == len(wyrazy[1]) == len(wyrazy[2]) == len(wyrazy[3]) == len(wyrazy[4]):
        print(*wyrazy)


plik.close()