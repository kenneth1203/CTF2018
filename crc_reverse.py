# -*- coding: utf-8 -*-
import binascii
import struct

#\x49\x48\x44\x52\x00\x00\x01\xF4\x00\x00\x01\xA4\x08\x06\x00\x00\x00

crc32key = 0xcbd6df8a
for i in range(420, 65535):
    height = struct.pack('>i', i)
    #CRC: CBD6DF8A
    data = b'\x49\x48\x44\x52\x00\x00\x01\xF4' + height + b'\x08\x06\x00\x00\x00'
    crc32result = binascii.crc32(data) & 0xffffffff
    print(hex(crc32result))
    if crc32result == crc32key:
        print(height)
        break
