class board(object):
    def __init__(self):
        self.positionDict = {
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }

    def __getPosition__(self, key):
        return self.positionDict[key]
    def __getValues__(self):
        return self.positionDict.values()
    
    def change_position(self, key, value):
        self.positionDict[key] = value
    
    def display_board(self):
        print(""" TIC-TAC-TOE
| %s | %s | %s |
| %s | %s | %s |
| %s | %s | %s |\n""" % (self.positionDict["1"], self.positionDict["2"], self.positionDict["3"], \
                       self.positionDict["4"], self.positionDict["5"], self.positionDict["6"], \
                       self.positionDict["7"], self.positionDict["8"], self.positionDict["9"]))
    

class player(object):
    def __init__(self, name):
        self.name = name
        self.score = 0

    def __getScore__(self):
        return self.score
    
    def add_score(self):
        self.score += 1

