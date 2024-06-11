#!/bin/user/python3
import subprocess
import os 

print('Starting to build index')
print('------------------------')
index = subprocess.run('STAR --runMode genomeGenerate --genomeDir ref/ --genomeFastaFiles /home/s2614505/Diss/Mus_musculus.GRCm39.dna_sm.primary_assembly.fa --sjdbGTFfile /home/s2614505/Diss/Mus_musculus.GRCm39.112.gtf --runThreadN 10', shell=True)
print('Finished')


