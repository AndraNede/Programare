"""
Problema 2018.3.1 - Zaruri

    Costică e în vacanță și l-au trimis părinții la țară. Acolo se plictisește groaznic și căutând prin dulapul
bunicului, a dat peste o pungă plină ochi cu zaruri. Neavând cu cine să joace zaruri, Costică s-a apucat
să le clădească, unul peste celălalt, cât de sus a putut. Uitându-se apoi la isprava făcută, i-a venit ideea
să afle care sunt numerele zarurilor de pe fețele acestora care nu se văd. Dându-și seama că deși e
posibil, e mai complicat, și că el e mai degrabă leneș decât curios, s-a hotărât să afle doar suma tuturor
numerelor de pe toate fețele zarurilor care nu se văd.
"""
# Cerinţă
"""
    Dându-se un număr N de zaruri și valorile de pe fețele vizibile ale zarurilor, calculați suma tuturor
fețelor care nu se văd. Se ignoră ordinea reală a numerelor pe fețele zarurilor, adică cele 6 numere
pot apărea pe zar în orice aranjament.

Date de intrare

    De la intrare (fluxul stdin) de pe prima linie se citește numărul natural N, reprezentând numărul de
zaruri suprapuse. Pe cea de-a doua linie se află 5 numere naturale distincte în intervalul [1; 6]
reprezentând cele 5 fețe vizibile pentru zarul de sus, apoi pe următoarele N-1 linii se află 4 numere
de același fel, reprezentând cele 4 fețe vizibile ale zarurilor.

Date de ieşire

    La ieşire (fluxul stdout) se va afișa un singur număr întreg pozitiv ce reprezintă suma fețelor invizibile
ale zarurilor.
"""

N = int(input("Nr. zaruri suprapuse = "))
zaruri = []

for i in range(N):
    zaruri.append( input("Fetele vazute = ").split(",") )

# suma initiala a zarurilor este 0:
suma = 0

# pentru fiecare zar si pentru toate fetele, daca cifra nu se vede se adauga la suma

for x in zaruri: 
    for j in range(1,6): 
        if str(j) not in x: 
            suma += j  
            
print(suma)

## test
##
