#!/bin/user/python3

import os
import subprocess 
import time
directory = 'sra'

try:
    os.mkdir(directory)
except OSError as error:
    print('the error:', error)
    time.sleep(0.5)
    print('continue')
    print('--------')
os.chdir(directory)

def download_sra():
    time.sleep(0.5)
    print('Begining to download runs from sra in sra directory')
    print('----------------------------------------------------')
    download = subprocess.getoutput("esearch -db sra -query SRP091444 | efetch -format runinfo | cut -d ',' -f 1 | grep SRR | xargs fastq-dump  --skip-technical  --readids --read-filter pass --dumpbase --split-3")
    print('The download of the runs id finished')
    print('------------------------------------------------------')
    return download
    

download_sra()

