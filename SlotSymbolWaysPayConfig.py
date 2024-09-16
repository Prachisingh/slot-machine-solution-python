class SlotSymbolWaysPayConfig:

    @property
    def minimumMatch(self):
        return self.__minimumMatch

    @property
    def win_amount(self):
        return self.__win_amount

    def __init__(self, minimumMatch, win_amount):
        self.__minimumMatch = minimumMatch
        self.__win_amount = win_amount

    def get_win_amount(self, matched_columns_count):
        if matched_columns_count < self.__minimumMatch:
            return 0
        if matched_columns_count - self.__minimumMatch == 0:
            return self.__win_amount[0]
        elif matched_columns_count - self.__minimumMatch == 1:
            return self.__win_amount[1]
        else:
            return self.__win_amount[2]



