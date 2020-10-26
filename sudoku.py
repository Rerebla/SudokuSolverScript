# %%
from math import floor as f
GAME_BOARD = [[10, 0, 0, 4, 0, 0, 1, 2, 0],
              [6, 0, 0, 0, 7, 5, 0, 0, 9],
              [0, 0, 0, 6, 0, 1, 0, 7, 8],
              [0, 0, 7, 0, 4, 0, 2, 6, 0],
              [0, 0, 1, 0, 5, 0, 9, 3, 0],
              [9, 0, 4, 0, 6, 0, 0, 0, 5],
              [0, 7, 0, 3, 0, 0, 0, 1, 2],
              [1, 2, 0, 0, 0, 7, 4, 0, 0],
              [0, 4, 9, 2, 0, 6, 0, 0, 7]
              ]


def main():
    print_board(GAME_BOARD)
    solver(GAME_BOARD)
    print("\n")
    print_board(GAME_BOARD)
    is_solvable = True
    for i in range(0, 9):
        if GAME_BOARD[i].count(0) >= 1:
            is_solvable = False
    if not is_solvable:
        print("Input was probably unsolvable/false")
    else:
        print("(probably) Solved!")


def print_board(game_board):
    for i in range(len(game_board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(game_board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(game_board[i][j])
            else:
                print(str(game_board[i][j]) + " ", end="")


def solver(game_board):
    find = find_empty(game_board)
    if not find:
        return True
    for i in range(1, 10):
        if check_if_valid(game_board, find[0], find[1], i):
            game_board[find[0]][find[1]] = i
            if solver(game_board):
                return True
            game_board[find[0]][find[1]] = 0
    return False


def find_empty(game_board):
    for i in range(0, 9):
        for j in range(0, 9):
            if game_board[i][j] == 0:
                return (i, j)  # vertical, horizontal
    return False


def check_if_valid(game_board, position_y, position_x, num):
    all_numbers = find_all_related_numbers(game_board, position_y, position_x)
    if all_numbers.count(num) >= 1:
        return False
    else:
        return True


def find_all_related_numbers(game_board, position_y, position_x):
    output = []
    output += find_numbers_in_row(game_board, position_y)
    output += find_numbers_in_column(game_board, position_x)
    output += find_numbers_in_cell(game_board, position_y, position_x)
    return output


def find_numbers_in_row(game_board, position_y):
    return game_board[position_y]


def find_numbers_in_column(game_board, position_x):
    output = []
    for i in range(0, 9):
        output.append(game_board[i][position_x])
    return output


def find_numbers_in_cell(game_board, position_y, position_x):
    cell = position_to_cell(position_y, position_x)
    output = []
    start_pos_y = cell[0] * 3
    start_pos_x = cell[1] * 3
    for row in range(start_pos_y, start_pos_y + 3):
        for column in range(start_pos_x, start_pos_x + 3):
            output.append(game_board[row][column])
    return output


def position_to_cell(position_y, position_x):
    output = []
    position_y /= 3
    position_x /= 3
    position_y = f(position_y)
    position_x = f(position_x)
    output.append(position_y)
    output.append(position_x)
    return output


main()
