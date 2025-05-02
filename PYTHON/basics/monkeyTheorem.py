import random




def genereateOne(strlen):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    for i in range(strlen):
        res = res + alphabet[random.randrange(27)]
        
    return res

def score(goal, teststring):
    numSame = 0
    for i in range (len(goal)):
        if goal[i] == teststring[i]:
            numSame = numSame + 1


