print('Minesweeper using python')
print()
import random
import re
class Board:
    def __init__(self,dim_size,num_bombs):
        self.dim_size=dim_size
        self.num_bombs=num_bombs
        self.dug=set()  #empty set
        self.board=self.make_new_board()  #helper function
        self.assign_values_to_board()

    def make_new_board(self):   #for planting the bomb *
        board=[[None for _ in range(self.dim_size)]for _ in range(self.dim_size)]
        bombs_planted=0  #initial value
        while bombs_planted<self.num_bombs:
            loc=random.randint(0,self.dim_size**2-1)
            row=loc//self.dim_size  #for finding row
            col=loc%self.dim_size   #for finding column
            if board[row][col]=='*':   #bomb is already planted
                continue
            board[row][col]='*'   #if not,then we plant bomb
            bombs_planted += 1  #increment
        return board

    def assign_values_to_board(self):  #for assigning the bombs
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c]=='*':
                    continue
                self.board[r][c]=self.get_num_neighboring_bombs(r,c)

    def get_num_neighboring_bombs(self,row,col):  #to get bombs in assign_value_to_board function
    # Top Left(r-1,c-1)   Here r = row and c = column
    # Top middle(r-1,c)
    # Top right(r-1,c+1)
    # Left(r,c-1)
    # Right(r,c+1)
    # Bottom Left(r+1,c-1)
    # Bottom Middle(r+1,c)
    # Bottom Right(r+1,c+1)
        num_neighboring_bombs=0  #initial value
        for r in range(max(0,row-1),min(self.dim_size-1,row+1)+1): #Top Left to Bottom Right #If we go below 1st bound,we take 0 as bound
            for c in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1): #Here (self.dim_size-1) means maximum size from board
                if r==row and c==col:  #our orihinal location,no need to check
                    continue
                if self.board[r][c]=='*':
                    num_neighboring_bombs+=1  #increment
        return num_neighboring_bombs

    def dig(self, row, col):
        # dig at that location!
        # return True if successful dig, False if bomb dug

        # a few scenarios:
        # hit a bomb -> game over
        # dig at location with neighboring bombs -> finish dig
        # dig at location with no neighboring bombs -> recursively dig neighbors!

        self.dug.add((row, col))  # keep track that we dug here

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        # self.board[row][col] == 0
        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1):
                if (r, c) in self.dug:
                    continue  # don't dig where you've already dug
                self.dig(r, c)

        # if our initial dig didn't hit a bomb, we *shouldn't* hit a bomb here
        return True

    def __str__(self):
        # this is a magic function where if you call print on this object,
        # it'll print out what this function returns!
        # return a string that shows the board to the player

        # first let's create a new array that represents what the user would see
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key=len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-' * str_len + '\n' + string_rep + '-' * str_len

        return string_rep

def play(dim_size=8,num_bombs=8): #to play the game
    board=Board(dim_size,num_bombs)#object board gets created
    safe=True
    while len(board.dug)<board.dim_size**2-num_bombs:
        print(board)
        user_input=re.split(',(\\s)*',input('Where would you like to dig? Input as row,col :'))
        row,col=int(user_input[0]),int(user_input[-1])
        if row<0 or row>=board.dim_size or col<0 or col>=board.dim_size:
            print('Invalid location,Try again')
            continue #for continuing the loop
        safe=board.dig(row,col) #if its valid,we dig
        if not safe:
            break # game is over
        #2 ways to end loop,lets check which one
    if safe:
        print('CONGRATULATIONS!!!YOU ARE VICTORIOUS!')
    else:
        print('SORRY GAME OVER:(')
        board.dug=[(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]  #to reveal the whole board
        print(board)
if __name__=='__main__':  #good practice
    play()



