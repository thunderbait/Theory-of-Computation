#C1615525
#Sotiris Hadjipanayi

import queue
from DFA import class_DFA

def listdfa(filename):
    with open(filename) as file:
        stateSz = int(read(file))
        s={}
        
        for i in strip_replace(file):
            s[i] = []
        alphabSz = int(read(file))
        a = []
       
        for i in strip_replace(file):
            a.append(i)
       
        for key in s:
            
            t = strip_replace(file)
            
            for k in t:
                s[key].append(k)
        
        initstate = read(file)
        cntfinal = int(read(file))
        finalst = []

        for i in strip_replace(file):
            finalst.append(i)
        dfa = class_DFA(s, a, finalst, initstate);

        return dfa

def DFAintersections(dfa_1, dfa_2):

    statesupd = {}

    for i, val in dfa_1.states.items():
        for j, val  in dfa_2.states.items():
            statesupd[i+j] = [(dfa_1.states[i][0],dfa_2.states[j][0])]
            statesupd[i+j].append((dfa_1.states[i][1],dfa_2.states[j][1]))
    finalst = []
    for a in dfa_1.finalst:
        for b in dfa_2.finalst:
            finalst.append(a+b)
    initstate = dfa_1.initstate + dfa_2.initstate
    new_dfa = class_DFA(statesupd, dfa_1.alphabet, finalst, initstate)
    return new_dfa

def read(file):

    return file.readline().strip()

def strip_replace(file):
    
    return read(file).replace(" ", "")

dfa_1 = listdfa(input("Select first DFA: "))
#print("dfa 1")
dfa_2 = listdfa(input("Select second DFA: "))
#print("dfa 2")
inter = DFAintersections(dfa_1, dfa_2)
print("Intersection: ") #INTERSECTION OF SELECTED DFAS
inter.display_dfa()

# End of Task 2