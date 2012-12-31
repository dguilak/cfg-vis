# Trying to implement a context-free grammar in Python.
# Author: DBG

"""
class Tree():
    "Controls the world"
    def __init__(self):
        # self.root from start variable of production.
        self.root = Node([S_])
        self.root.__expand__()
"""

class Value():
    "A nonterminal or terminal"
    def __init__(self, stringRep, isTerminal):
        """String representation and whether or not it's a terminal"""
        self.stringRep = stringRep
        self.isTerminal = isTerminal

    def __str__(self):
        return self.stringRep

#Temporary for testing (global values):
S_ = Value("S", False)
a = Value("a", True)
b = Value("b", True)
eps = Value("", True)

#Temporary production (not allowing empty string yet) -- palindrome
production = [[a], [b], [eps], [a, S_, a], [b, S_, b]]

class Node():
    "Nodes that make up the tree"
    def __init__(self, values):
        """Constructor for Node -- should take list of values"""
        self.values = values
        self.children = []
        # Initial depth of tree.
        self.depth = 0

    def generateToN(self, n):
        """ Want to make it so it generates down to a specific n """


    def __expand__(self):
        """expand goes through values and expands the ones that are nonterminals by productions."""
        for idx, v in enumerate(self.values):
            # If we run across a nonterminal, want to replace it with the production.
            if not v.isTerminal:
                # This will need to change with more productions.
                # For every element in the production (i.e., everything the nonterminal can be
                # replaced with), want to add a new node and add it to this Node's children.
                for p in production:
                    # Temporary values; shallow copy.
                    tempValues = self.values[:]
                    # Alex Martelli - Stack Overflow for flattening list
                    #tempProduction = [item for sublist in production for item in sublist]
                    before = tempValues[:idx]
                    after = tempValues[idx+1:]
                    # Put it all back together again.
                    before.extend(p)
                    before.extend(after)

                    # Make new node and append it to the children.
                    self.children.append(Node(before))

    def __str__(self):
        returnString = ""
        for i in self.values:
            returnString += i.__str__()

        return returnString

    def setValues(self, values):
        self.values = values 
            
