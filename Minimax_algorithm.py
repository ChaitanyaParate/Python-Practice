import math


def evaluate(board):
   
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == 'X':
                return 10
            elif board[row][0] == 'O':
                return -10
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'X':
                return 10
            elif board[0][col] == 'O':
                return -10


    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 10
        elif board[0][0] == 'O':
            return -10

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 10
        elif board[0][2] == 'O':
            return -10

  
    return 0


def is_moves_left(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == '_':
                return True
    return False


def minimax(board, depth, is_maximizing_player):
    score = evaluate(board)

   
    if score == 10:
        return score

  
    if score == -10:
        return score

  
    if not is_moves_left(board):
        return 0

    
    if is_maximizing_player:
        best = -math.inf

     
        for i in range(3):
            for j in range(3):
           
                if board[i][j] == '_':
                   
                    board[i][j] = 'X'

            
                    best = max(best, minimax(board, depth + 1, False))

                   
                    board[i][j] = '_'
        return best

   
    else:
        best = math.inf

       
        for i in range(3):
            for j in range(3):
               
                if board[i][j] == '_':
                    # Make the move
                    board[i][j] = 'O'

                  
                    best = min(best, minimax(board, depth + 1, True))

                    
                    board[i][j] = '_'
        return best


def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
               
                board[i][j] = 'X'

                
                move_val = minimax(board, 0, False)

                
                board[i][j] = '_'

                
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def play_game():
    board = [['_' for _ in range(3)] for _ in range(3)]
    print("Tic Tac Toe Game (AI is 'X', Player is 'O')\n")
    print_board(board)

    while True:
        
        row, col = map(int, input("Enter your move (row and column 0-2): ").split())
        if board[row][col] == '_':
            board[row][col] = 'O'
        else:
            print("Cell is already occupied. Try again.")
            continue

        print_board(board)

        
        if evaluate(board) == -10:
            print("You win!")
            break

       
        if not is_moves_left(board):
            print("It's a draw!")
            break

     
        print("AI is making a move...\n")
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = 'X'
        print_board(board)

        
        if evaluate(board) == 10:
            print("AI wins!")
            break

       
        if not is_moves_left(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
