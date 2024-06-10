#!/bin/user/python3
import subprocess
import os 
import time
import zipfile
import glob

print('Downloading assembly for Mus musculus')
print('--------------------------')
assmebly = subprocess.run('wget https://ftp.ensembl.org/pub/release-112/fasta/mus_musculus/dna/Mus_musculus.GRCm39.dna_sm.primary_assembly.fa.gz', shell = True)
print('-----------------------------')
print('Finished download')
time.sleep(0.5)
print('Downloading GTF for Mus musculus')
print('--------------------------')
gtf = subprocess.run(' wget https://ftp.ensembl.org/pub/release-112/gtf/mus_musculus/Mus_musculus.GRCm39.112.gtf.gz', shell = True)
print('-----------------------------')
print('Finished download')
time.sleep(0.5)
gz_files = glob.glob('*.gz')
if not gz_files:
    print('Error no files not find in directory')
else:
    print('Begin to unzip files')
    print('--------------------')
    unzip = subprocess.run(['gunzip'] + gz_files, check=True)
    print('Finished')



