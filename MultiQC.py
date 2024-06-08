#!/bin/user/python3
import subprocess
import os 
import time

print('Begining MultiQC analysis')
print('--------------------------')
d1 = 'sra'
os.chdir(d1)
d = 'fastqc' 
os.chdir(d)
multiqc_run = subprocess.run('multiqc .', shell = True)
print('-----------------------------')
print('Finished MultiQC')
time.sleep(0.5)
print('Multiqc direcotry created')

