from auxiliary import *

def encode(binary_str):
    new_binary_str = ""
    for b in range(0, len(binary_str), 4):
        bit0 = binary_str[b]
        bit1 = binary_str[b + 1]
        bit2 = binary_str[b + 2]
        bit3 = binary_str[b + 3]
        new_binary_str += bit0
        new_binary_str += bit1
        new_binary_str += bit2
        new_binary_str += bit3
        new_binary_str += str(int(bit1) ^ int(bit2) ^ int(bit3))
        new_binary_str += str(int(bit0) ^ int(bit1) ^ int(bit3))
        new_binary_str += str(int(bit0) ^ int(bit2) ^ int(bit3))
    return new_binary_str

def decode(binary_str):
    new_binary_str = ""
    for b in range(0, len(binary_str), 7):
        bit0 = binary_str[b]
        bit1 = binary_str[b + 1]
        bit2 = binary_str[b + 2]
        bit3 = binary_str[b + 3]
        r_bit0 = binary_str[b + 4]
        r_bit1 = binary_str[b + 5]
        r_bit2 = binary_str[b + 6]

        e_bit0 = int(bit1) ^ int(bit2) ^ int(bit3)
        e_bit1 = int(bit0) ^ int(bit1) ^ int(bit3)
        e_bit2 = int(bit0) ^ int(bit2) ^ int(bit3)
        sindroma = str(e_bit0 ^ int(r_bit0)) + str(e_bit1 ^ int(r_bit1)) + str(e_bit2 ^ int(r_bit2))
        if(sindroma == "011"):
            new_binary_str += str(int(bit0) ^ 1)
            new_binary_str += bit1
            new_binary_str += bit2
            new_binary_str += bit3
        elif(sindroma == "110"):
            new_binary_str += bit0
            new_binary_str += str(int(bit1) ^ 1)
            new_binary_str += bit2
            new_binary_str += bit3
        elif(sindroma == "101"):
            new_binary_str += bit0
            new_binary_str += bit1
            new_binary_str += str(int(bit2) ^ 1)
            new_binary_str += bit3
        elif(sindroma == "111"):
            new_binary_str += bit0
            new_binary_str += bit1
            new_binary_str += bit2
            new_binary_str += str(int(bit3) ^ 1)
        else:
            new_binary_str += bit0
            new_binary_str += bit1
            new_binary_str += bit2
            new_binary_str += bit3
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

def examplesIII(file):
    binary_str = fileToBinary(file)
    coded_binary_str = encode(binary_str)
    print("Example 1")
    print("- Without Encoding")
    getBER(binary_str, 0.001)
    print("- With Encoding")
    result1 = getCodedBER(binary_str, coded_binary_str, 0.001)
    binaryStringToFile("generated-content/bscResult1.txt", result1)
    print("----------------------------")
    print("Example 2")
    print("- Without Encoding")
    getBER(binary_str, 0.01)
    print("- With Encoding")
    result2 = getCodedBER(binary_str, coded_binary_str, 0.01)
    binaryStringToFile("generated-content/bscResult2.txt", result2)
    print("----------------------------")
    print("Example 3")
    print("- Without Encoding")
    getBER(binary_str, 0.1)
    print("- With Encoding")
    result3 = getCodedBER(binary_str, coded_binary_str, 0.1)
    binaryStringToFile("generated-content/bscResult3.txt", result3)
    print("----------------------------")
    print("Example 4")
    print("- Without Encoding")
    getBER(binary_str, 0.5)
    print("- With Encoding")
    result4 = getCodedBER(binary_str, coded_binary_str, 0.5)
    binaryStringToFile("generated-content/bscResult4.txt", result4)
    print("----------------------------")

def main():
    examplesIII("resources/alice29.txt")
    


if __name__ == "__main__":
    main()