class Cell:

    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        pass
    def set_cell_value(self, value):
        self.value = value
    def set_sketched_value(self,value):
        self.sketched_value = value
    def draw(self):
        #draws this cell, along with the value inside it
        if self.value != 0:
            #If this cell has a nonzero value, that value is displayed
            return self.value
        else:
            pass
