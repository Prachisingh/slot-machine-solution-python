from GameConfiguration import GameConfiguration
from WinData import WinData
import random as rd

stop_position_list = []
slot_face = []

reels = GameConfiguration.get_reels()

def select_reels(board_height, reel, stop_pos):
    board_reels = []
    for i in range(0, board_height):
        board_reels.insert(i, reel[(stop_pos + i) %  len(reel)])
    return board_reels

for i in reels:
    stop_position = rd.randint(0, len(reels.get(i)) - 1)  # stop position for multiple wins [3, 14, 10, 19, 13]
    slot_face_reel = select_reels(GameConfiguration.BOARD_HEIGHT, reels.get(i), stop_position)
    stop_position_list.insert(i, stop_position)
    slot_face.insert(i, slot_face_reel)


def check_for_win_combination(sym_to_compare, board):
    win_data = WinData()
    pos_list = []
    current_col = 0
    sym_count_per_col_map = {}
    for col in range(0, GameConfiguration.BOARD_WIDTH):
        sym_count_per_column = 0
        pos = col
        if col - current_col > 1:
            break
        for row in range(0, GameConfiguration.BOARD_HEIGHT):
            current_sym = board[col][row]
            if sym_to_compare == current_sym:
                sym_count_per_column = sym_count_per_column +1

                if sym_count_per_col_map.__contains__(col):
                    sym_count_per_col_map.pop(col)
                    sym_count_per_col_map[col] = sym_count_per_column
                else:
                    sym_count_per_col_map[col] = sym_count_per_column

                pos_list.append(pos)
                current_col = col
            pos += 5

    win_data.pos_list = pos_list
    win_data.sym_count_on_each_col = sym_count_per_col_map
    win_data.symbol_name = sym_to_compare
    return win_data


def populate_win(win_data, stake):
    pay_out = GameConfiguration.get_pay_out()[win_data.symbol_name]
    ways = 1
    if pay_out is not None and len(win_data.sym_count_on_each_col) >= pay_out.minimum_match:
        symbol_win = pay_out.get_win_amount(len(win_data.sym_count_on_each_col))
        for i in range(0, len(win_data.sym_count_on_each_col)):
            ways *= win_data.sym_count_on_each_col[i]

        final_win = symbol_win * ways
        win_data.win_amount = final_win * stake
        win_data.ways = ways
    else:
        win_data.win_amount = 0

def calculate_win(board, stake):
    win_data_list = []
    total_win = 0
    for row in range(0, GameConfiguration.BOARD_HEIGHT):
        sym_to_compare = board[0][row]
        exist = False
        for sym in win_data_list: # TODO
            if sym.symbol_name == sym_to_compare:
                exist = True

        if len(win_data_list) != 0 and exist:
            continue
        win_data = check_for_win_combination(sym_to_compare, board)
        populate_win(win_data, stake)
        if win_data.win_amount != 0:
            total_win += win_data.win_amount
            win_data_list.append(win_data)

    print("Total wins: " + str(total_win))
    for win in win_data_list :
        print("- Ways win " + str(win.pos_list) + " " + win.symbol_name + " X" + str(len(win.sym_count_on_each_col)) + ", " + str(win.win_amount) + ", Ways: " + str(win.ways) + " ")


print("Stop Positions: " + str(stop_position_list) )
print()
print("Screen:")

for row in range(0, GameConfiguration.BOARD_HEIGHT):
    for col in range(0, GameConfiguration.BOARD_WIDTH):
        print(slot_face.__getitem__(col).__getitem__(row), end=' ')
    print()

calculate_win(slot_face, GameConfiguration.STAKE)

