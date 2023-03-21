from datetime import date

kolegij ={}
ispit = {}

ime_kolegija = input("Unesite ime kolegija:")
ects_bodovi = int(input("Unesite brioj ECTS bodova:"))
kolegij[ime_kolegija.upper()] = ects_bodovi

godina = int(input("Unesite godinu ispita:"))
mjesec = int(input("Unesite mjesec ispita:"))
dan = int(input("Unesite dan ispita:"))
datum_ispita = date(godina, mjesec, dan)

ispit["kolegij"] = kolegij
ispit ["datum"] = datum_ispita

print(" Kolegij",ime_kolegija,"nosi",ects_bodovi,"bodova")
print("Datum ispita je:", datum_ispita)



