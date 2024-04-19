from ex6a import bsc
from ex6b import countErrors

def berComparionWithFile(file, p):
    f = open(file, "r")
    text = f.read()
    f.close()
    binary_str = ""
    for c in text:
        binary_str += format(ord(c), 'b')
    newSeq = bsc(binary_str, p)
    errors = countErrors(binary_str, newSeq)
    ber = errors / len(binary_str)
    print("Number of bits: ", len(binary_str))
    print("Number of errors: ", errors)
    print("Original BER: ", p)
    print("New BER: ", ber)


def main(file):
    berComparionWithFile(file, 0.1)
    
if __name__ == "__main__":
    main("resources/alice29.txt")