# QuTiling: Quantum Tiling
Anna Rose Osofsky, Jacob Pritzker, Joseph Feld, Sage Simhon
## Introduction
 
Quantum computing has the promise of speeding up our solving of NP-hard problems through annealing. A polynomial-time verifier allows for clear translation into a QUBO or DFQ, making the use of a QPU fairly straightforward for this class of problems.  
In this project, we present an implementation of a quantum tiling problem solver. Given a list of tiles to use and a grid, it will completely tile that grid with the given tiles if possible. If it is not possible, it will cover as much space as possible. Our system supports arbitrary numbers of arbitrary tiles tiling an arbitrary space in 2 or 3 dimensions, which is an NP-hard problem[1].  
We would like to thank Ariel Jacobs for his amazing tiling problems which inspired this project.  
We saw that other people have used quantum annealing to solve a similar problem[2], but our solution is different since we have 3D capabilities, support for arbitrary tiles and grids, the ability to use pentominoes and above, the ability to find a good solution that doesn’t tile the whole grid in the case where a complete tiling is impossible, and their problem is about having only a specific number of each tile.  
## Applications
Solving these tiling problems has possible applications in real-life packing problems.   
For 2D-like problems to efficiently pack objects, this could give solutions in arranging desks in an office, or packing furniture into a truck.  
For 3D, this could describe how to efficiently pack a box full of things. With valentines day coming up, the chocolate packing applications are very clear.  
## Defining The DFQ
We model each tile as a set of squares around (0,0), which we call the prime square, and a number indicating what orientation the tile is in. We create a DFQ where each possible location is a variable with a value that if nonzero indicates there is a prime square on that space. Then its value is the orientation of the tile.  
For a tile with n squares, a nonzero value gives -n to the objective function. This counts how many tiles are covered in the energy. The more tiles get covered, the lower the energy gets.  
Then we need to penalize two things: tiles going off the grid and tiles overlapping with one another. When we have a grid with N spaces and tiles with max number of tiles nm, we use a penalty of gamma = N\*nm+1. If all of the tiles are assigned the smallest value of nm, just one penalty is enough to make that state have an energy of gamma-nm\*N = 1 which is worse than just placing no tiles, which has energy 0.  
We can stop tiles going off the grid by using linear terms where any value of a variable describing a tile that goes off the grid gets a value of gamma. We can calculate this classically by checking all the squares within all possible tile orientations.  
We can stop tiles from overlapping using quadratic terms. We go through all possible tile placements and orientations and assign a value of gamma to any pair of tiles that overlap.  
Then we send this DFQ to the D-Wave hybrid solver and get back a tiling, which we can display with our ASCII art generator.  
## User Interface
Defining a grid: A user can define a grid in two ways. One can specify an m by n rectangle, or a m by n by p rectangular prism, and a list of coordinates will be generated. Alternatively, for an arbitrary grid shape, the user can manually provide a list of coordinates, with the constraint that the minimum value of each coordinate in every dimension must be 0.   
Defining a set of tiles: A tile shape is defined as a list of tuples of coordinates. Each tile must have a (0,0) coordinate corresponding to the prime square on the tile. The user provides a list of each tile shape, allowing for multiple shapes if desired.  
## Demonstrations
The GitHub repository link is https://github.com/iQuHACK/2021_Hadamarcheshvan.  

[1] Erik D. Demaine, Martin L. Demaine. Jigsaw Puzzles, Edge Matching, and Polyomino Packing: Connections and Complexity. Graphs and Combinatorics 23, 195–208 (2007). https://doi.org/10.1007/s00373-007-0713-4
[2] Asa Eagle, Takumi Kato, and Yuichiro Minato. Solving tiling puzzles with quantum annealing. 2019. arXiv: 1904.01770 [quant-ph].
 
 
## ToDo
Things we would want to fix/implement but didn't have enough time to do
* Make it N-dimensional
* Explore efficiency improvements
## Highlights:
* Arbitrary grid shapes and sizes!
* Arbitrary tile shapes and sizes!
* Variety of tile shapes in one problem!
* 2- and 3-dimensional support!