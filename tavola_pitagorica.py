#tavola pitagorica in python 

for riga in range(1, 13):
    for colonna in range(1, 13):
        print("%5d" % (riga * colonna,), end ='')
    print("")

#ps che arriva fino a 12 non è che cambi poi più di tanto
#istruzione che indica l'ultimo carattere 