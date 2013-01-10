#Tree -> () ->
#    width = 960
#    height = 800
#
#    tree = (selection, data) ->
#        #main implementation
#        
#    update = () ->
#        # private function
#    
#    network.toggleLayout = (newLayout) ->
#        # public function
#
#    return tree

class Value
    constructor: (@stringRep, @isTerminal) ->


class Node
    @leaves: []
    @S_ = new Value "S", false
    @a = new Value "a", true
    @b = new Value "b", true
    @eps = new Value "", true
    @production = [[@a], [@b], [@eps], [@a,@S_,@a], [@b,@S_,@b]]

    constructor: (@values) ->
        @children = []
        @depth = 0
        # Append this object to the leaves.
        Node.leaves.push this

    expand: () ->
        #For every index and value in own values
        for v,idx in @values
            # If we run across a nonterminal, want to replace with production.
            if not v.isTerminal
                # When you expand (not terminal!) you remove self from leaves.
                myIdx = Node.leaves.indexOf(this)
                Node.leaves.splice(myIdx, 1)
                # For every element in the production (i.e., everything the nonterminal
                # can be replaced with), want to add a new node and add it to this Node's
                # children.
                for p in Node.production #TODO: Need to add production.
                    # Temporary values, shallow copy.
                    tempValues = @values[..]
                    #before = tempValues[0...idx]
                    #after = tempValues[idx+1..]
                    # List flattening
                    tempValues[idx] = p 
                    tempValues = [].concat tempValues...

                    @children.push new Node tempValues

                
