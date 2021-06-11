  
class Cell:
    def __init__(self, x=0, y=0, dist=0):
        self.x = x
        self.y = y
        self.dist = dist

# block[] = board[x][y]
def inRange(x, y):
    if 0 <= x <= 7 and 0 <= y <= 7:
        return True
    return False


# isBlock(curr.x , curr.y , x , y)
def isBlock(currx , curry , x , y , board):
    # 0 0 >> 2 0 >> 2 1
    
    flg = False
    if(x == 1 and y == -2 and inRange(currx + x , curry + y)):
        if(board[currx + 1][curry] == '*' or board[currx + 1][curry - 1] == '*' or board[currx + 1][curry - 2] == '*'):
            flg = True
        
    if(x == 2 and y == -1 and inRange(currx + x , curry + y)):
        if(board[currx + 1][curry] == '*' or board[currx + 2][curry] == '*' or board[currx + 2][curry - 1] == '*'):
            flg = True
            
    if(x == 2 and y == 1 and inRange(currx + x , curry + y)):
        if(board[currx + 1][curry] == '*' or board[currx + 1][curry] == '*' or board[currx + 2][curry + 1] == '*'):
            flg = True
            
    if(x == 1 and y == 2 and inRange(currx + x , curry + y)):
        if(board[currx + 1][curry] == '*' or board[currx + 1][curry + 1] == '*' or board[currx + 1][curry + 2] == '*'):
            flg = True
            
    if(x == -1 and y == 2 and inRange(currx + x , curry + y)):
        if(board[currx - 1][curry] == '*' or board[currx - 1][curry + 1] == '*' or board[currx - 1][curry + 2] == '*'):
            flg = True
    
    if(x == -2 and y == 1 and inRange(currx + x , curry + y)):
        if(board[currx - 1][curry] == '*' or board[currx - 2][curry] == '*' or board[currx - 2][curry + 1] == '*'):
            flg = True
    
    if(x == -2 and y == -1 and inRange(currx + x , curry + y)):
        if(board[currx - 1][curry] == '*' or board[currx - 2][curry] == '*' or board[currx - 2][curry - 1] == '*'):
            flg = True
            
            
    if(x == -1 and y == -2 and inRange(currx + x , curry + y)):
        if(board[currx - 1][curry] == '*' or board[currx - 1][curry - 1] == '*' or board[currx - 1][curry - 2] == '*'):
            flg = True
    return flg




def play():

    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    queue = []
    Dict = {}
    board = [[0, 1, 2, 3, 4, 5, 6, 7],
            [8, 9, 10, 11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20, 21, 22, 23],
            [24, 25, 26, 27, 28, 29, 30, 31],
            [32, 33, 34, 35, 36, 37, 38, 39],
            [40, 41, 42, 43, 44, 45, 46, 47],
            [48, 49, 50, 51, 52, 53, 54, 55],
            [56, 57, 58, 59, 60, 61, 62, 63]]
            
    # to initail Vis
    Vis = [[False for i in range(0, 8)] for j in range(0, 8)]
    
    # to get src
    x = -1
    y = -1
 
    print("Enter x for src \n")
    x_src = int(input())
    print("Enter y for src \n")
    y_src = int(input())
    queue.append(Cell(x_src, y_src))
    
    print("Enter x for goal \n")
    x_goal = int(input())
    print("Enter y for goal \n")
    y_goal = int(input())
    dst = Cell(x_goal, y_goal)
    
    N = 0
    print("Enter Number Of Obstacles \n");
    N = int(input())
 
    for i in range(0 , N):
        print("Enter x for Obstacles \n")
        x = int(input())
        print("Enter y for Obstacles \n")
        y = int(input())
        board[x][y] = '*'
    
    
    if board[x_src][y_src] == board[x_goal][y_goal]:
        return 0
    
    while len(queue) > 0:
        curr = queue[0]
        queue.pop(0)
        if curr.x == dst.x and curr.y == dst.y:
            xx = curr.x
            yy = curr.y
            NN = curr.dist
            print("(" + str(xx) + ", " + str(yy) + ")")
            for i in range(0 , NN):
                parent = Dict[(xx,yy)]
                print(parent)
                xx , yy = parent
            return curr.dist
            
        for i in range(8):
            x = curr.x + dx[i]
            y = curr.y + dy[i]
            
            if inRange(x, y) and not isBlock(curr.x , curr.y , dx[i] , dy[i] , board) and not Vis[x][y]:
                Dict[x,y] = (curr.x,curr.y)
                #print(curr.x , curr.y , x , y)
                Vis[x][y] = True
                queue.append(Cell(x, y, curr.dist + 1))
                
    
print("Minimum Number Of Moves to goal = " + str(play()))
