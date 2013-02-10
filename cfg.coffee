class Value
    constructor: (@stringRep, @isTerminal) ->

class Link
    constructor: (@source, @target) ->

class CFGTree
    # For keeping track of id for nodes
    @numberNodes = 0
    @nodes: []
    @links: []
    @S_ = new Value "S", false
    @a = new Value "a", true
    @b = new Value "b", true
    @eps = new Value "", true
    # Right now this only does palindromes with two characters (a,b)
    @production = [[@a], [@b], [@eps], [@a,@S_,@a], [@b,@S_,@b]]

    constructor: (@values) ->
        @children = []
        @unique_id = CFGTree.numberNodes
        # Increment the number of nodes.
        CFGTree.numberNodes += 1
        # Append this object to the leaves.
        CFGTree.nodes.push this

    expand: () ->
        #For every index and value in own values
        for v,idx in @values
            # If we run across a nonterminal, want to replace with production.
            if not v.isTerminal
                # When you expand (not terminal!) you remove self from leaves.
                #myIdx = CFGTree.leaves.indexOf(this)
                #Node.leaves.splice(myIdx, 1)
                # For every element in the production (i.e., everything the nonterminal
                # can be replaced with), want to add a new node and add it to this Node's
                # children.
                for p in CFGTree.production #TODO: Need to add production.
                    # Temporary values, shallow copy.
                    tempValues = @values[..]
                    #before = tempValues[0...idx]
                    #after = tempValues[idx+1..]
                    # List flattening
                    tempValues[idx] = p
                    tempValues = [].concat tempValues...
                    tempNode = new CFGTree tempValues
                    @children.push tempNode
                    # Add link for nodes as well.
                    CFGTree.links.push new Link this,tempNode

