#Função que apresenta todos os símbolos de um ficheiro, cuja frequência de ocorrência é superior a uma percentagem indicada como parâmetro. histograma
import math

def symbolsHistogram(text):
    symbols = {}

    for c in text:
        if(symbols.get(c) == None):
            symbols[c] = 1
        else:
            symbols[c] = symbols.get(c) + 1
            
    return symbols

def symbolsProbability(symbolsFrequency, totalBytes):
    symbols = {}

    for symbol, value in symbolsFrequency.items():
        symbols[symbol] = value/totalBytes

    return symbols

def symbolsOwnInformation(symbolsProbability):
    symbols = {}

    for symbol, value in symbolsProbability.items():
        symbols[symbol] = -math.log2(value)

    return symbols

def symbolsEntropy(symbolsOwnInfo, symbolsProbability):
    entropy = 0

    for symbol in symbolsOwnInfo:
        entropy += symbolsOwnInfo[symbol] * symbolsProbability[symbol]

    return entropy


def main(file):
    f=open(file, "rb")
    text = f.read()
    totalBytes = len(text)

    symbolsFreq = symbolsHistogram(text)
    symbolsProb = symbolsProbability(symbolsFreq, totalBytes)
    symbolsOwnInfo = symbolsOwnInformation(symbolsProb)
    symbolsEntrop = symbolsEntropy(symbolsOwnInfo, symbolsProb)

    for x, y in symbolsFreq.items():
        print("Symbol: '%c' - Histogram: %d \n" %(x, y))
    
    for x, y in symbolsProb.items():
        print("Symbol: '%c' - Probability: %f \n" %(x, y))

    for x, y in symbolsOwnInfo.items():
        print("Symbol: '%c' - Own Information: %d \n" %(x, y))

    print("Symbols Entropy: %d" %symbolsEntrop)

main("/workspaces/CD/fibonacci.kt")