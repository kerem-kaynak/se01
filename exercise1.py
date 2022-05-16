board = [[1,2,3],[4,4,5],[5,3,4]]

def check_adjacency(r1, r2, c1, c2):
    if ((r1 - r2 == 1) | (r1 - r2 == -1)) & (c1 - c2 == 0):
        return True
    elif ((c1 - c2 == 1) | (c1 - c2 == -1)) & (r1 - r2 == 0):
        return True
    else:
        print('\nNon-adjacent cells!')
        return False

def check_3(board, r1, r2, c1, c2):
    temp_board = board.copy()
    temp_board[r1][c1], temp_board[r2][c2] = temp_board[r2][c2], temp_board[r1][c1]

    for i in range(len(temp_board)):
        if temp_board[i][0] == temp_board[i][1] == temp_board[i][2]:
            for i in range(len(temp_board)):
                print(temp_board[i])
            return True

    for i in range(len(temp_board[0])):
        if temp_board[0][i] == temp_board[1][i] == temp_board[2][i]:
            for i in range(len(temp_board)):
                print(temp_board[i])
            return True
    
    print('\nNo complete rows or columns were found!')
    return False

def check_legal(board):
    for i in range(len(board)):
        print(board[i])

    row_1 = int(input('\nEnter row of first cell:')) - 1
    col_1 = int(input('Enter column of first cell:')) - 1
    row_2 = int(input('Enter row of second cell:')) - 1
    col_2 = int(input('Enter column of second cell:')) - 1

    if (0 <= row_1 <= 2) & (0 <= col_1 <= 2) & (0 <= row_2 <= 2) & (0 <= col_2 <= 2):
        adjacency = check_adjacency(row_1, row_2, col_1, col_2)
        if adjacency:
            complete_3 = check_3(board, row_1, row_2, col_1, col_2)
            if complete_3:
                print('\nValid move!')
                return True
    else:
        print('\nInvalid coordinates!')
        return False

check_legal(board)