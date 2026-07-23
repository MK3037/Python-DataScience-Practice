grid = [[1,3,1,4],[1,5,1,4],[4,2,1,4]]
print(grid)
row=len(grid)                               #horizontal
column=len(grid[0])                         #vertical
for i in range(1,row):
    grid[i][0]=grid[i-1][0]+grid[i][0]
for i in range(1,column):
    grid[0][i]=grid[0][i-1]+grid[0][i]
print(grid)


for r in range(1, row):
    for c in range(1,column):
        grid[r][c]=grid[r][c]+min(grid[r-1][c],grid[r][c-1])
print(grid)
print(grid[row-1][column-1])
