
class ConnectGame:
    def __init__(self, board):
        self.winner=""
        self.win_x(board)
        self.win_y(board)

    def get_winner(self):
        return self.winner

    def win_x(self,board):
        board=board.replace(" ","").split("\n")

        #coordenadas de todos las X
        x_side=[]
        for row,letter in enumerate(board):
            if letter[0]=="X":
                x_side.append([0,row])

        if self.follow_x_path(x_side,board,[]):
            self.winner="X"
        

    def follow_x_path(self,coords,board,pasados):
        #movimientos permitidos
        movimientos_p=[[0,1],[0,-1],[1,-1],[1,0],[-1,1],[-1,0]]
        #ancho y alto en indices
        ancho_board,alto_board=len(board[0]),len(board)
        #iterar en la lista de coordenadas dado
        revisar=[]
        for coord in coords:
            x,y=coord
            pasados.append(coord)
            #probar si existe el item a los alrededores
            for mov in movimientos_p:
                x_t,y_t=mov
                x_t+=x
                y_t+=y

                if x_t+1>ancho_board:
                    return True
                
                if 0<=x_t<ancho_board and 0<=y_t<alto_board:
                    if board[y_t][x_t]=="X":
                        
                        if [x_t,y_t] not in revisar and [x_t,y_t] not in pasados:
                            revisar.append([x_t,y_t])
                        
        if len(revisar)==0:
            return False
        return self.follow_x_path(revisar,board,pasados)

    def win_y(self,board):
        board=board.replace(" ","").split("\n")
        [print(item) for item in board]

        #coordenadas de todos las Y
        y_side=[]
        print(board[0])
        for column,letter in enumerate(board[0]):
            if letter=="O":
                y_side.append([column,0])

        if self.follow_y_path(y_side,board,[]):
            self.winner="O"

    def follow_y_path(self,coords,board,pasados):
        #movimientos permitidos
        movimientos_p=[[0,1],[0,-1],[1,0],[-1,0],[-1,1],[1,-1]]
        #ancho y alto en indices
        ancho_board,alto_board=len(board[0]),len(board)
        print(f"- - {ancho_board}x{alto_board} - -")
        #iterar en la lista de coordenadas dado
        revisar=[]
        for coord in coords:
            x,y=coord
            print(coord)
            pasados.append(coord)
            #probar si existe el item a los alrededores
            for mov in movimientos_p:
                x_t,y_t=mov
                x_t+=x
                y_t+=y
                print(f"--- {x_t,y_t}")
                if y_t+1>alto_board:
                    print(x_t,y_t)
                    return True
                
                if 0<=x_t<ancho_board and 0<=y_t<alto_board:
                    if board[y_t][x_t]=="O":
                        
                        if [x_t,y_t] not in revisar and [x_t,y_t] not in pasados:
                            print(f"--- {x_t,y_t}")
                            revisar.append([x_t,y_t])
                        
        if len(revisar)==0:
            return False
        return self.follow_y_path(revisar,board,pasados)
            
        
