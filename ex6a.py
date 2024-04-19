#Simulate binary symmetric channel with error probability p
#Input: sequence of bits, p
from ex4a import randomSymbolGenerator

def bsc(seq, p):
    fmp = {'0': 1-p, '1': p}
    newSeq = ""
    for bit in seq:
        symbol = randomSymbolGenerator(fmp, 1)
        if(symbol == '1'):
            newSeq += '0' if bit == '1' else '1'
        else:
            newSeq += bit
    return newSeq

#Output: sequence of bits with errors
def main():
    result = bsc("1010", 0.5)
    print(result)

if __name__ == "__main__":
    main()
