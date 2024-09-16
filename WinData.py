

class WinData:

    def __init__(self):
        self.__ways = None
        self.__sym_count_on_each_col = None
        self.__win_amount = None
        self.__pos_List = None
        self.__symbol_name = None

    @property
    def symbol_name(self):
        return self.__symbol_name

    @symbol_name.setter
    def symbol_name(self, new_value):

        self.__symbol_name = new_value

    @property
    def pos_list(self):
        return self.__pos_List

    @pos_list.setter
    def pos_list(self, new_value):
        self.__pos_List= new_value


    @property
    def win_amount(self):
        return self.__win_amount

    @win_amount.setter
    def win_amount(self, new_value):
        self.__win_amount = new_value


    @property
    def sym_count_on_each_col(self):
        return self.__sym_count_on_each_col

    @sym_count_on_each_col.setter
    def sym_count_on_each_col(self, new_value):
        self.__sym_count_on_each_col = new_value

    @property
    def ways(self):
        return self.__ways

    @ways.setter
    def ways(self, new_value):
        self.__ways= new_value