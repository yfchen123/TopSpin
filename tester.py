#import game
list = [2,3,4,5,6,7,8, 9]
#game.createPDB([1,2, 3, 4],16)
index = 2
k = 4
ret = list[:index-2]
temp = list[index-2:index-2+k]
temp.reverse()
ret.extend(temp)
ret.extend(list[index-2+k:])
print(ret)