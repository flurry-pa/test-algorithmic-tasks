"""
https://coderbyte.com/sl-candidate?inviteKey=vKTE9sfg2s
Game of Life Strings
The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells,
each of which is in one of two possible states, alive or dead.
Every cell interacts with its eight neighbours,
which are the cells that are horizontally, vertically, or diagonally adjacent.
At each step in time, the following transitions occur:

- Any live cell with fewer than two live neighbours dies, as if caused by under-population.
- Any live cell with two or three live neighbours lives on to the next generation.
- Any live cell with more than three live neighbours dies, as if by overcrowding.
- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

Implement the method that calculates new generation of game of life.
The method receives a string in the format "000_000_000"
that represents the matrix NxM of 0's (dead cell) and 1's (living cell).

And returns a string in the same format "000_000_000" that represents equally sized array
representing the next generation.
Cells outside the array must be considered dead.
Cells that would born out of the array boundaries should be ignored
(universe never grows beyond the initial NxM grid).
"""


def game_of_life_strings(cell_map: str) -> str:
    # split the input string by "_" to get the rows of the grid
    rows = cell_map.split("_")

    # get the number of rows and columns of the grid
    m_row = len(rows)
    n_col = len(rows[0])

    # initialize an empty string to store the output
    output = ""

    # loop through each cell in the grid
    for i in range(m_row):

        for j in range(n_col):
            # get the current cell value (0 or 1)
            cell = int(rows[i][j])
    
            # initialize a variable to store the number of live neighbors
            live_cells = 0

            # loop through the eight possible neighbors (neighboring cells), this is 3 x 3 square matrix
            for i_near in [-1, 0, 1]:

                for j_near in [-1, 0, 1]:
                    # skip the current cell
                    if i_near == 0 and j_near == 0:
                        continue

                    # get the neighbor row and column indices
                    ni = i + i_near
                    nj = j + j_near

                    # check if the neighbor is within the grid boundaries
                    if 0 <= ni < m_row and 0 <= nj < n_col:
                        # Add the neighbor value to the live_cells count
                        live_cells += int(rows[ni][nj])

            # apply the rules of the game to determine the next cell value
            if cell == 1 and (live_cells < 2 or live_cells > 3):
                # live cell dies by underpopulation or overpopulation
                next_cell = "0"

            elif cell == 0 and live_cells == 3:
                # dead cell becomes alive by reproduction
                next_cell = "1"

            else:
                # cell state remains unchanged
                next_cell = str(cell)

            # append the next cell value to the output string
            output += next_cell

        # append a "_" separator after each row except the last one
        if i < m_row - 1:
            output += "_"

    # return the output string
    return output


# keep this function call here
# print(game_of_life_strings(cell_map="000_111_000"))
# print(game_of_life_strings(cell_map="11"))
assert game_of_life_strings(cell_map="000_111_000") == "010_010_010"
assert game_of_life_strings(cell_map="00") == "00"

"""
This solution has a time complexity of O(M*N), where M and N are the number of rows and columns of the grid, 
and a space complexity of O(M*N), where M and N are the number of rows and columns of the output string.
"""
