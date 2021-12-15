def emptyGrid(rows, cols):
    matrix=[]
    for i in range(rows):         
        a =[]
        for j in range(cols):     
            a.append(EMPTY_UNCLICKED)
        matrix.append(a)
    return matrix
