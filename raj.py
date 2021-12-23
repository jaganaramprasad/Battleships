from battleship import EMPTY_CLICKED, EMPTY_UNCLICKED, SHIP_CLICKED, SHIP_UNCLICKED


def drawGrid(data, canvas, grid, showShips):#drawgrid
    for row in range(data["rows"]):
        for cols in range(data["columns"]):
            if grid[row][cols]==SHIP_UNCLICKED:
                canvas.create_rectangle(cols*data["cellsize"],row*data["cellsize"],data["cellsize"]+cols*data["cellsize"], row*data["cellsize"]+data["cellsize"], fill="yellow")
            elif grid[row][cols]==EMPTY_UNCLICKED:
                canvas.create_rectangle(cols*data["cellsize"],row*data["cellsize"],data["cellsize"]+cols*data["cellsize"], row*data["cellsize"]+data["cellsize"], fill="blue")
            elif grid[row][cols]==SHIP_CLICKED:
                canvas.create_rectangle(cols*data["cellsize"],row*data["cellsize"],data["cellsize"]+cols*data["cellsize"], row*data["cellsize"]+data["cellsize"], fill="red")
            elif grid[row][cols]==EMPTY_CLICKED:
                canvas.create_rectangle(cols*data["cellsize"],row*data["cellsize"],data["cellsize"]+cols*data["cellsize"], row*data["cellsize"]+data["cellsize"], fill="white")
                if showShips==False:
                    if grid[row][cols]==SHIP_UNCLICKED:
                        canvas.create_rectangle(cols*data["cellsize"],row*data["cellsize"],data["cellsize"]+cols*data["cellsize"], row*data["cellsize"]+data["cellsize"], fill="blue")
    return