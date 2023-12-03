filePath = "input.txt"

def computePower(info):
    redMax = 0
    greenMax = 0
    blueMax = 0
    for game in info:
        pulls = game.split(",")
        result = [(int(item.split()[0]), item.split()[1]) for item in pulls]
        for marble in result:
            if(marble[1] == 'red'):
                if(marble[0] > redMax):
                    redMax = marble[0]
            elif(marble[1] == "green"):
                if(marble[0] > greenMax):
                    greenMax = marble[0]
            else: #blue
                if(marble[0] > blueMax):
                    blueMax = marble[0]
    return redMax * greenMax * blueMax

with open(filePath, 'r') as file:
    total = 0
    for line in file:
        data = line.strip()
        gameNum = data[5: data.index(":")]
        info = data[data.index(":") + 1:].split(";")
        total += computePower(info)
    print(total)
        
