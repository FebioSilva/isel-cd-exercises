def symbolsFrequency(text):
    symbols = {}

    for c in text:
        if(symbols.get(c) == None):
            symbols[c] = 1
        else:
            symbols[c] = symbols.get(c) + 1
            
    return symbols

def symbolsPercentage(symbolsFreq, totalBytes):
    symbols = {}

    for symbol, value in symbolsFreq.items():
        symbols[symbol] = (value/totalBytes) * 100
        
    return symbols  

def symbolsTopFive(symbolsPer): 
    symbols = {}
    lowest = 0
    for symbol, value in symbolsPer.items():
        if(len(symbols) < 5):
            symbols[symbol] = value
        else:
            if( value > symbols[lowest]):
                symbols.pop(lowest)
                symbols[symbol] = value
        lowest = min(symbols, key=symbols.get)
    return symbols

def symbolsFreqPairs(text):
    symbols = {}
    before = text[0]

    for c in range(1, len(text), 1):
        pair = chr(before) + chr(text[c])
        if(symbols.get(pair) == None):
            symbols[pair] = 1
        else:
            symbols[pair] = symbols.get(pair) + 1
        before = text[c]

    return symbols


def main(file):
    f=open(file, "rb")
    text = f.read()
    totalBytes = len(text)

    symbolsFreq = symbolsFrequency(text)
    symbolsFreqPair = symbolsFreqPairs(text)
    symbolsPer = symbolsPercentage(symbolsFreq, totalBytes)
    symbolsPerPair = symbolsPercentage(symbolsFreqPair, totalBytes)
    symbolsTop5 = symbolsTopFive(symbolsPer)
    symbolsTop5Pair = symbolsTopFive(symbolsPerPair)

    print("All symbols\n")
    for x, y in symbolsPer.items():
            print("Symbol: '%c' - Percentage: %f" %(x, y))

    print("\nTop 5 symbols\n")
    for x, y in symbolsTop5.items():
            print("Symbol: '%c' - Percentage: %f" %(x, y))

    print("All symbol pairs\n")
    for x, y in symbolsPerPair.items():
            print("Symbol: '%s' - Percentage: %f" %(x, y))

    print("\nTop 5 symbol pairs\n")
    for x, y in symbolsTop5Pair.items():
            print("Symbol: '%s' - Percentage: %f" %(x, y))        

if __name__=="__main__":
    main("./resources/ListaPalavrasPT.txt")