from ex6a import bsc
from ex6b import countErrors

def berComparionWithFile(file, p):
    f = open(file, "r")
    text = f.read()
    f.close()
    binary_str = ""
    for c in text:
        binary_str += format(ord(c), '08b')
    newSeq = bsc(binary_str, p)
    errors = countErrors(binary_str, newSeq)
    ber = errors / len(binary_str)
    print("Number of bits: ", len(binary_str))
    print("Number of errors: ", errors)
    print("Original BER: ", p)
    print("New BER: ", ber)
    return newSeq

def binaryStringToFile(binary_str):
    f = open("generated-content/binary_str.txt", "w")
    for i in range(0, len(binary_str), 8):
        char = chr(int(binary_str[i:i+8],2))
        f.write(char)
    f.close()





def main(file):
    newSeq = berComparionWithFile(file, 0.01)
    binaryStringToFile(newSeq)
    
if __name__ == "__main__":
    main("resources/alice29.txt")