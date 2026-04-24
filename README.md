# linear-cell

Linear Cell is a combinatorial game where two players take turns removing cells from a grid; the player who removes the last cell(s) wins. Players can remove any number of cells as long as they all lie on a line that is horizontal, vertical, or diagonal. If the players begin on an nxm board, who has a winning strategy? This project attempts to answer that very question.

The Cell module serves as the main UI for this project: when prompted, enter the board size, then the binary encoding of the state you wish to analyze. To translate a board state into binary, start at the bottom right corner, then go right to left, bottom to top, and type a 1 if the cell has not been removed, or a 0 if a cell has been removed. After a state is entered, the program will indicate whether your position is an N-position or a P-position. An N-position means that the player who moves (N)ext has a winning strategy, and the last analyzed position is the state that said player should create next (it's the optimal move). A P-position means that the player who moved (P)reviously has a winning strategy; no matter how the next player moves, the previous player can counter it. 

The algorithm takes a depth-first brute-force approach, systematically checking each possible move from a position until it finds a P-Position. A position is decided to be a P-position if it is the null position (all cells have been removed), or if all possible moves lead to N-positions. A position is decided to be an N-position if at least one move in that position leads to a P-position. After a state is assigned as being an N or P-position, its binary encoding is stored in a dictionary with its position type (False or N and True for P). Before all possible moves of a position are searched, the memory is searched to see if this same state has already been computed. If it has, then the value of the state is taken into account for the next significant position, otherwise the algorithm continues down the line like usual.

## Strategies used before and during the creation of the algorithm

Before this project was created, this problem was attempted to be solved by hand. It is easy to list all possible moves in a 2x2 or 2x3 grid to see who wins, but moving to a 3x3 grid is a big step in complexity. 

## Improvements and future work

* Change the memory from a dictionary to an AVL tree, searching time collapses from O(n) to O(log n)
* When storing states into memory, store their normal form to further reduce search time
* When generating all moves from a position, convert associated functions with generators
* Create a general depth-search algorithm that any grid-based game with a generator can use
  * Implement the other two cell-based games: continuous cell and discrete cell   
