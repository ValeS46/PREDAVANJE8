ime = "Miha"

if ime == "Miha":
    print("Pozdravljen, Miha")
elif ime == "Franci":
    print("Zdravo, Franci!")
else:
    print("Pozdravljen, neznanec")

#Upošteva prvi pogoj, ki se uresniči. Print se zaključi.

#starost = int(input("Vpišite vašo starost: "))   -----> zapis kot integer
starost = 30
if starost > 25:
    print ("Star si več kot 25")
elif starost >= 18:
    print("Odrasel si!")
else:
    print ("Mlad si!")