from tabulate import tabulate

def print_board(board):
    print(tabulate(board, tablefmt="grid"))

def take_user_turn(sign):
    user_input = input("{} user turn. enter row and column number (e.g. 1 2)".format(sign)).split(" ")
    print (user_input[0], user_input[1])
    try:
        return (int(user_input[0]), int(user_input[1]))
    except:
        print("wrong board coordinates X:{}, O:{}".format(user_input[0] if user_input[0] else "wrong value", user_input[1] if user_input[1] else "wrong value"))
        return take_user_turn(sign)

def set_cell_value(board, value, coordinates):
    print (coordinates)
    x, y = coordinates
    if board[x][y] == "*":
        board[x][y] = value
    else: 
        print("cell already accupied")

def check_result(board, sign):
    winning_combinations = [[(0, 0), (0, 1), (0, 2)],
                            [(1, 0), (1, 1), (1, 2)],
                            [(2, 0), (2, 1), (2, 2)],
                            [(0, 0), (1, 0), (2, 0)],
                            [(0, 1), (1, 1), (2, 1)],
                            [(0, 2), (1, 2), (2, 2)],
                            [(0, 0), (1, 1), (2, 2)],
                            [(2, 0), (1, 1), (0, 2)]]

    for combination in winning_combinations:
        if all([board[item[0]][item[1]] == sign for item in combination]):
            print("the winner is " + sign)
            return sign

def game_round(board, sign):
    set_cell_value(board, sign, take_user_turn(sign))
    print_board(board)
    return check_result(board, sign)

def tic_tac_toe():
    winner = None
    board = [
    [ "*", "*", "*"],
    [ "*", "*", "*"],
    [ "*", "*", "*"]
    ]
    while not winner and any([item == "*" for sublist in board for item in sublist]):
        winner = game_round(board, 'X')
        if not winner:
            winner = game_round(board, 'O')
            print (winner)
        


if __name__ == "__main__":
    tic_tac_toe()
