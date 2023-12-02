filePath = 'input.txt'  
digitMap = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def findTrueSandwiches(prev):
    first = None 
    last = None
    for i in range(len(prev)):
        if(prev[i] != None):
            first = (prev[i], i)
            break 
    for i in range(len(prev) - 1, -1, -1):
        if(prev[i] != None):
            last = (prev[i], i)
            return [first, last]
        
def findStringNumDP(data):
    s = [False] * (len(data))
    prev = [None] * (len(data))
    s[0] = True
    for k in range(1, len(data)):
        j = k
        while(not s[k] and j>0):
            if(data[j:k+1] in digitMap):
                s[k] = True 
                prev[k] = j-1
            else:
                j -= 1
    return prev

def findNums(data):
    left = 0
    right = len(data)-1
    while(not data[left].isdigit()):
        left+=1
    while(not data[right].isdigit()):
        right-=1
    return (left, right)


with open(filePath, 'r') as file:
    total = 0
    for line in file:
        data = line.strip()
        data = "x" + data #i am stupid so I need this
        prev = findStringNumDP(data)
        sandwiches = findTrueSandwiches(prev)
        left,right = findNums(data)

        if(sandwiches != None):
            if(sandwiches[0][0] < left):
                left = digitMap[data[sandwiches[0][0] + 1 : sandwiches[0][1] + 1]]
            else:
                left = data[left]
            if(sandwiches[-1][1] > right):
                right = digitMap[data[sandwiches[-1][0] + 1 : sandwiches[-1][1] + 1]]
            else:
                right = data[right]
        else:
            left = data[left]
            right = data[right]
        num = int(left + right)
        total += num
    print(total) 

