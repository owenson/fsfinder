#!/usr/bin/env python
# Copyright Gareth Owen <drgowen@gmail.com>
import struct
import sys

if len(sys.argv) != 2:
    print("Usage: fsfinder.py imageordisk")
    sys.exit(1)

sector = 0
with open(sys.argv[1], "rb") as f:
    while True:
        sec = f.read(512)
        found = False
        if len(sec) < 512:
            break
        # Boot sector
        if sec[510] == 0x55 and sec[511] == 0xaa:
            found = "boot sector"
        #NTFS filesystem
        if sec[3:7] == b"NTFS":
            sizedt = sec[0x28:0x30] #BPB
            sizent = struct.unpack("<Q", sizedt)
            found = "NTFS size={}".format(sizent[0])

        #Linux ext filesystem
        if sec[0x38] == 0x53 and sec[0x39]==0xef: #linux
            blockcnt=struct.unpack("<I", sec[4:8])[0]
            blksizeraw=1024<<struct.unpack("<I",sec[0x18:0x18+4])[0]
            found = "Linux totalblocks={} blksize={} size={}".format(blockcnt, blksizeraw, (blockcnt*blksizeraw)//(1024*1024))

        #did we find something?
        if found:
            print ("found at sector {}:\n\t{}".format(sector,found))

        sector += 1

