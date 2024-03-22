import random

from ex3a import symbolsHistogram, symbolsProbability



def limitMaker(fmp, r):
    limits = {}
    limit = 1

    for symbol, prob in fmp.items():
        limit += prob * r
        limits[limit] = symbol
    return limits



    

def randomSymbolGenerator(fmp, N, file): #fmp = a: 0.5 b: 0.5 aabb pode acontecer sair bbbb?
    maxLimit = 1000
    limits = limitMaker(fmp, maxLimit)
    f = open(file, "a")

    for i in range(0,N):
        randomNum = random.randrange(1, maxLimit)
        for limit, symbol in limits.items():
            if(randomNum < limit):
                print(chr(symbol))
                f.write(chr(symbol))
                break


def main4a(file):
    f=open("/workspaces/CD/resources/maximumSubarray.kt", "rb")
    text = f.read()
    totalBytes = len(text)

    symbolsFreq = symbolsHistogram(text)
    symbolsProb = symbolsProbability(symbolsFreq, totalBytes)

    randomSymbolGenerator(symbolsProb, 3, file)

main4a("/workspaces/CD/generated.txt")