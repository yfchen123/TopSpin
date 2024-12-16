import game
import time

start_time = time.time()
game.createPDB([2,3,6, 12], 20, 4)
print("--- %s seconds ---" % (time.time() - start_time))