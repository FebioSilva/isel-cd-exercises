import random

from ex4a import randomSymbolGenerator, writeInFile

def pinGenerator(file):
    pinFMP = { '0': 0.1, '1': 0.1, '2': 0.1, '3': 0.1, '4': 0.1, '5': 0.1, '6': 0.1, '7': 0.1, '8': 0.1, '9': 0.1 }
    N = random.randrange(4, 7)
    symbols = randomSymbolGenerator(pinFMP, N)
    writeInFile(symbols, file)

def euroInfo(nOfSymbols, nOfTotalSymbols):
    totalSymbols = nOfTotalSymbols
    fmp = 1/totalSymbols
    euroFMP = {}
    euroKeys = ""
    ## Generate the keys for the euro milhoes
    for n in range (1, nOfTotalSymbols + 1):
        euroFMP[str(n)] = fmp

    for i in range(1, nOfSymbols + 1):
        symbol = randomSymbolGenerator(euroFMP, 1)
        euroKeys += symbol + " "
        totalSymbols -= 1
        euroFMP.pop(symbol)
        fmp = 1/totalSymbols
        for symbol in euroFMP:
            euroFMP[symbol] = fmp
    return euroKeys



def euroMilhoesGenerator(file):
    ## Generate the keys for the euro milhoes
    euroKeys = euroInfo(5, 50)
    ## Generate the keys for the euro stars
    euroStars = euroInfo(2, 12)
    writeInFile(euroKeys + " - " + euroStars, file)
        
def generateNotSpecialFMP(first, total):
    fmp = {}
    last = first + total
    for n in range(first, last):
        fmp[chr(n)] = 1/total
    return fmp
    
def generateSpecialFMP():
    fmp = {}
    total = 32
    for n in range(33, 48):
        fmp[chr(n)] = 1/total

    for n in range(58, 65):
        fmp[chr(n)] = 1/total

    for n in range(91, 97):
        fmp[chr(n)] = 1/total

    for n in range(123, 127):
        fmp[chr(n)] = 1/total

    return fmp

def passWordGenerator(file):
    numbersFMP = generateNotSpecialFMP(48, 10)
    capitalLettersFMP = generateNotSpecialFMP(65, 26)
    smallLettersFMP = generateNotSpecialFMP(97, 26)
    specialFMP = generateSpecialFMP()
    choiceFMP = { '0': 0.25, '1': 0.25, '2': 0.25, '3': 0.25 }
    n = random.randrange(8, 13)
    
    password = ""


    for i in range(0, n):
        choice = randomSymbolGenerator(choiceFMP, 1)
        if(choiceFMP[choice] != 0.01):
            for key in choiceFMP:
                if(key == choice):
                    choiceFMP[key] = 0.01
                else :
                    choiceFMP[key] = 0.33
        if(choice == "0"):
            password += randomSymbolGenerator(numbersFMP, 1)
        elif(choice == "1"):
            password += randomSymbolGenerator(capitalLettersFMP, 1)
        elif(choice == "2"):
            password += randomSymbolGenerator(smallLettersFMP, 1)
        elif(choice == "3"):
            password += randomSymbolGenerator(specialFMP, 1)

    writeInFile(password, file)






        






        

def main():
    pinGenerator("pinGenerated.txt")
    euroMilhoesGenerator("euroMilhoesGenerator.txt")
    passWordGenerator("passwordGenerated.txt")

if __name__=="__main__":
    main()