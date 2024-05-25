from auxiliary import *

def getBER(binary_str, p):
    newSeq = bsc(binary_str, p)
    errors = countErrors(binary_str, newSeq)
    ber = errors / len(binary_str)
    print("Number of bits: ", len(binary_str))
    print("BER: ", ber)
    print("Number of wrong bits: ", errors)
    return newSeq

def examplesI(file):
    binary_str = fileToBinary(file)
    print("Example 1")
    result1 = getBER(binary_str, 0.001)
    binaryStringToFile("generated-content/bscResult1.txt", result1)
    print("----------------------------")
    print("Example 2")
    result2 = getBER(binary_str, 0.01)
    binaryStringToFile("generated-content/bscResult2.txt", result2)
    print("----------------------------")
    print("Example 3")
    result3 = getBER(binary_str, 0.1)
    binaryStringToFile("generated-content/bscResult3.txt", result3)
    print("----------------------------")
    print("Example 4")
    result4 = getBER(binary_str, 0.5)
    binaryStringToFile("generated-content/bscResult4.txt", result4)
    print("----------------------------")

def main():
    examplesI("resources/alice29.txt")

if __name__ == "__main__":
    main()