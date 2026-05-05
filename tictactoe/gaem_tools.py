board = [
         ['-','-','-','-','-','-','-'],
         ['-','-','-','-','-','-','-'],
         ['-','-','-','-','-','-','-'],
         ['-','-','-','-','-','-','-'],
         ['-','-','-','-','-','-','-'],
         ['-','-','-','-','-','-','-'],
         ['-','-','-','-','-','-','-'],

        ]
#打印棋盘函数
def print_board(board):
    for row in board:
        print('  '.join(row))

#检查函数
def check_move(col, row, player):
    if not (1 <= col <= 7 and 1 <= row <= 7):
        print("超出棋盘范围，请输入1-7！")
        return False
    if board[row - 1][col - 1] != "-":
        print("这个位置已经有棋子了！")
        return False
    board[row - 1][col - 1] = player
    return True

#落子函数
def make_move():
    while True:
        while True:
            col,row =map(int,input('---------玩家1（x）---------\n请选择要落子的位置（列 , 行）：').replace(' ','').split(','))
            success = check_move(col,row,player= "x")
            if success:
                break
        print_board(board)

        while True:
            col, row = map(int, input('---------玩家2（o）---------\n请选择要落子的位置（列 , 行）：').split(','))
            success = check_move( col, row, player="o")
            if success:
                break
        print_board(board)

#判断胜负函数
def check_win(player):
    for x in range(7):
        for y in range(4):
            if board[x][y] ==board[x][y+1]==board[x][y+2]==board[x][y+3]==player :
                return True
    for y in range(7):
        for x in range(4):
            if board[x][y] ==board[x+1][y]==board[x+2][y]==board[x+3][y]==player :
                return True
    for y in range(4):
        for x in range(3,7):
            if board[x][y] == board[x+1][y-1] == board[x+2][y-2] == board[x+3][y-3] == player:
                return True
    return False

#判断棋局满不满
def check_full(board):
    for row in range(7):
        for col in range(7):
            if board[row][col] == "-":
                return False
    print("棋盘满了，平局了，再战一次吧！")
    return True

        