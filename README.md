# TopSpin
Authors:

Yun Fei Chen (yfc9)

Braden Takashima btakashi

Snimer S Gill (ssg28)

# Introduction
The purpose of this project is to explore the effect of using different PDB algorithms on the TopSpin problem and to benchmark the performance of the various algorithms. For the puzzle we generated random solvable configurations. In TopSpin
a configuration is solvable if the start configuration and the end configuration 
have the same parities. The proof is demonstrated in the paper below: https://digitalrepository.salemstate.edu/bitstream/handle/20.500.13013/607/auto_convert.pdf?sequence=3. 

#play yourself
run the main.py file to try your hand at the puzzle on an N=20, K = 4 setup.


#How to use game.py
The tester.py and timeTester.py files contain example code.
The times obtained were made using timeTester.py.
There are two main functions in game.py, game.createPDB() and game.astar_solver().

#game.createPDB(db_numbers, N, K)
pdb_numbers: a list of the numbers that will be checked for the pdb
N: number of pegs
K: number value for size of spinner
Takes in a list of numbers and produces a pdb lookup table with instructions on how to move the given numbers to their correct position in the identity list in the best moves
performs a breadth first search to and checks if its current formation is in the PDB or not. Uncomment the second to last line of createPDB if you would like to inspect the finished PDB yourself

#game.astar_solver(list, K)
This is an A* style solver for the top spin problem that uses half the number of breakpoints as it's heuristic.
the list is the current configuration of the puzzle.EG: [1,2,3,...,N] Must be in the normalized form so that 1 is the first position in the list, then 1 is removed. IE: [3,1,2] -->[2,3]
you may use game.format_sequence(list) to normalize a sequence contataining a 1.
It will return the solution in the form of the list of steps you take to solve the congfiguration.

The following is an example of how to use the solver. 
When the state [1, 8, 6, 7, 3, 9,10, 2, 4, 5] is input into the A*, with K = 4, it produces the following sequence, [2, 5, 2, 5, 8, 2]. To use this to solve the puzzle, perform a spin with the given index as the left most position of the spinner.

2
1, 8, 6, 7, 3, 9,10, 2, 4, 5 → 1, 3, 7, 6, 8, 9, 10, 2, 4, 5
5
1, 3, 7, 6, 8, 9, 10, 2, 4, 5 → 1, 3, 7, 6, 2, 10, 9, 8, 4, 5
2
1, 3, 7, 6, 2, 10, 9, 8, 4, 5 → 1, 2, 6, 7, 3, 10, 9, 8, 4, 5
5
1, 2, 6, 7, 3, 10, 9, 8, 4, 5 → 1, 2, 6, 7, 8, 9, 10, 3, 4, 5
8
1, 2, 6, 7, 8, 9, 10, 3, 4, 5 → 1, 5, 4, 3, 2, 6, 7, 8, 9, 10
2
1, 5, 4, 3, 2, 6, 7, 8, 9, 10 → 1, 2, 3, 4, 5, 6, 7, 8, 9, 10



# References

https://digitalrepository.salemstate.edu/bitstream/handle/20.500.13013/607/auto_convert.pdf?sequence=3

