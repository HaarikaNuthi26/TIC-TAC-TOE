#Initial game board
def initial_board():
    print("      |       |      ")
    print("  1  |  2   |  3   ")
    print("---- | ---- | ----")
    print("  4  |  5   |  6   ")
    print("---- | ---- | ----")
    print("  7  |  8   |  9   ")
    print("      |       |      ")

#Function to print board
def print_board(board):
    print("\n")
    print(f"\t  {board[0]}  |  {board[1]}  |  {board[2]}  ")
    print("\t-----|-----|-----")
    print(f"\t  {board[3]}  |  {board[4]}  |  {board[5]}  ")
    print("\t-----|-----|-----")
    print(f"\t  {board[6]}  |  {board[7]}  |  {board[8]}  ")    
    print("\n")
    
#Function to print the game instructions
def instructions():
    print("WELCOME TO TIC TAC TOE GAME")
    print("\n_____INSTRUCTIONS_____")
    print("Following is the game board")
    initial_board()
    print("1. Player has to choose the symbol")
    print("2. Player 1 has to choose a number from range 1-9")
    print("3. Player 2 has to do the same")
    print("Player who places either 'X' or 'O' in a row or column or diagonal wins the game")
    print("Repeat the same until win or draw\n")

#Function to check the winner after every move
def check_winner(board, player):
    #winning conditions
    win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

#Function to check if the game is a tie
def check_draw(board):
    if "-" not in board:
        print_board(board)
        print("It's a tie...!!!")
        return True
    return False

#Function to get the player input
def get_ply_input(board, current_ply):
    while True:
        print(f"{current_ply} it's your turn")
        move = int(input("Enter a number (1-9): "))
        #move conditions
        if 1 <= move <= 9 and board[move - 1] == "-":
            return move - 1
        else:
            print("Invalid move...!! Please choose a valid position")
            print("\n")

#Function to switch the player
def switch_player(current_ply):
    return "O" if current_ply == "X" else "X"

#Function to read player details and choose the player symbol
def choose_symbol():
    symbol = {}
    ply1 = input("Enter the name of player 1: ")
    ply2 = input("Enter the name of player 2: ")
    print("Enter 1 for 'X'\nEnter 2 for 'O'.")
    choice = int(input(f"{ply1} choose your symbol (1 or 2): "))
    symbol[ply1] = "X" if choice == 1 else "O"
    symbol[ply2] = "O" if choice == 1 else "X"
    return symbol, ply1

#Game loop function
def tic_tac_toe():
    instructions()
    symbol, current_ply = choose_symbol()
    board = ["-" for _ in range(9)]
    #assign values to players
    player1, player2 = symbol.keys()
    
    while True:
        print_board(board)
        #Call the function get_ply_input
        move = get_ply_input(board, current_ply)
        #If the move is valid then update the board
        board[move] = symbol[current_ply]
        #After every move checks for the winner
        if check_winner(board, symbol[player1]):
            print_board(board)
            print(f"{player1} wins the game!")
            break
        #Check for the tie
        if check_draw(board):
            break
        #switch players
        current_ply = player2 if current_ply == player1 else player1
        #After every move checks for the winner
        if check_winner(board, symbol[player2]):
            print_board(board)
            print(f"{player2} wins the game!")
            break
        #Check for the tie
        if check_draw(board):
            break

#Main function 
if __name__ == "__main__":
    tic_tac_toe()
