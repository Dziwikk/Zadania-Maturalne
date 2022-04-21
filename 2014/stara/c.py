plik = open("napis.txt", "r")
dane = plik.readlines()




unikatowe = []
wszystkie = []

for line in dane:

    line = line.strip()
    unikatowe.append(line)
    wszystkie.append(line)

unikatowe = list(set(unikatowe))



x = dict()

for napis in unikatowe:
    x[napis] = wszystkie.count(napis)

for wyraz in x.keys():
    if x[wyraz] > 1:
        print(wyraz)
