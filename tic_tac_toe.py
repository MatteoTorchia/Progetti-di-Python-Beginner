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
            print("Error: You inserted an illegal value. Try again.\n")
            continue

        if move < 1 or move > 9:
            print("Error: The number must be between 1 and 9. Try again.\n")
            continue
        
        index = move - 1
        row_index = index // 3
        col_index = index % 3
        if board[row_index][col_index] == "X" or board[row_index][col_index] == "O":
            print("This square is already taken! Try a different one.\n")
            continue
        board[row_index][col_index] = "O"
        return board

# this is my vers that doesn't return a list of tuples but a list of ints
# free_fields = []
# def make_list_of_free_fields(board):
#     free_fields.clear()
#     for i in board:
#         for j in i:
#             if type(j) == str:
#                 continue
#             else:
#                 free_fields.append(j)
#     return free_fields

def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if type(board[row][col]) == int:
                free_fields.append((row, col))
                
    return free_fields


# --- Main Flow ---
make_list_of_free_fields(board)
display_board(board)
enter_move(board)

make_list_of_free_fields(board)
display_board(board)
enter_move(board)

make_list_of_free_fields(board)
display_board(board)
enter_move(board)

make_list_of_free_fields(board)
display_board(board)
enter_move(board)

make_list_of_free_fields(board)
display_board(board)
enter_move(board)

make_list_of_free_fields(board)
display_board(board)
enter_move(board)

make_list_of_free_fields(board)
display_board(board)
enter_move(board)

make_list_of_free_fields(board)
display_board(board)
enter_move(board)
