filePath = "input.txt"

def calculateWinnings(winningNumbers, ourNumbers):
    totalWinnings = 0
    for num in ourNumbers:
        if num in winningNumbers:
            if(totalWinnings == 0):
                totalWinnings +=1 
            else:
                totalWinnings *= 2
    return totalWinnings
    
with open(filePath, 'r') as file:
    total = 0
    for line in file:
        parts = line.split('|')
        winningNumbers = [int(num) for num in parts[0].split() if num.strip().isdigit()]
        ourNumbers = [int(num) for num in parts[1].split() if num.strip().isdigit()]
        winningNumbers = {num: True for num in winningNumbers}
        total += calculateWinnings(winningNumbers,ourNumbers)
    print(total)
        


