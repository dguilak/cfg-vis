# Trying to implement a context-free grammar in Python.
# Using Linked List implementation currently.
# Author: Daniel Guilak <daniel.guilak@gmail.com>
# http://danielguilak.com/


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
    # TODO: Eventually want to keep track of when a Node is all terminals, and not call
    # expand on it. 
    # This is klugy and delicious, but keeps track of all leaves in the Tree.
    leaves = []

    "Nodes that make up the tree"
    def __init__(self, values):
        """Constructor for Node -- should take list of values"""
        self.values = values
        self.children = []
        # Initial depth of tree.
        self.depth = 0
        # Append self to leaves.
        Node.leaves.append(self)
        

    def generateToN(self, n):
        """ Want to make it so it generates down to a specific depth n """
        # This currently is not working correctly -- don't think it's generating to a
        # specific depth, just generating a specific number of times.
        # For every i in n
        for i in range(n):
            # For every leaf, expand it!
            # Can't use for each loop because it modifies leaves
            for i in range(len(Node.leaves)):
                Node.leaves[i].__expand__()

    def __expand__(self):
        """expand goes through values and expands the ones that are nonterminals by productions."""
        for idx, v in enumerate(self.values):
            # If we run across a nonterminal, want to replace it with the production.
            if not v.isTerminal:
                # When you actually expand (not terminal!), you remove yourself from the leaves.
                Node.leaves.remove(self)
                # This will need to change with more productions.
                # For every element in the production (i.e., everything the nonterminal can be
                # replaced with), want to add a new node and add it to this Node's children.
                for p in production:
                    # Temporary values; shallow copy.
                    tempValues = self.values[:]
                    before = tempValues[:idx]
                    after = tempValues[idx+1:]
                    # Put it all back together again.
                    before.extend(p)
                    before.extend(after)

                    # Make new node and append it to the children.
                    self.children.append(Node(before))

    def __expandChildren__(self):
        """Expand all of your children. All of them."""
        for c in self.children:
            c.__expand__()

    def __str__(self):
        returnString = ""
        for i in self.values:
            returnString += i.__str__()

        return returnString

    def setValues(self, values):
        self.values = values 
            
