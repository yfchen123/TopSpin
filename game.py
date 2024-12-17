import numpy as np
from math import perm
import queue as q

###
#Takes in a list of numbers and produces a pdb lookup table with instructions on how to move the given numbers to their correct position in the identity list in the best moves
#performs a breadth first search to and checks if its current formation is in the PDB or not. If it isn't it will add its current path to the table, then create offspring.
#if it already in the matrix then the branch is pruned and will not create children.
# 1 is considered the first point no matter what
#pdb_numbers: a list of the numbers that will be checked for the pdb
#N: number of pegs
#K: number value for size of spinner

def createPDB(pdb_numbers, N, K):
    number_of_numbers = len(pdb_numbers)
    pdb = dict()
    EntriesToBe = perm(N, number_of_numbers)#checks the current number of entries that are to exist once the PDB has finished being made.
    currentEntries = 0
    queue = q.Queue()
    queue.put(([*range(2, N+1)],[]))
    #perfrom Breadth first search
    #while currentEntries < EntriesToBe:
    while queue.empty() == False:
        (current, path) = queue.get()
        pdbIndex = []
        for num in pdb_numbers:#gets the current location in the state where each of the elements to find are
            pdbIndex.append(current.index(num)+2)
        if not tuple(pdbIndex) in pdb:#if the entry does not yet exist in the pdb
            pdb[tuple(pdbIndex)] = path
            currentEntries += 1
            #create children that need to wrap around.
            queue.put((outsideRotate(current, 1, K),path+[1]))
            for i in range(2, N - K+2):
                #print(i)
                #create inside rotation children
                queue.put((insideRotate(current, i, K),path+[i]))
            #Create children that don't need to wrap around (outside rotation)
            for i in range(N-K+2, N+1):
                #print(i)
                queue.put((outsideRotate(current, i, K),path+[i]))
    #print(pdb)
    return pdb    
    
    
    
    
def astar_solver(list, K):
    identity = range(2,len(list)+2)
    
    
    return 0

#takes a list of size n-1 with numbers in any permutation of numbers 2 to n and returns the number of breakpoints, list are in the same [2,3,4,5] type format without the 1 as is in 
def calculate_breakpoints(list):
    n = len(list)+1
    breakpoint_count = 0
    previous = list[0]
    if previous != 2:
        print("1 to 2 wrong")
        breakpoint_count += 1
    if n > 2:
        if list[-1] != n:
            print("last to 1 wrong")
            breakpoint_count += 1
            
        for num in list[1:n-1]:
            if num != previous+1:
                print(previous, "to", num,  "wrong")
                breakpoint_count += 1
            previous = num
    return breakpoint_count
                
            
            
#returns a list representing a state with a single slip starting with the position at index as the left most in the flip
#takes a list state [], 
#the index is the left most position in the range to be flipped. (the first index in the list would be at index value 2)
#k is the number of pegs to be flipped
#assumes it has been fed values that do not break the rule
def insideRotate(list, index, K):
    if (index <= 1 or index+K-2 > len(list)):
        raise Exception("Improper index, not an inside rotate")
    ret = list[:index-2]
    temp = list[index-2:index-2+K]
    temp.reverse()
    ret.extend(temp)
    ret.extend(list[index-2+K:])
    return ret




def outsideRotate(list, index, K):
    #print(index)
    if not(index == 1 or (index-2 < len(list) and index-2+K > len(list))):
        raise("Improper index for an outside rotate")

    #steps, take the portion from the end to rotate
    if index == 1:
        return [*list[K-1:], *list[K-2::-1]]
    end_partition = list[index-2:]
    start_partition = []
    
    #print("indexy thing is", index-2+K-len(list)-1 )
    if (index-2+K-len(list)-1) >= 0:
        start_partition = list[:index-3+K-len(list)]
    untouched_partition = list[index-3+K-len(list):index-2]
    #print("untouched_partition", untouched_partition)
   # print ("end_partition", end_partition)
   # print("start_partition", start_partition)
    ret = [*end_partition[::-1], *untouched_partition,*start_partition[::-1] ]

    return ret
    
    
    
