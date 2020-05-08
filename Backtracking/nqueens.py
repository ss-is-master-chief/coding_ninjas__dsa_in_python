def isSafe(row, col, board, n):
    i = row-1
    while(i>=0):
        if(board[i][col]==1):
            return False
        i -= 1

    i = row-1
    j = col-1

    while(i>=0 and j>=0):
        if(board[i][j]==1):
            return False
        i -= 1
        j -= 1
        
    i = row-1
    j = col+1

    while(i>=0 and j<n):
        if(board[i][j]==1):
            return False
        i -= 1
        j += 1

    return True

def nQueen_helper(row, n, board):
    if(row==n):
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=" ")
                
        print()
        return

    for col in range(n):
        if(isSafe(row, col, board, n)):
            board[row][col] = 1
            nQueen_helper(row+1, n, board)
            board[row][col] = 0

    return 

def nQueen(n):
    #Implement Your Code Here
    board = [[0 for i in range(n)] for j in range(n)]
    nQueen_helper(0,n, board)


n = int(input())
nQueen(n)