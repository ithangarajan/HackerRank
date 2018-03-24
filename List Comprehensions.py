if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result=[]
    for xDim in range (0,x+1):
        for yDim in range (0,y+1):
            for zDim in range (0,z+1):
                if xDim+yDim+zDim != n:
                    result.append([xDim,yDim,zDim])
    print (result)