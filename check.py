class Check:
    def __init__(self,board,index,w):
        self.board = board
        self.window_size = w
        self.index = index

        self.no_of_row = len(board)
        self.no_of_col = len(board[0])
        self.index2point(index)
        self.lines = []
        self.moves = []

    def index2point(self,index):
        # Row major indexed
        self.row = index // self.no_of_col
        self.col = index % self.no_of_col

    def point2index(self,row,col):    
        return row * self.no_of_col + col

    def horizonatal(self):
        line = [(self.row,c) for c in range(self.no_of_col)] 
        self.lines.append(line)
    
    def vertical(self):
        line = [(r,self.col) for r in range(self.no_of_row)]
        self.lines.append(line)

    def diagonal(self):
        l = min(self.row,self.col)
        u = min(self.no_of_row - self.row,self.no_of_col - self.col)
        d = self.row - self.col
        line = []
        for i in range(self.row-l,self.row+u):
            line.append((i,i-d))
        self.lines.append(line)

    def anti_diagonal(self):
        s = self.row + self.col

        if s < self.no_of_row:
            row_end = s
        else: 
            row_end = self.no_of_row -1
        
        col_end = s - row_end
        step = min(row_end+1,self.no_of_col-col_end)
        line = []
        for i in range(row_end,row_end-step,-1):
            line.append((i,s-i))
        self.lines.append(line)

    def n_gram(self,line):
        w = self.window_size

        n = line.index((self.row,self.col)) 
        l = max(0,n-w+1)
        u = min(len(line),n+w)

        for i in range(l,u-w+1):
            self.moves.append(line[i:i+w])


    def windows(self):
        # check
        self.horizonatal()
        self.vertical()
        self.diagonal()
        self.anti_diagonal()

        for line in self.lines:
            #print(line)
            self.n_gram(line)
            #print(line)
        #print(self.moves)
        #print(list(map(lambda p: self.point2index(p[0],p[1]),self.moves)))
    
    def show_info(self):
        print('\n'.join(map(str,self.board)))
        print(f'There are {self.no_of_row} rows and {self.no_of_col} columns')
        print(f'The index is {self.index} and it represent ({self.row},{self.col}) point')
        print('The lines that pass the point are')
        for line in self.lines:
            print(list(map(lambda p: self.point2index(p[0],p[1]),line)))
        print('The Window that contain are')
        for line in self.moves:
            print(list(map(lambda p: self.point2index(p[0],p[1]),line)))

    def check_win(self,ch):
        """
        moves => 2d array, that contain the winning moves(1d array)
        ch => target character
        return <= boolen
        """
        self.windows()
        return any(map(lambda arr: all(map(lambda x: self.board[x[0]][x[1]]==ch,arr)),self.moves))

if __name__ == '__main__':
    board = [['x','o','',''],['','x','o',''],['','','x','']]
    #n,m = 3,3
    #board = [[r*m+c for c in range(m)] for r in range(n)]
    index = 4
    check_obj = Check(board,index,3)
    print(check_obj.check_win('x'))
    check_obj.show_info()
