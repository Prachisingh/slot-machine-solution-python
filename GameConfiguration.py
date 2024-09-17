from SlotSymbolWaysPayConfig import SlotSymbolWaysPayConfig


class GameConfiguration:

    STAKE = 1
    BOARD_HEIGHT = 3
    BOARD_WIDTH = 5

    @staticmethod
    def get_pay_out():
        d = {'sym1' : SlotSymbolWaysPayConfig(3, [1, 2, 3]),
             'sym2' : SlotSymbolWaysPayConfig(3, [1, 2, 3]),
             'sym3' : SlotSymbolWaysPayConfig(3, [1, 2, 5]),
             'sym4' : SlotSymbolWaysPayConfig(3, [2, 5, 10]),
             'sym5' : SlotSymbolWaysPayConfig(3, [5, 10, 15]),
             'sym6' : SlotSymbolWaysPayConfig(3, [5, 10, 15]),
             'sym7' : SlotSymbolWaysPayConfig(3, [5, 10, 20]),
             'sym8' : SlotSymbolWaysPayConfig(3, [10, 20, 50])
             }
        return d

    @staticmethod
    def get_reels():

        d = {
            0 : ["sym2", "sym7", "sym7", "sym1", "sym1", "sym5", "sym1", "sym4", "sym5", "sym3", "sym2", "sym3", "sym8", "sym4", "sym5", "sym2", "sym8", "sym5", "sym7", "sym2"],
            1:  ["sym1", "sym6", "sym7", "sym6", "sym5", "sym5", "sym8", "sym5", "sym5", "sym4", "sym7", "sym2", "sym5", "sym7", "sym1", "sym5", "sym6", "sym8", "sym7", "sym6", "sym3", "sym3", "sym6", "sym7", "sym3"],
            2 : ["sym5", "sym2", "sym7", "sym8", "sym3", "sym2", "sym6", "sym2", "sym2", "sym5", "sym3", "sym5", "sym1", "sym6", "sym3", "sym2", "sym4", "sym1", "sym6", "sym8", "sym6", "sym3", "sym4", "sym4", "sym8", "sym1", "sym7", "sym6", "sym1", "sym6"],
            3 : ["sym2", "sym6", "sym3", "sym6", "sym8", "sym8", "sym3", "sym6", "sym8", "sym1", "sym5", "sym1", "sym6", "sym3", "sym6", "sym7", "sym2", "sym5", "sym3", "sym6", "sym8", "sym4", "sym1", "sym5", "sym7"],
            4 : ["sym7", "sym8", "sym2", "sym3", "sym4", "sym1", "sym3", "sym2", "sym2", "sym4", "sym4", "sym2", "sym6", "sym4", "sym1", "sym6", "sym1", "sym6", "sym4", "sym8"]
        }
        return d


