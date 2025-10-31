# Globals for the directions
# Change the values as you see fit
EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction=direction
        self.coordinates=(x_pos,y_pos)
        
    def move(self,cad):
        for letter in cad:
            if letter in ["R","L"]:
                self.girar(letter)

            if letter == "A":
                self.mover()

    def girar(self,sentido):
        rosa=[NORTH,EAST,SOUTH,WEST]
        
        idx=rosa.index(self.direction)
        
        if sentido=="R":
            idx+=1
            if idx>3:
                idx=0
        else:
            idx-=1

        self.direction=rosa[idx]
    def mover(self):
        x,y=self.coordinates
        if self.direction==NORTH:
            y+=1
        if self.direction==SOUTH:
            y-=1
        if self.direction==EAST:
            x+=1
        if self.direction==WEST:
            x-=1
        self.coordinates=(x,y)