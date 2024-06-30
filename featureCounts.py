#/!/user/bin/python3 
import os 
import subprocess 
import pandas as pd 

STAR_dir = 'aligment'
gtf_new_file = 'new_bed2.gtf'

print('Begining to perform featureCounts')
print('-----------------------------------')


feature = subprocess.run('featureCounts -s 2 -a ' + gtf_new_file + ' -o counts.txt -T 10 -p ' + STAR_dir + '/*bam', shell=True)
if feature.returncode !=0:
    print('Error occured')
else:
    print('Created counts.txt')
    print('-------------------')

    
