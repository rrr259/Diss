#!/bin/user/python3
import subprocess
import os 
import time
directory = 'sra'
os.chdir(directory)

directory2 = 'fastqc'

try:
    os.mkdir(directory2)
except OSError as error:
    print('the error:', error)
    time.sleep(0.5)
    print('continue')
    print('--------')


#running FastQC
print('Running FastQC')
time.sleep(0.5)
print('---------------')
fastqc_run = subprocess.run('fastqc * -o fastqc', shell=True)
print('------------------------')
time(0.5)
print('Finished FastQC analysis')
print('-------------------------')
time(0.5)
print('All the files are in the fastqc folder')
print('---------------------------------------')




