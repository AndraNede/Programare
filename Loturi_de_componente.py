"""
Problema 2018.1.3 – Loturi de componente electronice

Sunteți șef de proiect la o companie și l-ați rugat pe Gigel să dea comandă de loturi de componente
electronice pentru a realiza un set de plăci cu circuite electronice. Problema este că Gigel nu știe
prea multă electronică așa că printre loturile pe care le-a comandat sunt și loturi cu tranzistoare
condensatoare sau rezistoare insuficiente. Loturile care vă sunt utile sunt doar loturile care au un
număr de condensatoare mai mare sau egal cu numărul de tranzistoare, numărul de rezistoare mai mare
sau egal cu numărul de condensatoare, și au cel puțin un condensator, un tranzistor și un rezistor.
În plus, vă interesează și lotul cu cele mai multe componente, pentru că din ele o să le mai
completați pe cele lipsă.
"""
# Cerință
"""
Scrieți un program care primește la intrare loturile de componente și afișează
câte dintre aceste loturi vă sunt utile și câte componente are lotul cel mai mare.
Un lot se consideră util dacă respectă condițiile impuse mai sus.
Aceste condiții trebuie îndeplinite simultan.

        Date de intrare

Se va citi de la tastatură (fluxul stdin) pe o singură linie un număr întreg n
reprezentând numărul de loturi. Apoi, se vor citi cele n loturi după cum urmează:
se citește pe o linie numărul de componente din lotul respectiv, k,
iar pe următoarea linie k litere reprezentând tipurile de componente ale lotului,
separate prin spatii (R reprezentând un rezistor, C reprezentând un condensator și T
reprezentând un tranzistor).

        Date de ieșire

Programul va afișa pe ecran (stream-ul standard de iesire) două numere întregi,
reprezentând numărul de loturi utile dintre cele citite cât și numărul de componente ale
lotului cel mai mare, valori separate printr-un spațiu.
"""
# Rezolvare

n = int(input("Nr. loturi: "))
loturi = []
#x = -1
marime_lot = 0
t = 0

for i in range(n):
    
    nr_comp = int(input("Nr. componente: "))
    comp = input("Componente: ")
    
    loturi.append(comp.upper().split(" "))
    
#print(loturi)

for j in range(len(loturi)):
    
    #if ( ('C' in loturi[j]) >= ('T' in loturi[j]) ) and ( ('R' in loturi[j]) >= ('C' in loturi[j]) ) and ( ('C' in loturi[j]) >= 1  ) and ( ('T' in loturi[j]) >= 1 ) and ( ('R' in loturi[j]) >= 1 ):
        #x += 1
    # nu stiu daca aceasta metoda de verificare este buna, dar rezultatul afisat este cel corect ca in cazul instructiunii de mai jos
        
    if loturi[j].count('C') >= loturi[j].count('T') and loturi[j].count('R') >= loturi[j].count('C') and loturi[j].count('C') >= 1 and loturi[j].count('T') >= 1 and loturi[j].count('R') >= 1:
        t += 1
      
    if marime_lot < len(loturi[j]):
        marime_lot = len(loturi[j])
            
print(t, marime_lot)

# print(x, marime_lot)









