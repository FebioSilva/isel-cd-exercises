import random

from ex3a import symbolsHistogram, symbolsProbability, symbolsEntropy, symbolsOwnInformation



def limitMaker(fmp, r):
    limits = {}
    limit = 1

    for symbol, prob in fmp.items():
        limit += prob * r
        limits[limit] = symbol
    return limits



def randomSymbolGenerator(fmp, N):
    maxLimit = 1000
    limits = limitMaker(fmp, maxLimit)
    symbols = ""
    
    for i in range(0,N):
        randomNum = random.randrange(1, maxLimit)
        for limit, symbol in limits.items():
            if(randomNum < limit):
                symbols = symbols + str(symbol)
                break
    return symbols

def writeInFile(str, file):
    f = open(file, "w")
    f.write(str)
    f.close()


def main(file):
    #f=open("/workspaces/CD/resources/maximumSubarray.kt", "rb")
    f = open("../resources/maximumSubarray.kt", "rb")
    textS = f.read()
    totalBytesS = len(textS)
    
    symbolsFreqS = symbolsHistogram(textS)
    symbolsProbS = symbolsProbability(symbolsFreqS, totalBytesS)
    symbolsOwnInfoS = symbolsOwnInformation(symbolsProbS)
    symbolsEntropS = symbolsEntropy(symbolsOwnInfoS, symbolsProbS)
   
    
    symbols = randomSymbolGenerator(symbolsProbS, 1000)
    writeInFile(symbols, file)

    d = open(file, "rb")
    textD = d.read()
    totalBytesD = len(textD)

    symbolsFreqD = symbolsHistogram(textD)
    symbolsProbD = symbolsProbability(symbolsFreqD, totalBytesD)
    symbolsOwnInfoD = symbolsOwnInformation(symbolsProbD)
    symbolsEntropD = symbolsEntropy(symbolsOwnInfoD, symbolsProbD)

    print("Source Entropy: {:.2f}".format(symbolsEntropS))
    print("Destination Entropy: {:.4f}".format(symbolsEntropD))

if __name__=="__main__":
    #main("/workspaces/CD/generated.txt")
    main("generated-content/generated.txt")