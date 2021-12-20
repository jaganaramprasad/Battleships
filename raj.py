from battleship import EMPTY_CLICKED, EMPTY_UNCLICKED, SHIP_CLICKED, SHIP_UNCLICKED


def drawGrid(data, canvas, grid, showShips):#drawgrid
    for row in range(data["rows"]):
        for cols in range(data["cols"]):
            if grid[row][cols]==SHIP_UNCLICKED:
                canvas.create_rectangle(cols*data["celsize"],row*data["celsize"],data["celsize"]+cols*data["celsize"], row*data["celsize"]+data["celsize"], fill="yellow")
            elif grid[row][cols]==EMPTY_UNCLICKED:
                canvas.create_rectangle(cols*data["celsize"],row*data["celsize"],data["celsize"]+cols*data["celsize"], row*data["celsize"]+data["celsize"], fill="blue")
            elif grid[row][cols]==SHIP_CLICKED:
                canvas.create_rectangle(cols*data["celsize"],row*data["celsize"],data["celsize"]+cols*data["celsize"], row*data["celsize"]+data["celsize"], fill="red")
            elif grid[row][cols]==EMPTY_CLICKED:
                canvas.create_rectangle(cols*data["celsize"],row*data["celsize"],data["celsize"]+cols*data["cellsize"], row*data["celsize"]+data["celsize"], fill="white")
                if showShips==False:
                    if grid[row][cols]==SHIP_UNCLICKED:
                        canvas.create_rectangle(cols*data["celsize"],row*data["celsize"],data["celsize"]+cols*data["celsize"], row*data["celsize"]+data["celsize"], fill="blue")
    return