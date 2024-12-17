import game
import time

list3 = [6,13,17,3,4,15,9,14,20,5,12,11,18,10,7,16,19,2,8]
list4 = [15, 9, 2, 6, 8, 5,10,14,12, 3, 4, 7,16,11,13]
list = [ 3,12, 5, 7, 8, 9, 4,10, 2,11, 6,]
list6 = [ 9,10, 8, 7, 4, 5, 3, 6,11, 2]
list5 = [ 8, 6, 7, 3, 9,10, 2, 4, 5]
list7 = [2,12, 5, 6,10, 7, 4, 3,11, 9, 8]
list8 = [ 8, 5, 6, 7, 4, 9,10,11, 2, 3]
start_time = time.time()
#game.createPDB([2,3,6,10, 18], 20, 4)
game.astar_solver(list5, 4)
print("--- %s seconds ---" % (time.time() - start_time))