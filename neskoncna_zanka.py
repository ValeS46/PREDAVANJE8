# 2pogoja da prenehamo telo zanke, da je pogoj izpolnjen ali da vstavimo break
stevilka = 1
#dokler drži da je res
while True:
    # ustavi ko je enkrat številka večja od 10
    if stevilka > 1000000:
        break
    print(stevilka)
    stevilka = stevilka * 2

print("Konec programa!")