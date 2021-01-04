Kontakty = {
"Wujek Adi" : 111111111,
"Wujek Józek" : 222222222,
"Konon" : 333333333,
"Major" : 444444444,
"Albrecht von Hohenzollern" : 555555555,
"Ladislaus Postumus von Habsburg" : 666666666,
"Eduardo de Trastamara" : 777777777,
"Henry V Lancaster" : 888888888,
"Dominic von Wittelsbach" : 999999999,
"Kijanu" : 000000000,
}

Kontakty["Wujek Adik"] = Kontakty.pop("Wujek Adi")
Kontakty["Kijanu Rifs"] = Kontakty.pop("Kijanu")

Kontakty.pop("Albrecht von Hohenzollern")
Kontakty.pop("Ladislaus Postumus von Habsburg")

for kontakt, nr in Kontakty.items():
    print(kontakt, nr)