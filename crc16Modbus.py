def calculateCRC(msgIn):
    CRC16 = 0xffff
    poly =  0xa001

    for i in range(len(msgIn)):

        CRC16 = ord(msgIn[i]) ^ CRC16

        for _ in range(8):
            if (CRC16 & 0x0001 == 1):
                CRC16 >>= 1
                CRC16 ^= poly
            else:
                CRC16 >>= 1

    return str(hex(CRC16 >> 8)),str(hex(CRC16 & 0x00ff))


checksum = ["",""]
checksum = calculateCRC("12.3,43.5,23.5")

checksum = [i[2:] for i in checksum]
print("Checksum: {} {}".format(checksum[0],checksum[1]))