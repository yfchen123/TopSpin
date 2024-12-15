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

path = []
                
for i in range(2, N - K+2):
                print((game.insideRotate(list, i, K)),path+[i])