fsfinder
========

File system finder for when partition absent / can't be trusted.  

python3 fsfinder.py diskorimagefile

Requires Python 3.

NOTE: all sizes in sectors

Sample output:


    root@svm18027:~/fsfinder# python3 fsfinderinder.py lab2.img
    found at sector 0:
        boot sector
    found at sector 63:
        NTFS size=32065
    found allt sector 21053:
        boot sector
    found at sector 32128:
        NTFS size=32065
    foundund at sector 32130:
        boot sector
    
    root@svm18027:~/fsfinder# python3 fsfinderinder.py /dev/xvda1 
    found at sector 2:
        Linux totalblocks=9175040 blksize=4096 size=35840

