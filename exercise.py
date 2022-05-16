import random

# Sample board

board = [[1,1,1,8],[5,6,7,1],[3,4,1,5],[6,7,6,1]]

# Check if chosen cells are adjacent

def check_adjacency(r1, r2, c1, c2):
    if ((r1 - r2 == 1) | (r1 - r2 == -1)) & (c1 - c2 == 0):
        return True
    elif ((c1 - c2 == 1) | (c1 - c2 == -1)) & (r1 - r2 == 0):
        return True
    else:
        print('\nNon-adjacent cells!')
        return False

# Check if the move forms a complete row or column or pattern

def check_pattern(board, r1, r2, c1, c2):
    temp_board = board.copy()
    temp_board[r1][c1], temp_board[r2][c2] = temp_board[r2][c2], temp_board[r1][c1]

    for i in range(len(temp_board)):
        if (temp_board[i][0] == temp_board[i][1] == temp_board[i][2]):
            if (i in [0,1]) & ((temp_board[i][0] == temp_board[i+1][0] == temp_board[i+2][0]) | (temp_board[i][1] == temp_board[i+1][1] == temp_board[i+2][1]) | (temp_board[i][2] == temp_board[i+1][2] == temp_board[i+2][2])):
                return True, temp_board
            if (i in [2,3]) & ((temp_board[i][0] == temp_board[i-1][0] == temp_board[i-2][0]) | (temp_board[i][1] == temp_board[i-1][1] == temp_board[i-2][1]) | (temp_board[i][2] == temp_board[i-1][2] == temp_board[i-2][2])):
                return True, temp_board
        if (temp_board[i][1] == temp_board[i][2] == temp_board[i][3]):
            if (i in [0,1]) & ((temp_board[i][1] == temp_board[i+1][1] == temp_board[i+2][1]) | (temp_board[i][2] == temp_board[i+1][2] == temp_board[i+2][2]) | (temp_board[i][3] == temp_board[i+1][3] == temp_board[i+2][3])):
                return True, temp_board
            if (i in [2,3]) & ((temp_board[i][1] == temp_board[i-1][1] == temp_board[i-2][1]) | (temp_board[i][2] == temp_board[i-1][2] == temp_board[i-2][2]) | (temp_board[i][3] == temp_board[i-1][3] == temp_board[i-2][3])):
                return True, temp_board
    
    for i in range(len(temp_board)):
        print(temp_board[i])
    return False, board

def check_3(board, r1, r2, c1, c2):
    temp_board = board.copy()
    temp_board[r1][c1], temp_board[r2][c2] = temp_board[r2][c2], temp_board[r1][c1]

    for i in range(len(temp_board)):
        if (temp_board[i][0] == temp_board[i][1] == temp_board[i][2]) | (temp_board[i][1] == temp_board[i][2] == temp_board[i][3]):
            return True, temp_board

    for i in range(len(temp_board[0])):
        if (temp_board[0][i] == temp_board[1][i] == temp_board[2][i]) | (temp_board[1][i] == temp_board[2][i] == temp_board[3][i]):
            return True, temp_board
    
    return False, board

def check_4(board, r1, r2, c1, c2):
    temp_board = board.copy()
    temp_board[r1][c1], temp_board[r2][c2] = temp_board[r2][c2], temp_board[r1][c1]

    for i in range(len(temp_board)):
        if (temp_board[i][0] == temp_board[i][1] == temp_board[i][2] == temp_board[i][3]):
            return True, temp_board

    for i in range(len(temp_board[0])):
        if (temp_board[0][i] == temp_board[1][i] == temp_board[2][i] == temp_board[3][i]):
            return True, temp_board
    
    return False, board

# Take user input and check whether it satisfies all conditions

def check_legal(board, score):
    tmp_score = score
    for i in range(len(board)):
        print(board[i])

    row_1 = int(input('\nEnter row of first cell:')) - 1
    col_1 = int(input('Enter column of first cell:')) - 1
    row_2 = int(input('Enter row of second cell:')) - 1
    col_2 = int(input('Enter column of second cell:')) - 1

    if (0 <= row_1 <= 3) & (0 <= col_1 <= 3) & (0 <= row_2 <= 3) & (0 <= col_2 <= 3):
        adjacency = check_adjacency(row_1, row_2, col_1, col_2)
        if adjacency:
            pattern, temp_board_pat = check_pattern(board, row_1, row_2, col_1, col_2)
            four, temp_board_four = check_4(board, row_1, row_2, col_1, col_2)
            print(four)
            three, temp_board_three = check_3(board, row_1, row_2, col_1, col_2)
            if pattern:
                print('\nBomb move! +50 pts.')
                tmp_score += 50
                return True, tmp_score, temp_board_pat
            elif four:
                print('\nFour connected! +20 pts.')
                tmp_score += 20
                return True, tmp_score, temp_board_four
            elif three:
                print('\nThree connected! +10 pts.')
                tmp_score += 10
                return True, tmp_score, temp_board_three
            else:
                print('No special patterns were formed!')
                return False, tmp_score, board
        else:
            print('Non-adjacent cells!')
            return False, tmp_score, board

    else:
        print('\nInvalid coordinates!')
        return False, tmp_score, board

# Run game, check for false moves and accumulate score, end game at 5 false moves 

def play(board):
    score = 0
    false_moves = 0
    tmp_board = board
    while True:
        res, tmp_score, after_board = check_legal(tmp_board, score)
        if res == False:
            false_moves += 1
        else:
            false_moves = 0
        score += tmp_score
        tmp_board = after_board
        if false_moves >= 5:
            print('Too many false moves, game over!')
            print('Total Score:\n')
            print(score)
            break

play(board)