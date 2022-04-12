sz = open("sz.txt","r")
klucze2 = open("klucze2.txt","r")

sz = sz.readlines()
klucze2 = klucze2.readlines()

tab = [chr(x) for x in range(65,91)]
print(tab)

for wyraz, klucz in zip(sz,klucze2):
    wyraz = wyraz.strip()
    klucz = klucz.strip()

    klucz = klucz*len(wyraz)

    nowe = ""
    for i,k in zip(wyraz,klucz):
        suma = ord(i)-(tab.index(k)+1)
        if suma < 65:
            suma = suma + 26
        nowe = nowe + chr(suma)
    print(nowe)