import time

def display_board(board):
    grid = []
    for row in board:
        row_str = ''
        for cell in row:
            if cell == 1:
                row_str += '#'
            else:
                row_str += '*'
        grid.append(row_str)
    return '\n'.join(grid)


def next_generation(board):
    rows = len(board)
    cols = len(board[0])
    updated_board = [[0] * cols for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            live_neighbours = count_live_dead_neighbors(board, row, col)

            if board[row][col] == 1:
                if live_neighbours < 2 or live_neighbours > 3:
                    updated_board[row][col] = 0
                else:
                    updated_board[row][col] = 1
            else:
                if live_neighbours == 3:
                    updated_board[row][col] = 1

    return updated_board


def count_live_dead_neighbors(board, row, col):
    rows = len(board)
    cols = len(board[0])
    live_neighbors = 0
    for i in range(max(0, row-1), min(rows, row+2)):
        for j in range(max(0, col-1), min(cols, col+2)):
            if board[i][j] == 1 and (i != row or j != col):
                live_neighbors += 1
    return live_neighbors





def main():
    # Initialize the starting grid
    grid = [[0, 1, 0],[0, 0, 1],[1, 1, 1]]

    
    while True:
        
        grid = next_generation(grid)

        
        print(display_board(grid))
        time.sleep(0.8)

print("Game Over")



if __name__ == "__main__":
    main()