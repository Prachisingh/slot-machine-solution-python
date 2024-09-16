from os.path import exists

from GameConfiguration import GameConfiguration
from WinData import WinData
import random as rd

w = WinData()
stop_position_list = []
slot_face =[]

reels = GameConfiguration.get_reels()

def select_reels(board_height, reel, stop_pos):
    board_reels = []
    for i in range(0, board_height):
        board_reels.insert(i, reel[(stop_pos + i) % reel.__len__()])
    return board_reels

for i in reels:
    stop_position = rd.randint(0, reels.get(i).__len__() - 1)  # stop position for multiple wins [3, 14, 10, 19, 13]
    slotFaceReel = select_reels(GameConfiguration.BoardHeight, reels.get(i), stop_position)
    stop_position_list.insert(i, stop_position)
    slot_face.insert(i, slotFaceReel)


def check_for_win_combination(sym_to_compare, slot_face):
    win_data = WinData()
    pos_list = []
    current_col = 0
    sym_count_per_col_map = {}
    for col in range(0, GameConfiguration.BoardWidth):
        sym_count_per_column = 0
        pos = col
        if col - current_col > 1:
            break
        for row in range(0, GameConfiguration.BoardHeight):
            current_sym = slot_face[col][row]
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

    symbol_win = 0
    ways = 1
    if pay_out is not None and win_data.sym_count_on_each_col.__len__() >= pay_out.minimum_match:
        symbol_win = pay_out.get_win_amount(win_data.sym_count_on_each_col.__len__())
        for i in range(0, win_data.sym_count_on_each_col.__len__()):
            ways *= win_data.sym_count_on_each_col[i]

        final_win = symbol_win * ways
        win_data.win_amount = final_win * stake
        win_data.ways = ways
    else:
        win_data.win_amount = 0

def calculate_win(slot_face, stake):
    win_data_list = []
    total_win = 0
    for row in range(0, GameConfiguration.BoardHeight):
        sym_to_compare = slot_face[0][row]
        exist = False
        for sym in win_data_list: # TODO
            if sym.symbol_name == sym_to_compare:
                exist = True

        if win_data_list.__len__() != 0 and exist:
            continue
        win_data = check_for_win_combination(sym_to_compare, slot_face)
        populate_win(win_data, stake)
        if win_data.win_amount != 0:
            total_win += win_data.win_amount
            win_data_list.append(win_data)

    print("Total wins: " + str(total_win))
    for win in win_data_list :
        print("- Ways win " + str(win.pos_list) + " " + win.symbol_name + " X" + str(win.sym_count_on_each_col.__len__()) + ", " + str(win.win_amount) + ", Ways: " + str(win.ways) + " ")


print("Stop Positions: " )
print(stop_position_list)
print()
print("Screen:")

for row in range(0, GameConfiguration.BoardHeight):
    for col in range(0, GameConfiguration.BoardWidth):
        print(slot_face.__getitem__(col).__getitem__(row), end=' ')
    print()

calculate_win(slot_face, GameConfiguration.Stake)

