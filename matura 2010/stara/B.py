plik = open("anagram.txt")
dane = plik.readlines()

for line in dane:
    wyrazy = line.split()

    if sorted(wyrazy[0]) == sorted(wyrazy[1]) == sorted(wyrazy[2]) == sorted(wyrazy[3]) == sorted(wyrazy[4]):
        print(*wyrazy)


plik.close()