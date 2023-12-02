filePath = "input.txt"

def checkGame(info):
    redLim = 12 
    greenLim = 13
    blueLim = 14
    for game in info:
        pulls = game.split(",")
        result = [(int(item.split()[0]), item.split()[1]) for item in pulls]
        for marble in result:
            if(marble[1] == 'red'):
                if(marble[0] > redLim):
                    return False
            elif(marble[1] == "green"):
                if(marble[0] > greenLim):
                    return False
            else: #blue
                if(marble[0] > blueLim):
                    return False 
    return True


with open(filePath, 'r') as file:
    total = 0
    for line in file:
        data = line.strip()
        gameNum = data[5: data.index(":")]
        info = data[data.index(":") + 1:].split(";")
        if(checkGame(info)):
            total += int(gameNum)
    print(total)
        


