"""
Procesor RISC

Pentru că echipa cu care lucrați a dezvoltat o nouă arhitectură de procesor RISC,
ați decis să-i ajutați în etapa de dezvoltare prin realizarea unui simulator software
pentru procesorul respectiv. Simulatorul va primi, ca și procesorul real, o secvență de
instrucțiuni care va trebui executată iar starea finală a datelor va trebui afișată la ieșire.
Procesorul are un set de 16 registre numerotate de la 0 la 15 și deocamdată nu are memorie.

Procesorul știe să execute următoarele instrucțiuni, pe care trebuie să le interpreteze și programul vostru:

• lconst <dst> <val> – se scrie valoarea <val> în registrul <dst>;
• add <dst> <src0> <src> – se adună valorile din registrele <src0> și <src1> și rezultatul se scrie în registrul <dst>;
• mul <dst> <src0> <src> – se înmulțesc valorile din registrele <src0> și <src1> și rezultatul se scrie în registrul <dst>;
• div <dst> <src0> <src> – se împart valorile din registrele <src0> și <src1> și câtul se scrie în registrul <dst>;
• print <reg> - se afișează valoarea din registrul <reg>.

Dacă la execuția unei instrucțiuni de tip div împărțitorul este zero, se va afișa fraza Exception: line <index>,
unde index reprezintă a câta instrucțiune nu a putut fi executată, iar programul se va încheia. Toate registrele au inițial valoarea 0.
"""
# Cerinţă
"""
Dându-se o secvență de instrucțiuni ca cele de mai sus, executați-le și afișați valorile printate de program.

        Date de intrare
Se va citi de la tastatură (fluxul standard de intrare, stdin) de pe prima linie un număr n, reprezentând numărul de instrucțiuni.
Pe următoarele n linii se află câte o instrucțiune din cele de mai sus.

        Date de ieşire
Programul va afişa la consolă (stream-ul standard de ieşire, stdout), valorile printate de program (prin instrucțiuni de tip print),
câte una pe linie.
"""
# Rezolvare

n = int(input("Nr. instructiuni: "))
instr = []
registre = []

for i in range(n):

    cmd = input("Instructinuni: ")
    instr.append(cmd.split(" "))

for x in range(16):
    registre.append(0)

# j = comanda

for j in instr:

    if j[0] == "lconst":
        registre[int(j[1])] = int(j[2])

    if j[0] == "add": 
        registre[int(j[1])] = registre[int(j[2])] + registre[int(j[3])]
        
    if j[0] == "mul":
        registre[int(j[1])] = registre[int(j[2])] * registre[int(j[3])]
        
    if j[0] == "div": 
        if registre[int(j[3])] == 0: 
            print("Exception: line " + str(i))

        else:
            registre[int(j[1])] = int(registre[int(j[2])] / registre[int(j[3])])
    
    if j[0] == "print":
        print(registre[int(j[1])])
