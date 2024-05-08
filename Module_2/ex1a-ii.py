from auxiliary import *

def encode(binary_str):
    new_binary_str = ""
    for b in binary_str:
        new_binary_str += b*3 
    return new_binary_str

def decode(binary_str):
    new_binary_str = ""
    for b in range(0, len(binary_str), 3):
        if(binary_str[b] == binary_str[b + 1]):
            new_binary_str += binary_str[b]
        elif(binary_str[b] == binary_str[b + 2]):
            new_binary_str += binary_str[b]
        else:
            new_binary_str += binary_str[b + 1]
    return new_binary_str        
            
def getBER(binary_str, p):
    newSeq = bsc(binary_str, p)
    errors = countErrors(binary_str, newSeq)
    ber = errors / len(binary_str)
    print("Number of bits: ", len(binary_str))
    print("BER: ", ber)
    print("Number of wrong bits: ", errors)
    return newSeq 

def getCodedBER(binary_str, coded_binary_str, p):
    toDecode_binary_str = bsc(coded_binary_str, p)
    decoded_binary_str = decode(toDecode_binary_str)
    errors = countErrors(binary_str, decoded_binary_str)
    ber = errors / len(decoded_binary_str)
    print("Number of bits: ", len(binary_str))
    print("BER': ", ber)
    print("Number of wrong bits: ", errors)
    return decoded_binary_str

def examplesII(file):
    binary_str = fileToBinary(file)
    coded_binary_str = encode(binary_str)
    print("Example 1")
    print("- Without Encoding")
    getBER(binary_str, 0.001)
    print("- With Encoding")
    result1 = getCodedBER(binary_str, coded_binary_str, 0.001)
    #binaryStringToFile("generated-content/bscResult1.txt", result1)
    print("----------------------------")
    print("Example 2")
    print("- Without Encoding")
    getBER(binary_str, 0.01)
    print("- With Encoding")
    result2 = getCodedBER(binary_str, coded_binary_str, 0.01)
    #binaryStringToFile("generated-content/bscResult2.txt", result2)
    print("----------------------------")
    print("Example 3")
    print("- Without Encoding")
    getBER(binary_str, 0.1)
    print("- With Encoding")
    result3 = getCodedBER(binary_str, coded_binary_str, 0.1)
    #binaryStringToFile("generated-content/bscResult3.txt", result~3)
    print("----------------------------")
    print("Example 4")
    print("- Without Encoding")
    getBER(binary_str, 0.5)
    print("- With Encoding")
    result4 = getCodedBER(binary_str, coded_binary_str, 0.5)
    #binaryStringToFile("generated-content/bscResult4.txt", result4)
    print("----------------------------")

def main():
    examplesII("resources/alice29.txt")

if __name__ == "__main__":
    main()