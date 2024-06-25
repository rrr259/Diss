#/!/bin/user/python3 
import os 
import subprocess
import re

bed_file = 'mouse_ann.bed'
bed_mod = 'modified_mouse_ann.bed'


print('Modifing Bed file')
print('-----------------')

with open(bed_file, 'r') as infile, open(bed_mod, 'w') as outfile:
    for line in infile: 
        new_line = line.strip()
        if new_line and line[0].isdigit():
            new_line = 'chr' + line
            outfile.write('\n' + new_line) 

            
print('Specifying promoter regions for BED file')
promoter_reg = subprocess.run('')



        





