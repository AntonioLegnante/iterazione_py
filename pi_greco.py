#calcolo del pigreco

termini = int(input("inserisci il numero di termini da usare"))
while termini < 0:
    termini = int(input("inserisci il numero di termini da usare"))
numeratore = -4.
pigreco = 4.
cont = 3.

for i in range(1, termini):
    pigreco += numeratore / cont
    numeratore = - numeratore
    cont += 2.

print(pigreco)
    