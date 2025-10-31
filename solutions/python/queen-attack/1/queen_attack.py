class Queen:
    def __init__(self, row, column):
        if row < 0:
            raise ValueError("row not positive")
        if row not in range(8):
            raise ValueError("row not on board")
        if column < 0:
            raise ValueError("column not positive")
        if column not in range(8):
            raise ValueError("column not on board")
            
        self.row = row
        self.column = column
        
        
        

    def can_attack(self, another_queen):
        row_fore = another_queen.row
        column_fore = another_queen.column

        if self.row == row_fore and self.column == column_fore:
            raise ValueError("Invalid queen position: both queens in the same square")

        if self.row == row_fore or self.column == column_fore:
            return True

        if (row_fore,column_fore) in cells_attack(self.row,self.column):
            return True

        print((row_fore,column_fore))
        print(cells_attack(self.row,self.column))
        return False

def cells_attack(row,column):
    out=[]

    #LEFT TOP
    row_temp=row
    column_temp=column
    while 7>=row_temp>=0 and 7>=column_temp>=0:
        row_temp-=1
        column_temp-=1
        out.append((row_temp,column_temp))

    #LEFT BOTTOM
    row_temp=row
    column_temp=column
    while 7>=row_temp>=0 and 7>=column_temp>=0:
        row_temp+=1
        column_temp-=1
        out.append((row_temp,column_temp))

    #RIGHT TOP
    row_temp=row
    column_temp=column
    while 7>=row_temp>=0 and 7>=column_temp>=0:
        row_temp-=1
        column_temp+=1
        out.append((row_temp,column_temp))

    #RIGHT BOTTOM
    row_temp=row
    column_temp=column
    while 7>=row_temp>=0 and 7>=column_temp>=0:
        row_temp+=1
        column_temp+=1
        out.append((row_temp,column_temp))

    return out