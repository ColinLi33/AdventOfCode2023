file_path = 'input.txt' 

def checkAdj(i, j, arr, alreadyChecked):
    adjCoords = [
        (i-1, j-1), (i-1,j), (i-1,j+1),
        (i,j-1), (i,j+1),
        (i+1,j-1), (i+1,j), (i+1, j+1)
    ]
    nums = []
    for i in range(len(adjCoords)):
        x,y = adjCoords[i]
        if(0 <= x < len(arr) and 0 <= y < len(arr[0]) and (x,y) not in alreadyChecked and arr[x][y].isdigit()):
            num, yRange = findNum(x,y,arr)
            nums.append(num)
            for j in range(yRange[0], yRange[1] + 1):
                alreadyChecked[(x,j)] = "True"
    return [nums, alreadyChecked]

def findNum(x,y,arr):
    num = ""
    while(y >= 0 and arr[x][y].isdigit()):
        y-=1
    y+=1
    startY = y
    while(y < len(arr[x]) and arr[x][y].isdigit()):
        num = num + arr[x][y]
        y+=1
    return [num, (startY, y)]

with open(file_path, 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    arr = [list(line) for line in lines]
    total = 0
    alreadyChecked = {}
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if(arr[i][j] == '*'):
                nums, alreadyChecked = checkAdj(i,j,arr,alreadyChecked)
                if(len(nums) >= 2):
                    product = 1
                    for k in nums:
                        product *= int(k)
                    total+=product  
    print(total)

                        
                    
                
                
    

