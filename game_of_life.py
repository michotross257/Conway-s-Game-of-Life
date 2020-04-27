"""
Conway's Game of Life
---------------------
Rule 1: A DEAD cell with exactly 3 LIVING neighbors will become a LIVING cell
Rule 2: A LIVING cell with 2 or 3 LIVING neighbors will remain LIVING
Rule 3: A LIVING cell with 1, 4, 5, 6, 7 or 8 LIVING neighbors will become DEAD
Rule 4: A DEAD cell without exactly 3 living neighbors will remain DEAD
"""

import copy
import time


NUM_ROWS = 5
MARK_LIVE = "*"
MARK_DEAD = " "
INITIAL_COORDINATES = [(0,0), (1,1), (1,2), (2,0), (2,1)]


def populate_board(gameBoard):
    """
    Populate the game board using the initial coordinates.

    Args:
        gameBoard(list): 2-d array representing unintialized game board

    Returns:
        gameBoard(list): 2-d array representing intialized game board
    """
    for coordinate in INITIAL_COORDINATES:
        try:
            row, col = coordinate[0], coordinate[1]
            gameBoard[row][col] = gameBoard[row][col].replace(MARK_DEAD, MARK_LIVE)
        except IndexError:
            print ("ERROR: Coordinates were encountered that are not found on game board")

    return gameBoard


def display_board(gameBoard, gen_num):
    """
    Display game board with current generation.

    Args:
        gameBoard(list): 2-d array representing game board
        gen_num(int): number of current generation

    Returns:
        None
    """
    print ("+----------------+")
    print ("| GENERATION #{} |".format(str(gen_num + 1).zfill(2)))
    print ("+----------------+")
    for row in range(NUM_ROWS):
        vals = [gameBoard[row][col] for col in range(NUM_ROWS)]
        output = ' {} |' * (NUM_ROWS-1) + ' {} '
        print(output.format(*vals))
        if row < NUM_ROWS-1:
            print ('---+' * (NUM_ROWS-1) + '---')
        time.sleep(0.10)


def _get_neighbors(dimension):
    """
    Get the coordinates of neighbors (left-right or above-below)
    at a given row or column coordinate.

    Args:
        dimension(int): the row or column coordinate

    Returns:
        list: the neighbors of a given coordinate
    """
    coordinates = range(NUM_ROWS)
    neighbors = [dimension-1, dimension, dimension+1]
    for index, val in enumerate(neighbors):
        if val < min(coordinates):
            neighbors[index] = min(coordinates)
        elif val > max(coordinates):
            neighbors[index] = max(coordinates)

    return list(set(neighbors))


def generational_shift(gameBoard):
    """
    For a given generation, apply the game rules.

    Args:
        gameBoard(list): 2-d array representing game board

    Returns:
        list: game board updated after a single generation
    """
    gameBoard_copy = copy.deepcopy(gameBoard)
    for row in range(NUM_ROWS):
        row_neighbors = _get_neighbors(row)
        for col in range(NUM_ROWS):
            col_neighbors = _get_neighbors(col)
            neighbors = []
            for rn in row_neighbors:
                for cn in col_neighbors:
                    if rn == row and cn == col:
                        pass
                    else:
                        neighbors.append(gameBoard[rn][cn])

            if gameBoard[row][col] == MARK_DEAD and neighbors.count(MARK_LIVE) == 3:
                gameBoard_copy[row][col] = gameBoard_copy[row][col].replace(MARK_DEAD, MARK_LIVE)
            elif gameBoard[row][col] == MARK_LIVE and neighbors.count(MARK_LIVE) in [1,4,5,6,7,8]:
                gameBoard_copy[row][col] = gameBoard_copy[row][col].replace(MARK_LIVE, MARK_DEAD)

    return gameBoard_copy


if __name__ == '__main__':
    print ("How many generations would you like to simulate?")
    desired_generations = int(input("Please enter an integer (min: 1; max: 15) and then press [ENTER]: "))
    assert 1 <= desired_generations <= 15, "Number of generations must be integer >= 1 and <= 15"

    # create a 2d array that represents the board
    gameBoard = [[MARK_DEAD for a in range(NUM_ROWS)] for b in range(NUM_ROWS)]

    # populate the board with live coordinates
    gameBoard = populate_board(gameBoard)

    for generation in range(desired_generations):
        display_board(gameBoard, generation)
        gameBoard = generational_shift(gameBoard)
