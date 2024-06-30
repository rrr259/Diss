#/!/user/bin/python3 
import os
import subprocess
import time 
import pandas as pd 



bed_file = 'ann_to_m39.bed'
print('Modifying BED file for further analyis')
print('--------------------------------------')

#need tp generate genome.sizes from fasta file 
fasta_file = 'Mus_musculus.GRCm39.dna_sm.primary_assembly.fa'
fasta_to_fai = subprocess.run('samtools faidx ' + fasta_file, shell=True)
time.sleep(0.5)
if fasta_to_fai.returncode !=0:
    print('Error occured')
else: 
    print('Fai file generated')
    print('------------------')

#by using fai can now create a genome.sizes file that is required for fblank option 
new_fai = fasta_file + '.fai'
gen_size = 'genome.size_now'
fai_to_gen = subprocess.run("awk '{{print $1\"\t\"$2}}' " + new_fai + " > " + gen_size, shell=True)
time.sleep(0.5)
if fai_to_gen.returncode !=0:
    print('Error occured')
else: 
    print('Created genome.size file')
    print('-------------------------')

gen_size_new = 'genome.size'

with open(gen_size, 'r') as infile, open(gen_size_new, 'w') as uotfile:
    for line in infile:
        new_line = line.strip()
        if not new_line.startswith('chr'):
            new_line = 'chr' + new_line
            uotfile.write(new_line +'\n')

#remove genome.size without chr 
os.remove(gen_size)

#using flank to modify bed 
time.sleep(0.5)
bed_file_new = 'new_bed.bed'
bed_to_new = subprocess.run('flankBed -i ' + bed_file + ' -g ' + gen_size_new + ' -b 500 > ' + bed_file_new, shell=True)
time.sleep(0.5)
if bed_to_new.returncode !=0:
    print('Error occured')
else:
    print('flnkBed performed')
    print('---------------------')

print('Now modifying bed file further to contain both strands to identify divergent transcription')
print('---------------------------------------------------------------------------------------')
columns_bed = ['chr', 'strat', 'end', 'gene', 'score', 'strand', 'pos1', 'pos2']
df = pd.read_csv(bed_file_new, sep='\t', names= columns_bed )

df_plus = df.copy()
df_plus['strand'] = '+'

df_minus = df.copy()
df_minus['strand'] = '-'

df_strands = pd.concat([df_plus, df_minus])

new2_bed = 'new_bed2.bed'
df_strands.to_csv(new2_bed, sep='\t', header=False, index=False )
print('Bed file now fully modified :', new2_bed)
print('--------------------------------------------')




