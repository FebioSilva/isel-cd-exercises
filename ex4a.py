import random

from ex3a import symbolsHistogram, symbolsProbability, symbolsEntropy, symbolsOwnInformation



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
    f = open(file, "w")

    for i in range(0,N):
        randomNum = random.randrange(1, maxLimit)
        for limit, symbol in limits.items():
            if(randomNum < limit):
                f.write(chr(symbol))
                break


def main(file):
    #f=open("/workspaces/CD/resources/maximumSubarray.kt", "rb")
    f = open("./resources/maximumSubarray.kt", "rb")
    textS = f.read()
    totalBytesS = len(textS)

    symbolsFreqS = symbolsHistogram(textS)
    symbolsProbS = symbolsProbability(symbolsFreqS, totalBytesS)
    symbolsOwnInfoS = symbolsOwnInformation(symbolsProbS)
    symbolsEntropS = symbolsEntropy(symbolsOwnInfoS, symbolsProbS)

    randomSymbolGenerator(symbolsProbS, 8, file)

    d = open(file, "rb")
    textD = d.read()
    totalBytesD = len(textD)

    symbolsFreqD = symbolsHistogram(textD)
    symbolsProbD = symbolsProbability(symbolsFreqD, totalBytesD)
    symbolsOwnInfoD = symbolsOwnInformation(symbolsProbD)
    symbolsEntropD = symbolsEntropy(symbolsOwnInfoD, symbolsProbD)

    print("Source Entropy: %d" %symbolsEntropS)
    print("Destination Entropy: %d" %symbolsEntropD)

if __name__=="__main__":
    #main("/workspaces/CD/generated.txt")
    main("generated.txt")