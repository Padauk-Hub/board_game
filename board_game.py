import os
from check import Check

class Board_game:
    def __init__(self,r,c,w):
        self.no_of_row = r
        self.no_of_col = c
        self.window_size = w
        self.player_1_term = True
        self.create_board()
        self.index_view()

    def index2point(self,index):
        # Row major indexed
        r = index // self.no_of_col
        c = index % self.no_of_col
        return r,c

    def point2index(self,row,col):    
        return row * self.no_of_col + col
    def index_view(self):
        self.index_board = [[r*self.no_of_col+c  for c in range(self.no_of_col)] for r in range(self.no_of_row)]
    def create_board(self):
        self.board = [[' ' for _ in range(self.no_of_col)] for _ in range(self.no_of_row)]

    def  change_player(self):
        if self.player_1_term:
            self.player_1_term = False
        else:
            self.player_1_term = True

    def make_move(self,r,c,ch):
        if r<0 or r>= self.no_of_row or c<0 or c >= self.no_of_col:
            print('Out of the board')
            return False
        if self.board[r][c] != ' ':
            print('This place is token')
            return False
        self.board[r][c] = ch
        return True
    def game(self):
        self.show2()
        m = 0
        while m < self.no_of_row*self.no_of_col:
            if self.player_1_term:
                ch = 'X'
            else:
                ch = 'O'
            print(f'Player {ch} Turn')
            i = int(input('Enter point you choose: '))
            r,c = self.index2point(i)
            sucess_move = self.make_move(r,c,ch)
            if sucess_move:
                check_obj = Check(self.board,i,self.window_size)
                if check_obj.check_win(ch):
                    print(f'Player {ch} win')
                    break
                self.show2()
                self.change_player() 
    def show(self):
        _ = os.system('clear')
        #print('\n'.join(map(str,self.index_board)))
        print('\n'.join(map(lambda line:'|'.join(map(lambda x: str(x).center(3),line)),self.index_board)))
        horizontal_line ='\n--'+'|---' * (self.no_of_col-1)+'\n'
        print(horizontal_line.join([" | ".join(self.board[r]) for r in range(self.no_of_row)]))
    
    def show2(self):
        _ = os.system('clear')
        for r in range(self.no_of_row):
            line = ''
            for c in range(self.no_of_col):
                if self.board[r][c] == ' ':
                    line += str(r*self.no_of_col+c).center(3)+"|"
                else:
                    line += str(self.board[r][c]).center(3)+"|"
            print(line)
if __name__=='__main__':
    n,m = 9,9
    board = Board_game(n,m)
    print("Game Start")
    board.game()
