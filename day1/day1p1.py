filePath = 'input.txt'  
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
        left,right = findNums(data)
        num = int(data[left] + data[right])
        total += num
    print(total)

