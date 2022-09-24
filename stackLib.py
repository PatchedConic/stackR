import json
filePath = "data.json"

class block:
    def __init__(self, blockID, dimension, tol, sign):
        self.dimension = dimension
        self.tol = tol
        self.sign = sign
        self.blockID = blockID

class stack:
    def __init__(self):
        self.blockList = []
        self.stackup = 0
        self.tol = 0
        self.rssTol = 0
    def blockAppend(self, block):
        self.blockList.append(block)
        self.update()
    def update(self):
        self.tol = 0
        self.stackup = 0
        self.rssTol = 0
        for x in self.blockList:
            self.stackup += float(x.dimension)*float(x.sign)
            self.tol += float(x.tol)
            self.rssTol += float(x.tol)**2
        self.rssTol = self.rssTol**(1/2)

def getLatestID():
    with open(filePath) as data:
        latestID = 0
        information = json.load(data)
        for lines in information["members"]:
            if lines["ID"] >= latestID:
                latestID = lines["ID"]
    return(latestID)
                

def readData():
    stackUp = stack()
    with open(filePath) as data:
        information = json.load(data)
        for lines in information["members"]:
            newBlock = block(lines["ID"], lines["dim"], lines["tol"], lines["sign"])
            stackUp.blockAppend(newBlock)
    return(stackUp)

def writeBlock(dim, tol, sign):
    latestID = getLatestID() + 1
    newInformation = {"ID": latestID, "dim": dim, "tol": tol, "sign": sign}
    with open(filePath, "r") as data:
        information = json.load(data)
        information['members'].append(newInformation)
    with open(filePath, "w") as data:
        json.dump(information, data, indent= 6)


def clearData():
    with open(filePath, "r") as data:
        information = json.load(data)
        information["members"] = []
    with open(filePath, "w") as data:
        json.dump(information, data, indent = 6)
