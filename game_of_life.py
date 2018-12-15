import copy

NUM_ROWS = 5
NUM_COLS = 5
MARK_LIVE = "*"
MARK_DEAD = " "
INITIAL_COORDINATES = [(0,0), (1,1), (1,2), (2,0), (2,1)]

def main():
    print ("How many generations would you like to simulate?")
    desired_generations = int(input("Please enter a number greater than ZERO and then press the 'ENTER' key: "))

    # create a 2d array that represents the board
    gameBoard = [['' for a in range(NUM_COLS)] for b in range(NUM_ROWS)]
    
    # populate the board with dead squares to start
    initialize_board(gameBoard)
    
    # populate the board with live coordinates
    populate_board(gameBoard)

    for generation in range(desired_generations):
        display_board(gameBoard, generation)
        gameBoard = generational_shift(gameBoard)

def initialize_board(gameBoard):
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            gameBoard[row][col] += MARK_DEAD
            
def populate_board(gameBoard):
    for coordinate in INITIAL_COORDINATES:
        try:
            row, col = coordinate[0], coordinate[1]
            gameBoard[row][col] = gameBoard[row][col].replace(MARK_DEAD, MARK_LIVE)
        except IndexError:
            print ("ERROR: Coordinates were encountered that are not found on game board")
                
def display_board(gameBoard, gen_num):
    print ("+----------------+")
    print ("| GENERATION #{} |".format(str(gen_num + 1).zfill(2)))
    print ("+----------------+")
    for row in range(NUM_ROWS):
        vals = [gameBoard[row][col] for col in range(NUM_COLS)]
        output = ' {} |' * (NUM_ROWS-1) + ' {} '
        print(output.format(*vals))
        if row < NUM_ROWS-1:
            print ('---+' * (NUM_ROWS-1) + '---')

def get_neighbors(dimension, row=True):
    if row:
        coordinates = range(NUM_ROWS)
    else:
        coordinates = range(NUM_COLS)
        
    neighbors = [dimension-1, dimension, dimension+1]
    for index, val in enumerate(neighbors):
        if val < min(coordinates):
            neighbors[index] = min(coordinates)
        elif val > max(coordinates):
            neighbors[index] = max(coordinates)

    return list(set(neighbors))

def generational_shift(gameBoard):
    '''Rule 1: A DEAD cell with exactly 3 LIVING neighbors will become a LIVING cell.
       Rule 2: A LIVING cell with 2 or 3 LIVING neighbors will remain LIVING.
       Rule 3: A LIVING cell with 1, 4, 5, 6, 7 or 8 LIVING neighbors will become DEAD.
       Rule 4: A DEAD cell without exactly 3 living neighbors will remain DEAD.'''

    gameBoard_copy = copy.deepcopy(gameBoard)
    for row in range(NUM_ROWS):
        row_neighbors = get_neighbors(row, row=True)
        for col in range(NUM_COLS):
            col_neighbors = get_neighbors(col, row=False)
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
    main()
