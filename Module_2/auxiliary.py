import random

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

def countErrors(originalSeq, newSeq):
    errors = 0
    for i in range(0, len(originalSeq)):
        if originalSeq[i] != newSeq[i]:
            errors += 1
    return errors

def bsc(seq, p):
    fmp = {'0': 1-p, '1': p} #0 e 1 são apenas para representar sucesso e insucesso, não são bits
    newSeq = ""
    for bit in seq:
        symbol = randomSymbolGenerator(fmp, 1)
        if(symbol == '1'):
            newSeq += '0' if bit == '1' else '1'
        else:
            newSeq += bit
    return newSeq

def fileToBinary(file):
    f = open(file, "r")
    text = f.read()
    f.close()
    binary_str = ""
    for c in text:
        binary_str += format(ord(c), '08b')
    return binary_str

def binaryStringToFile(file, binary_str):
    f = open(file, "w")
    for i in range(0, len(binary_str), 8):
        char = chr(int(binary_str[i:i+8],2))
        f.write(char)
    f.close()