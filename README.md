fsfinder
========

File system finder for when partition absent / can't be trusted.  

python3 fsfinder.py diskorimagefile

Requires Python 3.

NOTE: all sizes in sectors

Sample output:

    ~/fsfinder# python3 fsfinder.py ~/lab2.img   
    found boot sector at sector 0  
    found NTFS size=32065 at sector 63  
    found boot sector at sector 21053  
    found NTFS size=32065 at sector 32128  
	found boot sector at sector 32130  

