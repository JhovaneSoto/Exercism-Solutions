class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point({self.x},{self.y})"


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle=puzzle

    def search(self, word):
        candidates=[]
        for row in range(len(self.puzzle)):
            for column in range(len(self.puzzle[row])):
                if word[0]==self.puzzle[row][column]:
                    candidates.append((column,row))

        positions = find_words(self.puzzle,candidates,word)
        
        result = [item for item in positions if len(item) == len(word)]
        
        if len(result)!=0:
            return (result[0][0],result[0][-1])
        
def find_words(puzzle,candidates,word):
    clock = [
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, 1)
    ]
    candidates_out=[]
    for coord in candidates:
        for delta in clock:
            candidates_out.append(word_tracker(puzzle,word,coord,delta))
    return candidates_out

def word_tracker(puzzle,word,coord,delta):
    x,y = coord
    delta_x, delta_y = delta
    new_coord = (x+delta_x , y+delta_y)
    
    
    alto=len(puzzle)
    ancho=len(puzzle[0])

    
    if not (0<=x<ancho and 0<=y<alto) or word=="":
        return []

    if puzzle[y][x]==word[0]:
        return [Point(x,y)]+word_tracker(puzzle,word[1:],new_coord,delta)
    return []

    