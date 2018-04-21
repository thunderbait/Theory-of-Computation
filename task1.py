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

def read(file):

    return file.readline().strip()

def strip_replace(file):
    
    return read(file).replace(" ", "")

def DFAcomplement(dfa):
    finalst_new = []
    for i in dfa.states.keys():
        if i not in dfa.finalst:
            finalst_new.append(i)
    new_dfa = class_DFA(dfa.states, dfa.alphabet, finalst_new, dfa.initstate)
    return new_dfa
 
dfa_1 = listdfa(input("Select first DFA: "))
dfacomp_1 = DFAcomplement(dfa_1)
print("Complement of First DFA")
dfacomp_1.display_dfa()
dfa_2 = listdfa(input("Select second DFA: "))
dfacomp_2 = DFAcomplement(dfa_2)
print("Complement of second DFA")
dfacomp_2.display_dfa()


# End of Task 1