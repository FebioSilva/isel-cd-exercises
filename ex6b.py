import random
from ex6a import bsc

def countErrors(originalSeq, newSeq):
    errors = 0
    for i in range(0,len(originalSeq)):
        if originalSeq[i] != newSeq[i]:
            errors += 1
    return errors

def berComparison(L, p):
    seq = ""
    for n in range(1,L):
        randomBit = random.randrange(0,2)
        seq += str(randomBit)
    newSeq = bsc(seq, p)
    errors = countErrors(seq, newSeq)
    ber = errors / L
    print("Original BER: ", p)
    print("New BER: ", ber)




def main():
    berComparison(1024, 0.3)
    berComparison(10240, 0.3)
    berComparison(102400, 0.3)

if __name__ == "__main__":
    main()

    
        
        

