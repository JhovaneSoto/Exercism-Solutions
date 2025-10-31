WHITE="W"
BLACK="B"
NONE="N"
class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self.board=board
        self.owners={}
        self.territories()

    def territory(self, x, y):
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        alto=len(self.board)
        ancho=len(self.board[0])
        if not(0<=x<ancho and 0<=y<alto):
            raise ValueError("Invalid coordinate")
        for llave in self.owners.keys():
            for region in self.owners[llave]:
                
                if (x,y) in region:
                    return llave,set(region)
        return NONE,set()

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        #definir las regiones existentes
        coords_none=[(x,y) for y in range(len(self.board)) for x in range(len(self.board[y])) if self.board[y][x]==" "]
        regiones=[]
        for coord in coords_none:
            if coord not in [item for reg in regiones for item in reg]:
                region=find_territory(coord,self.board,[])
                
                if region not in regiones:
                    regiones.append(region)
        owners={}
        for region in regiones:
            owner=region_owner(region,self.board)
            if owner not in owners.keys():
                owners[owner]=[region]
            else:
                owners[owner]+=[region]
        self.owners=owners
        out={
            BLACK:set(),
            WHITE:set(),
            NONE:set()
        }
        for owner in owners.keys():
            out[owner]|=set([item for region in owners[owner] for item in region])
      
        return out
        
            
def find_territory(coord,board,forbidden):
    x,y=coord
    alto=len(board)
    ancho=len(board[0])
    out=[coord]
    delta_x,delta_y = 0, -1
    for _ in range(4):
        if 0<=x+delta_x<ancho and 0<=y+delta_y<alto:
            if board[y+delta_y][x+delta_x]==" " and (x+delta_x,y+delta_y) not in forbidden:
                out+=find_territory((x+delta_x,y+delta_y),board,forbidden+out)
        delta_x,delta_y=-delta_y,delta_x
    return out

def region_owner(region,board):
    owner=NONE
    alto=len(board)
    ancho=len(board[0])
    delta_x,delta_y = 0, -1
    for coord in region:
        x,y=coord
        for _ in range(4):
            if 0<=x+delta_x<ancho and 0<=y+delta_y<alto:
                item=board[y+delta_y][x+delta_x]
                if item==" ":
                    continue
                if item=="B":
                    if owner==WHITE:
                        return NONE
                    owner=BLACK
                if item=="W":
                    if owner==BLACK:
                        return NONE
                    owner=WHITE
            delta_x,delta_y=-delta_y,delta_x
    return owner
