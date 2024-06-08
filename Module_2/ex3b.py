import serial
from ex2a import burstBSC

def main():
   
    arduino = serial.Serial('COM3', 9600)
    while True:
        nums = []
        while len(nums) < 4:
            data = arduino.read()
            dataToPrintInDecimal = int.from_bytes(data, byteorder='big')
            print(dataToPrintInDecimal)
            nums.append(dataToPrintInDecimal)
        numsToBinaryToString = ""
        for i in nums:
            numsToBinaryToString += format(i, '08b')
        withError = burstBSC(numsToBinaryToString, 3, 0.1)
        
        nums = [int(withError[i:i+8], 2) for i in range(0, len(withError), 8)]
        print("Result of BSC: ", nums)


        sindroma = nums[0] ^ nums[1] ^ nums[2] ^ nums[3]
        print("Sindroma:", sindroma)
        if sindroma == 0:
            print("No error detected")
        else:
            print("Error detected")
    
     
if __name__ == "__main__":
    main()