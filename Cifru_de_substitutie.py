"""
    Problema 11-E1 – Cifru de substituţie
    
Una din cele mai vechi metode de a cripta informaţia este printr-un cifru de substituţie.
Acest cifru se realizează prin înlocuirea fiecărui caracter din textul de intrare cu alt caracter.
"""
# Cerinta
"""
    Dându-se un text de intrare şi un tabel de substituţie, să se scrie un program care să cripteze textul
de intrare.

    Date de intrare
Pe prima linie citită de la tastatură (stream-ul stdin) se află textul de intrare. Pe următoarea linie se
află perechi de câte două caractere: caracterul din textul de intrare şi caracterul cu care acesta
trebuie înlocuit. Cele două caractere sunt separate prin virgulă şi perechile sunt separate prin spaţiu.
Doar literele mici (26), literele mari (26) şi cifrele (10) se vor înlocui în text, în total tabelul de
substituţie are deci 62 de elemente. Lungimea maximă a textului este de 1000 de caractere. Ambele
linii se termină cu apăsarea tastei Enter (caracterul newline, \n).

    Date de ieşire
Programul va afişa pe ecran (stream-ul standard de ieşire), pe o singură linie, textul criptat. Din
textul de intrare se vor înlocui doar literele mici şi mari şi cifrele, restul caracterelor rămânând
nemodificate. Linia se termină obligatoriu cu caracterul newline (\n).
"""

# Rezolvare

text = input("Textul este: ")
perechi = input("Inlocuim: ")
perechi = perechi.split()

for x in text:
    for i in perechi:
        if x == i[0]:                             #i[0] este litera ce trebuie inlocuita
            text = text.replace( x, i[2] )        #i[2] este litera cu care se inlocuieste

# i[1] este virgula ce delimiteaza caracterul din text si caracterul cu care trebuie inlocuit

print(text)
