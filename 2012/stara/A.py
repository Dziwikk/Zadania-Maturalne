tj = open("tj.txt","r")
klucze1 = open("klucze1.txt","r")

tj = tj.readlines()
klucze1 = klucze1.readlines()

tab = [chr(x) for x in range(65,91)]
print(tab)

for wyraz, klucz in zip(tj,klucze1):
    wyraz = wyraz.strip()
    klucz = klucz.strip()

    klucz = klucz*len(wyraz)

    nowe = ""
    for i,k in zip(wyraz,klucz):
        suma = ord(i)+tab.index(k)+1
        if suma > 90:
            suma = suma - 26
        nowe = nowe + chr(suma)
    print(nowe)