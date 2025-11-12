board = [
    [1, 2, 3],
    [4, "X", 6],
    [7, 8, 9]
]
# --- Functions ---
def display_board(board):
    for i in board:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print(f"|   {i[0]}   |   {i[1]}   |   {i[2]}   |")
        print("|       |       |       |")
    print("+-------+-------+-------+\n")

def enter_move(board):
    while True:
        move = input("Select a square between 1 and 9: ")
        try:
            move = int(move)
        except ValueError:
            print("Error: You inserted an illegal value. Try again")
        for i in board:
            for j in i:
                if move == j:
                    j = "O"
                    return board
        else:
            print("Error: You inserted an illegal value. Try again")   

def enter_move_WRONG(board):
    while True:
        move = input("Select a square between 1 and 9: ")
        try:
            for i in board:
                for j in i:
                    if move == j:
                        j = "O"
                        return board
            else:
                print("Error: You inserted an illegal value. Try again")
        except ValueError:
            print("Error: You inserted an illegal value.")
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.


# --- Main Flow ---
display_board(board)
enter_move(board)

display_board(board)
enter_move(board)

display_board(board)
enter_move(board)

display_board(board)
enter_move(board)

