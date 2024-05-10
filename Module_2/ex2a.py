from auxiliary import *

def burstBSC(seq, L, p):
    fmp = {'0': 1-p, '1': p} #0 e 1 são apenas para representar sucesso e insucesso, não são bits
    newSeq = ""
    counter = 0
    for bit in seq:
        if(counter == 0):
            symbol = randomSymbolGenerator(fmp, 1)
            if(symbol == '1'):
                counter = L - 1
                newSeq += str(int(bit) ^ 1)
            else:
                newSeq += bit
        else:
            newSeq += str(int(bit) ^ 1)
            counter -= 1
    return newSeq

def examples(file):
    binary_str = fileToBinary(file)
    newSeq = burstBSC(binary_str, 3, 0.01)
    binaryStringToFile("generated-content/burstBSCResult1.txt", newSeq)
    newSeq = burstBSC(binary_str, 3, 0.1)
    binaryStringToFile("generated-content/burstBSCResult2.txt", newSeq)
    newSeq = burstBSC(binary_str, 8, 0.01)
    binaryStringToFile("generated-content/burstBSCResult3.txt", newSeq)
    newSeq = burstBSC(binary_str, 8, 0.1)
    binaryStringToFile("generated-content/burstBSCResult4.txt", newSeq)
    
    
def main():
    examples("resources/alice29.txt")

if __name__ == "__main__":
    main()
