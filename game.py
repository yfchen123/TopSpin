import numpy as np
from math import perm
import queue as q

class game:
    board_state = [];
    N = 0;
    K = 0;
    
    def __init__(self, board_state, K = 4):
        self.N = len(board_state)
        self.K = K
        self.board_state = board_state


###
#Takes in a list of numbers and produces a pdb lookup table with instructions on how to move the given numbers to their correct position in the identity list in the best moves
#performs a breadth first search to and checks if its current formation is in the PDB or not. If it isn't it will add its current path to the table, then create offspring.
#if it already in the matrix then the branch is pruned and will not create children.
# 1 is considered the first point no matter what
#numbers_to_check: a list of the numbers that will be checked for the pdb
#size: number value for size of spinner

def createPDB(pdb_numbers, N, K):
    number_of_numbers = len(pdb_numbers)
    pdb = dict()
    EntriesToBe = perm(N, number_of_numbers)#checks the current number of entries that are to exist once the PDB has finished being made.
    currentEntries = 0
    queue = q.Queue()
    queue.put(([*range(2, N+1)],[]))
    #perfrom Breadth first search
    while currentEntries < EntriesToBe:
        (current, path) = queue.get()
        pdbIndex = []
        for num in number_of_numbers:#gets the current location in the state where each of the elements to find are
            pdbIndex.append(current.index(num)+1)
        if not pdbIndex in pdb:#if the entry does not yet exist in the pdb
            pdb[pdbIndex] = path
            currentEntries += 1
            #TODO create children
            #
            #create children that need to wrap around.
            
            for i in range(2, N - K+2):
                queue.put((insideRotate(current, i, K)),path+[i])
            #Create children that don't need to wrap around
#returns a list representing a state with a single slip starting with the position at index as the left most in the flip
#takes a list state [], 
#the index is the left most position in the range to be flipped. (the first index in the list would be at index value 2)
#k is the number of pegs to be flipped
#assumes it has been fed values that do not break the rule
def insideRotate(list, index, k):
    if (index <= 1 or index+k-2 > len(list)):
        raise Exception("Improper index, not an inside rotate")
    ret = list[:index-2]
    temp = list[index-2:index-2+k]
    temp.reverse()
    ret.extend(temp)
    ret.extend(list[index-2+k:])
    return ret
#def outsideRotate(list, index, k)
                
            
        
    
    
    
    #print(pdb)
    #print (EntriesToBe)
    
