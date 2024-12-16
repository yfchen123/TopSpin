import game
list = [2,3,4,5,6,7,8, 9]
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
""" for i in range(1, N+2):
    game.outsideRotate(list, i, K) """
    #print("tester",i-2+K-len(list)-1)
game.createPDB([2,3,6], 8, 4)    
