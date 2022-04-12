

plik = open("liczby.txt","r")
dane = plik.readlines()


max = int(dane[0].strip(),2)
for line in dane:
    line = int(line.strip(),2)
    if line > max:
        max = line
print(f"największa liczna  {max} - 10 system, {bin(max)[2:]} - 2 system")
