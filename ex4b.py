import random

from ex4a import randomSymbolGenerator

def pinGenerator(file):
    pinFMP = { '0': 0.1, '1': 0.1, '2': 0.1, '3': 0.1, '4': 0.1, '5': 0.1, '6': 0.1, '7': 0.1, '8': 0.1, '9': 0.1 }
    print(pinFMP)
    N = random.randrange(4, 6)
    randomSymbolGenerator(pinFMP, N, file)

def main():
    pinGenerator("pinGenerated.txt")

if __name__=="__main__":
    main()