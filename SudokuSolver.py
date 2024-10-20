def possible(x, y, n, grid):
    for i in range(9):
        if grid[x][i] == n: 
            return False
        if grid[i][y] == n:
            return False
        
    x0 = x//3*3
    y0 = y//3*3
    for i in range(3):
        for j in range(3):
            if grid[x0+i][y0+j] == n:
                return False
    return True

def solve(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for n in range(1,10):
                    if(possible(i,j,n,grid)):
                        grid[i][j] = n
                        if solve(grid):
                            return grid
                        grid[i][j] = 0
                return 
    return grid

