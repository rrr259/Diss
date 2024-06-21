#/!/user/bin/python3 
import os
import subprocess
import time 

bed_file = 'ann_promoters.bed'
print('Modifying BED file for further analyis')
print('--------------------------------------')

#need tp generate genome.sizes from fasta file 
fasta_file = 'Mus_musculus.GRCm39.dna_sm.primary_assembly.fa'
fasta_to_fai = subprocess.run('samtools faidx ' + fasta_file, shell=True)
if fasta_to_fai.returncode !=0:
    print('Error occured')
else: 
    print('Fai file generated')
    print('------------------')

#by using fai can now create a genome.sizes file that is required for fblank option 
new_fai = fasta_file + '.fai'
gen_size = 'genome.size_now'
fai_to_gen = subprocess.run("awk '{{print $1\"\t\"$2}}' " + new_fai + " > " + gen_size, shell=True)
print('Created genome.size file')
print('-------------------------')

gen_size_new = 'genome.size'

with open(gen_size, 'r') as infile, open(gen_size_new, 'w') as uotfile:
    for line in infile:
        new_line = line.strip()
        if not new_line.startswith('chr'):
            new_line = 'chr' + new_line
            uotfile.write(new_line +'\n')

os.remove(gen_size)
        

#using flank to modify bed 
bed_to_new = subprocess.run('flankBed -i ' + bed_file + ' -g ' + gen_size_new + ' -b 500 > new_bed.bed', shell=True)
print('BED file now modified')


