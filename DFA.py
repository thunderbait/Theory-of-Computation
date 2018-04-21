class class_DFA:
    states = ()
    alphabet = []
    finalst = []
    initstate = ""

    def __init__(self, states, alphabet, finalst, initstate):
        self.states = states
        self.alphabet = alphabet
        self.finalst = finalst
        self.initstate = initstate

    def display_dfa(self):
        print("states: ", self.states, '\n',"alphabet: ", self.alphabet, '\n', "final states:", self.finalst, '\n', "start state: ", self.initstate)

