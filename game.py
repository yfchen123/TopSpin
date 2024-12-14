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

def createPDB(numbers_to_check, size):
    number_of_numbers = len(numbers_to_check)
    pdb = dict()
    EntriesToBe = perm(size, number_of_numbers)#checks the current number of entries that are to exist once the PDB has finished being made.
    currentEntries = 0
    queue = q.Queue()
    queue.put(([*range(2, size+1)],[]))
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
            
            
            
        
    
    
    
    #print(pdb)
    #print (EntriesToBe)
    
