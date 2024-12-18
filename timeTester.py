import game
import time


#uncomment the lines
#list = []
list1 = [ 8, 6, 7, 3, 9,10, 2, 4, 5]# terminates in around 0.28 seconds
list2 = [ 9,10, 8, 7, 4, 5, 3, 6,11, 2]#terminates in 16 seconds
list3 = [2,12, 5, 6,10, 7, 4, 3,11, 9, 8]
list4 = [ 8, 5, 6, 7, 4, 1, 9,10,11, 2, 3]
start_time = time.time()
#list = game.format_sequence(list) #uncomment if you included 1 in your example list
#example configuration for createPDB
#game.createPDB([2,3,6,9], 20, 4)
#example configuration for astar_solver
#game.astar_solver(list1, 4)

print("--- %s seconds ---" % (time.time() - start_time))