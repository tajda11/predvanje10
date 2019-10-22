import random

skrito_stevilo = random.randint(1,100)   #vrže številko

with open("tocke.txt") as datoteka:
    stari_stevec = int(datoteka.read())

print("Prejšnje število poizkusov je bilo:" + str(stari_stevec))

stevec = 0
while True:
    vneseno_stevilo = int(input("Ugani stevilo:"))  #string
    stevec += 1                # za stevec bi lahko uporabili tudi i

    if vneseno_stevilo == skrito_stevilo:
        print("Cestitke, uganili ste pravo število")
        break
    elif vneseno_stevilo > skrito_stevilo:
        print("Vpisali ste preveliko stevilo")
    #če ne velja 1 in 2 pogoj, potem pa se ta:

    else:
        print("Vpisali ste premajhno število")

print("Število poizkusov je bilo:" + str(stevec))

if stevec < stari_stevec:
    with open("tocke.txt", "w") as datoteka:
        datoteka.write (str(stevec))

print("Konec programa")