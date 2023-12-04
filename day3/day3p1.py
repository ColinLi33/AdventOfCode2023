file_path = 'input.txt' 

def checkAdj(i,jStart, jEnd, arr):
    for j in range(jStart, jEnd+1):
        adjCoords = [
            (i-1, j-1), (i-1,j), (i-1,j+1),
            (i,j-1), (i,j+1),
            (i+1,j-1), (i+1,j), (i+1, j+1)
        ]
        for x, y in adjCoords:
            if(0 <= x < len(arr) and 0 <= y < len(arr[0]) and arr[x][y] != '.' and not arr[x][y].isdigit()):
                return True
    return False

def checkNums(i, jStart, jEnd, arr):
    returnVal = 0
    if(checkAdj(i,numStart,numEnd,arr)):
        num = ""
        for k in range(numStart, numEnd+1):
            num = num + arr[i][k]
        returnVal = int(num)
    return returnVal

with open(file_path, 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    arr = [list(line) for line in lines]
    total = 0
    for i in range(len(arr)):
        numStart = -1
        numEnd = -1
        for j in range(len(arr[i])):
            if(arr[i][j].isdigit()):
                if(numStart == -1):
                    numStart = j
                if(j == len(arr[i])-1):
                    numEnd = j
                    total += checkNums(i,numStart,numEnd,arr)
            else:
                if(numStart != -1):
                    numEnd = j-1
                    total += checkNums(i,numStart,numEnd,arr)
                    numStart = -1
    print(total)

                        
                    
                
                
    

