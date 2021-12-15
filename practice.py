def addShips(grid, numShips):
    r=0
    while r<numShips:
        s=createShip() #[[1,2][2,3][4,5]]
        m=checkShip(grid,s) #
        if m==True:
            for i in s:#[1,2]
                grid[i[0]][i[1]]=EMPTY_UNCLICKED
            r=r+1
    return grid