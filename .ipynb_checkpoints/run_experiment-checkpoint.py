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

    # Run experiments
    for instance in puzzle_instances:
        # Time PDB creation
        start = time.time()
        pdb = createPDB(pdb_numbers, K)
        end = time.time()
        pdb_creation_time = end - start
        pdb_creation_times.append(pdb_creation_time)

        # Time A* with PDB heuristic
        # (In this placeholder, it just calls the same solver as breakpoints)
        start = time.time()
        solution_pdb = a_star_search(instance, K)
        end = time.time()
        astar_pdb_time = end - start
        astar_pdb_times.append(astar_pdb_time)

        # Time A* with breakpoints heuristic
        start = time.time()
        solution_bp = a_star_search(instance, K)
        end = time.time()
        astar_bp_time = end - start
        astar_breakpoints_times.append(astar_bp_time)

    # Print results to the console
    for label, p_time, pdb_time, bp_time in zip(instance_labels, pdb_creation_times, astar_pdb_times, astar_breakpoints_times):
        print(f"For {label} instance:")
        print(f" PDB creation time: {p_time:.4f} s")
        print(f" A* with PDB time: {pdb_time:.4f} s")
        print(f" A* with Breakpoints time: {bp_time:.4f} s\n")

    # Plot comparison graphs
    # We'll plot the A* times side by side for each instance
    x_positions = range(len(puzzle_instances))
    width = 0.3

    plt.figure(figsize=(10,6))
    # Bars for A* with PDB
    plt.bar([x - width/2 for x in x_positions], astar_pdb_times, width=width, label="A* + PDB")
    # Bars for A* with Breakpoints
    plt.bar([x + width/2 for x in x_positions], astar_breakpoints_times, width=width, label="A*")

    plt.xticks(x_positions, instance_labels)
    plt.ylabel("Time (seconds)")
    plt.title("Comparison: PDB vs A_star")
    plt.legend()
    plt.tight_layout()
    plt.show()

    # If you want, you can also plot PDB creation times separately
    plt.figure(figsize=(10,6))
    plt.bar(x_positions, pdb_creation_times, width=0.4, label="PDB Creation")
    plt.xticks(x_positions, instance_labels)
    plt.ylabel("Time (seconds)")
    plt.title("PDB Creation Times")
    plt.legend()
    plt.tight_layout()
    plt.show()
