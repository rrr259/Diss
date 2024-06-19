#!/bin/user/python3
import os 
import subprocess 
import time 

gtf_file = 'Mus_musculus.GRCm39.112.gtf'
processed_gtf = 'processed_Mus_musculus.GRCm39.112.gtf'
output_bed = 'mouse_ann.bed'

new_lines =[]
with open(gtf_file, 'r') as infile:
    for line in infile: 
        if 'transcript_id' not in line:
            new_line = line.strip() + ' transcript_id "";'
        else: 
            new_line = line.strip()
        new_lines.append(new_line)

with open(processed_gtf, 'w') as outfile: 
    for line in new_lines:
        outfile.write(line +'\n')






print('Converting GFT to BED file')
print('--------------------------')
gtf_to_bed = subprocess.run('gtf2bed < ' + processed_gtf + ' > ' + output_bed , shell=True)
if gtf_to_bed.returncode !=0:
    print('error occured')
else: 
    time.sleep(0.5)
    print('Done')
