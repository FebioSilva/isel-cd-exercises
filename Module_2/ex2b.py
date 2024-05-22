import random

from crccheck.crc import *
from crccheck.checksum import *
from ex2a import burstBSC

crcBits = 16

def generateBinarySeq(k):
    seq = ""
    for i in range(k):
        seq += str(random.randint(0, 1))
    return seq

def seqToByteArray(seq):
    data = bytearray()
    for b in range(0, len(seq), 8):
        byte = int(seq[b:b+8], 2)
        data.append(byte)
    return data



def parityBits(data):
    parBits = format(Crc16.calc(data), '08b')
    if(len(parBits) < crcBits):
        newBits = ""
        for i in range(0, crcBits - len(parBits)):
            newBits += '0'
        newBits += parBits
        return newBits
    return parBits    

def encodeMsg(seq):
    data = seqToByteArray(seq)
    b = parityBits(data)
    seq += b
    return seq

def decodeMsg(result):
    m = result[:-(crcBits)]
    print("Message: ", m)
    mByte = seqToByteArray(m)
    expectedParBits = result[-crcBits:]
    actualParBits = parityBits(mByte)
    print("Expected Parity Bits: ", expectedParBits)
    print("Actual Parity Bits:   ", actualParBits)
    if(expectedParBits != actualParBits):
        print("Error Detected")


def examples():
    print("AH")

def main():
    seq = generateBinarySeq(1024)
    encode = encodeMsg(seq)
    result = burstBSC(encode, 16, 0.002)
    decode = decodeMsg(result)

if __name__ == "__main__":
    main()