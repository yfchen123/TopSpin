import time
import matplotlib.pyplot as plt
from game import createPDB, astar_solver, calculate_breakpoints, a_star_search, is_goal, get_successors



if __name__ == "__main__":
    # Define a set of puzzle instances to test
    # These should be in the format expected by your solver (excluding '1', if your code does so)
    puzzle_instances = [
        [2,3,4,5],             # A small instance
        [2,3,5,4,6,7],         # A medium-sized instance
        [3,5,14,9,8,13,7,6,10,2,18,12,4,11,]   # A larger instance (adjust as desired)
    ]
    instance_labels = ['Small', 'Medium', 'Larger']

    # Pattern subset for the PDB (just an example)
    pdb_numbers = [2, 3, 4]
    K = 4

    # Lists to store the timing results
    pdb_creation_times = []
    astar_pdb_times = []
    astar_breakpoints_times = []

    # Run exper