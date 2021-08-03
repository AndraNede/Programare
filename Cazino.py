"""
Problema 2018.1.5 - Cazino

Un faimos cazino din București dorește să detecteze mai rapid trișorii de la mesele lor de cărți.
Folosind un program de recunoaștere a imaginilor se pot detecta ce cărți sunt jucate de fiecare jucător de
la masă și se dorește să se descopere dacă vreunul din ei a scos cărți din buzunar.
Jocul monitorizat se joacă cu două pachete clasice (52 de cărți fiecare, fără Joker).
"""
# Cerință
"""
Scrieți un program care să ajute la detectarea trișorilor.
În cazul în care se detectează că o carte apare de prea multe ori, programul va afișa cartea și va opri jocul.

    Date de intrare
Se vor citi de la tastatură (fluxul stdin) următoarele date:
• Pe prima linie se află numărul n, reprezentând numărul maxim de mâini ce vor fi jucate;
• Pe următoarele n linii se află cartea jucată, în formatul:
<număr_carte> <semn_carte>

    Date de ieşire
În cazul în care nimeni nu încearcă să trișeze se va afișa textul JOC OK.
În cazul în care cineva a încercat sa trișeze, se va afișa cartea problemă în același format ca la intrare:
numărul cărții urmat de semn, separate prin spațiu.
"""

# Rezolvare

nr_maini = int(input("Numar maini: "))
carti = []
x = 0

for i in range(nr_maini):           # pentru fiecare numar de maini ce vor fi jucate
    
    cartea = input("Cartile sunt: ")                # se adauga nr cartii si semnul
    carti.append(cartea)                            # se adauga in lista

    if carti.count(carti[i]) > 2:           # daca o carte se afiseaza de mai mult de 3, afisez cartea
    
        x = i
        print(carti[x])
        
if x < i:                           # daca afisarea este mai mica de 3, este "joc ok"

    print("JOC OK")
