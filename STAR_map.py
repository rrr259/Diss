#!/usr/bin/env python3
import subprocess
import glob
import os
import time
import shutil

#path tp directories 
fastq_dir = '/home/s2614505/Diss/sra'
index_dir = '/home/s2614505/Diss/ref'
out_dir = 'aligment'

#moving fastqc directory from sra 
dir_move = '/home/s2614505/Diss/sra/fastqc'
move_to = '/home/s2614505/Diss'

try:
    shutil.move(dir_move, move_to) 
except OSError as error: 
    print('Directory moved already')

#getting back home dir 
def get_home():
    return os.chdir('/home/s2614505/Diss')
get_home()

#making aligmnet dir 
try: 
    os.mkdir(out_dir)
except OSError as error:
    print('the error:', error)
    time.sleep(0.5)
    print('continue')
    print('--------')
output_dir = '/home/s2614505/Diss/aligment'

#finding all the reads in sra 
def find_reads():
    os.chdir(fastq_dir)
    find_base = subprocess.run("find . -name 'SRR*' -print| sort | uniq", shell=True, capture_output= True, text=True)
    if find_base.returncode !=0:
        print('Error occured')
    else:
        time.sleep(0.5)
        print('-----------------')
        print('Reads found:')
        time.sleep(0.5)
        names = set()
        for line in find_base.stdout.splitlines():
            name = line.strip().split('/')[-1]
            name = name.split('_')[0]
            names.add(name)
        for name in sorted(names):
            print(name)

        time.sleep(0.5)
        print('Begining aligment')
        print('-----------------')
        get_home()
        #defining bases 
        for name in sorted(names):
            fq1 = os.path.join('sra', name + '_pass_1.fastq')
            fq2 = os.path.join('sra', name + '_pass_2.fastq')
            aligned_read = os.path.join(output_dir, name)
            

        
        
        time.sleep(0.5)
        map = subprocess.run("STAR --runThreadN 10 --genomeDir " + index_dir + " " "--readFilesIn " + fq1 + " " + fq2 + " " "--outSAMtype BAM SortedByCoordinate --quantMode GeneCounts " "--outFileNamePrefix " + aligned_read + "_", shell=True)
        if map.returncode !=0: 
            print('Error occured')
        else: 
            print('Finised')  


find_reads()


 
