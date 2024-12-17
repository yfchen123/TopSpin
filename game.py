from math import perm
import queue as q
import heapq as hq

###
#Takes in a list of numbers and produces a pdb lookup table with instructions on how to move the given numbers to their correct position in the identity list in the best moves
#performs a breadth first search to and checks if its current formation is in the PDB or not. If it isn't it will add its current path to the table, then create offspring.
#if it already in the matrix then the branch is pruned and will not create children.
# 1 is considered the first point no matter what
#pdb_numbers: a list of the numbers that will be checked for the pdb
#N: number of pegs
#K: number value for size of spinner

def createPDB(pdb_numbers, N, K):
    pdb = dict()
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
    identity = [*range(2,len(list)+2)]
    print(identity)
    checked = set()
    heap = []
    priority = calculate_breakpoints(list)/2
    N = len(list)+1
    
    hq.heappush(heap, (priority, 0, list, []))
    
    while len(heap) > 0:
        (prio, path_length, state, path) = hq.heappop(heap)
        #print(prio, path_length, state, path)
        if state == identity:
            print(path)
            return path
        else:
            checked.add(tuple(state))
            #print(state)
            #populate children
            next_state = outsideRotate(state, 1, K)#swap on 1
            if not(tuple(next_state) in checked):
                priority = calculate_breakpoints(state)/2 + path_length
                hq.heappush(heap, (priority, path_length+1, next_state, path+[1]))
            for i in range(2, N - K+2):
                #print(i)
                #create inside rotation children
                next_state = insideRotate(state, i, K)#inside swaps
                if not(tuple(next_state) in checked):
                    priority = calculate_breakpoints(state)/2 + path_length
                    hq.heappush(heap, (priority, path_length+1, next_state, path+[i]))
            #Create children that don't need to wrap around (outside rotation)
            for i in range(N-K+2, N+1):
                #print(i)
                next_state = outsideRotate(state, i, K)#inside swaps
                if not(tuple(next_state) in checked):
                    priority = calculate_breakpoints(state)/2 + path_length
                    hq.heappush(heap, (priority, path_length+1, next_state, path+[i]))
    print("no solution found")

#takes a list of size n-1 with numbers in any permutation of numbers 2 to n and returns the number of breakpoints, list are in the same [2,3,4,5] type format without the 1 as is in 
def calculate_breakpoints(list):
    n = len(list)+1
    breakpoint_count = 0
    previous = list[0]
    if previous != 2:
        breakpoint_count += 1
    if n > 2:
        if list[-1] != n:
            breakpoint_count += 1
            
        for num in list[1:n-1]:
            if num != previous+1:
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

#takes in a list of numbers that represent a configuration of the puzzle and then creates a list in the configuration that the functions in the file can use
#standardizes 1 to be the starting position in the set and then removes it from the list
def format_sequence(list):
    ones_index = list.index(1)
    return [*list[ones_index+1:], *list[:ones_index]]
    
    
if __name__ == "__main__":
    print("hello")