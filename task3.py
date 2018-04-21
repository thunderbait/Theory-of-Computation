#C1615525
#Sotiris Hadjipanayi

import queue
from DFA import class_DFA

def symmetric_diff(dfa_1, dfa_2):
    cdfa_1 = DFAcomplement(dfa_1)
    union1 = DFAintersections(cdfa_1, dfa_2)
    cdfa_2 = DFAcomplement(dfa_2)
    union2 = DFAintersections(dfa_1, cdfa_2)
    return DFAunion(union1,union2)

def DFAunion(dfa_1, dfa_2):
    cdfa_1 = DFAcomplement(dfa_1)
    cdfa_2 = DFAcomplement(dfa_2)
    dfainter = DFAintersections(cdfa_1, cdfa_2)
    cdfa_int = DFAcomplement(dfainter)
    return cdfa_int

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

def DFAcomplement(dfa):
    finalst_new = []
    for i in dfa.states.keys():
        if i not in dfa.finalst:
            finalst_new.append(i)
    new_dfa = class_DFA(dfa.states, dfa.alphabet, finalst_new, dfa.initstate)
    return new_dfa

dfa_1 = listdfa(input("Select first DFA: "))
#print("dfa 1")
dfa_2 = listdfa(input("Select second DFA: "))
#print("dfa 2")

sdiff = symmetric_diff(dfa_1, dfa_2)
print("Symmetric Difference") #SYMMETRIC DIFFERENCE OF SELECTED DFAS
sdiff.display_dfa()