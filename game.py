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
    dimensions = (size,) *number_of_numbers
    pdb = np.zeros(dimensions)
    EntriesToBe = perm(size, number_of_numbers)#checks the current number of entries that are to exist once the PDB has finished being made.
    currentEntries = 0
    queue = q.Queue()
    queue.put()
    #perfrom Breadth first search
    
    
    
    #print(pdb)
    #print (EntriesToBe)
    
    
    
    
    
def BFS():
    
    
        
    """ def rotate(self, index):
        if index>= self.N:
            raise IndexError("out of bounds")
        if index + self.K > self.N:
            reversed_list = self.board_state[:]
            reversed_list[index:index+self.K] = reversed(self.board_state[index:index+self.K])
        else:
            if list reversed  
 """


          
    
    
    
