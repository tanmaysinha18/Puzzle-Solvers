# Puzzle Solvers

The repo contains simple n-puzzle solvers.

The completed ones, and their respective issues and to-do's are given below.

1. A* Search :- Simple implementation of A* with a simple heuristic. Should work very well for small shuffling and small size of board. To run, enter the A* folder and run puzzle.py
+ Issues :- 
    * Becomes slow when the depth is larger
    * The hash function is not optimum and leads to improper cycle detection, which causes it to enter a loop.
+ To-Do :-
    * Fix the hash function
    * Better heuristic
    * Optimize the code, as the current one is slow(perhaps move away from Python)

Other implementations soon to arrive...
