import game
from game import insideRotate, outsideRotate

list = [2,3,4,5,6,7,8, 9]
list2 = [2,3,4,5,9,8,7,6]
list3 = [6,13,17,3,4,15,9,14,20,5,12,11,18,10,7,16,19,2,8]
#game.createPDB([1,2, 3, 4],16)
index = 2
K = 4
N = len(list)+1
""" ret = list[:index-2]
temp = list[index-2:index-2+K]
temp.reverse()
ret.extend(temp)
ret.extend(list[index-2+K:])
print(ret) """
#print(list[-4:])
                
#for i in range(2, N - K+2):
#                print((game.insideRotate(list, i, K)),path+[i])

    #print("tester",i-2+K-len(list)-1)
#game.createPDB([2,3,6, 12], 20, 4)    
""" for i in range(2, N - K+2):
    print(i)
    #create inside rotation children
    print((insideRotate(list, i, K)))
#Create children that don't need to wrap around (outside rotation)
for i in range(N-K+2, N+1):
    print(i)
    print((outsideRotate(list, i, K)))
 """
#print([*range(2,len(list)+2)] == list)
#print(game.calculate_breakpoints([5,2,3,4]))
#game.astar_solver(list3, 4)
#print([*range(2,len(list)+1)])
#print([*range(2,len(list)+2)])
#print(list)
print(list)