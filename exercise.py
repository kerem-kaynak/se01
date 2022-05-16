# Sample board

board = [[1,2,1,5],[1,1,1,1],[3,4,1,5],[6,7,6,1]]

# Check if chosen cells are adjacent

def check_adjacency(r1, r2, c1, c2):
    if ((r1 - r2 == 1) | (r1 - r2 == -1)) & (c1 - c2 == 0):
        return True
    elif ((c1 - c2 == 1) | (c1 - c2 == -1)) & (r1 - r2 == 0):
        return True
    else:
        print('\nNon-adjacent cells!')
        return False

# Check if the move forms a complete row or column

def check_pattern(board, r1, r2, c1, c2):
    temp_board = board.copy()
    temp_board[r1][c1], temp_board[r2][c2] = temp_board[r2][c2], temp_board[r1][c1]

    for i in range(len(temp_board)):
        if (temp_board[i][0] == temp_board[i][1] == temp_board[i][2]):
            if (i in [0,1]) & ((temp_board[i][0] == temp_board[i+1][0] == temp_board[i+2][0]) | (temp_board[i][1] == temp_board[i+1][1] == temp_board[i+2][1]) | (temp_board[i][2] == temp_board[i+1][2] == temp_board[i+2][2])):
                for i in range(len(temp_board)):
                    print(temp_board[i])
                return True
            if (i in [2,3]) & ((temp_board[i][0] == temp_board[i-1][0] == temp_board[i-2][0]) | (temp_board[i][1] == temp_board[i-1][1] == temp_board[i-2][1]) | (temp_board[i][2] == temp_board[i-1][2] == temp_board[i-2][2])):
                for i in range(len(temp_board)):
                    print(temp_board[i])
                return True
        if (temp_board[i][1] == temp_board[i][2] == temp_board[i][3]):
            if (i in [0,1]) & ((temp_board[i][1] == temp_board[i+1][1] == temp_board[i+2][1]) | (temp_board[i][2] == temp_board[i+1][2] == temp_board[i+2][2]) | (temp_board[i][3] == temp_board[i+1][3] == temp_board[i+2][3])):
                for i in range(len(temp_board)):
                    print(temp_board[i])
                return True
            if (i in [2,3]) & ((temp_board[i][1] == temp_board[i-1][1] == temp_board[i-2][1]) | (temp_board[i][2] == temp_board[i-1][2] == temp_board[i-2][2]) | (temp_board[i][3] == temp_board[i-1][3] == temp_board[i-2][3])):
                for i in range(len(temp_board)):
                    print(temp_board[i])
                return True
    
    for i in range(len(temp_board)):
        print(temp_board[i])
    print('\nNo special patterns were found!')
    return False

# Take user input and check whether it satisfies all conditions

def check_legal(board):
    for i in range(len(board)):
        print(board[i])

    row_1 = int(input('\nEnter row of first cell:')) - 1
    col_1 = int(input('Enter column of first cell:')) - 1
    row_2 = int(input('Enter row of second cell:')) - 1
    col_2 = int(input('Enter column of second cell:')) - 1

    if (0 <= row_1 <= 3) & (0 <= col_1 <= 3) & (0 <= row_2 <= 3) & (0 <= col_2 <= 3):
        adjacency = check_adjacency(row_1, row_2, col_1, col_2)
        if adjacency:
            complete_3 = check_pattern(board, row_1, row_2, col_1, col_2)
            if complete_3:
                print('\nValid move!')
                return True
    else:
        print('\nInvalid coordinates!')
        return False

# Run

check_legal(board)