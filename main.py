from datetime import date

kolegij ={}
ispit = {}
student = {}
ime_kolegija = input("Unesite ime kolegija:")
ects_bodovi = int(input("Unesite brioj ECTS bodova:"))
kolegij[ime_kolegija.upper()] = ects_bodovi

godina = int(input("Unesite godinu ispita:"))
mjesec = int(input("Unesite mjesec ispita:"))
dan = int(input("Unesite dan ispita:"))
datum_ispita = date(godina, mjesec, dan)

ispit["kolegij"] = kolegij
ispit ["datum"] = datum_ispita

ime = input("Unesite ime studenta:").capitalize()
prezime = input("Unesite prezime studenta:").capitalize()
student["ispit"] =ispit
student["ime"] = ime
student["prezime"] = prezime
print(" Kolegij",ime_kolegija,"nosi",ects_bodovi,"bodova")
print("Datum ispita je:", datum_ispita)

print("Student",ime,prezime," je prijavio ispit iz kolegija",ime_kolegija,"koji će se održati:",datum_ispita)


