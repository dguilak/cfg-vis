# Trying to implement a context-free grammar in Python.
# Author: DBG

#Temporary for testing (global values):
S_ = Value("S", False)
a = Value("a", True)
b = Value("b", True)

#Temporary production (not allowing empty string yet)
production = [[a], [b], [a, S_, a], [b, S_, b]]

class Tree():
    "Controls the world"
    def __init__(self):
        """Will eventually have more to say than just this."""
        # self.root from start variable of production.
        self.root = Node([S_])
        self.root.__expand__()

class Node():
    "Nodes that make up the tree"
    def __init__(self, values):
        """Constructor for Node -- should take list of values"""
        self.values = values
        self.children = []

    def __expand__(self):
        """expand goes through values and expands the ones that are nonterminals by productions."""
        # Will want to use for i = 0; i < length; i++
        for v in self.values:
            # If we run across a nonterminal, want to replace it with the production.
            # Need to figure out how to do this with lists.
            if not self.values.isTerminal:
                
                # This will need to change with more productions.
                # For every element in the production (i.e., everything the nonterminal can be
                # replaced with), want to add a new node and add it to this Node's children.
                for p in production:
                    

    def __str__(self):
        returnString = ""
        for i in self.values:
            returnString ++ i.__str__()
            

class Value():
    "A nonterminal or terminal"
    def __init__(self, stringRep, isTerminal):
        """String representation and whether or not it's a terminal"""
        self.stringRep = stringRep
        self.isTerminal = isTerminal

    def __str__(self):
        return stringRep
