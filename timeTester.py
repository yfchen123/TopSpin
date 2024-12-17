import game
import time

start_time = time.time()
game.createPDB([2,3,6,10, 18], 20, 4)
print("--- %s seconds ---" % (time.time() - start_time))