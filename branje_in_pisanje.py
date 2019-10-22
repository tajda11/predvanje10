datoteka = open("besedilo.txt")
vsebina_datoteke = datoteka.read()

print("To je vsebina datoteke:")
print("\"" + vsebina_datoteke + "\"")

datoteka.close()      #ni nujno zapreti, če bi pa imeli zanko pa bi morali

datoteka = open("besedilo.txt", "a")   #w = write, zamenja #a pa doda k staremu besedilu
datoteka.write("To je nova vsebina datoteke.\n")  #n - nova vrstica

datoteka.close()


