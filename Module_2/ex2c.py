from crccheck.crc import *
from crccheck.checksum import *

from ex2b import decodeMsg, seqToByteArray

def main():
    crc16 = Crc16IbmSdlc()
    print("Polynomial for CRC16-IBM-SDLC: ", format(crc16._poly, '016b'))

    data =         "00010000001000010" # number: 8258 * 4 = 33032
    msgWithError = "000100000010000100000" # number: 33032
    bytearrayData = seqToByteArray(data)
    crc16 = Crc16.calc(bytearrayData)

    decodeMsg(msgWithError + format(crc16, '08b'))



if __name__ == "__main__":
    main()