#/!/user/bin/python3
import os
import subprocess 

bed_file = 'new_bed2.bed'
print('Converting BED cutomized file to GTF')
print('------------------------------------')

bed_to_genepred = subprocess.run('./bedToGenePred ' + bed_file + ' new_bed.genepred', shell=True)
if bed_to_genepred.returncode !=0: 
    print('Error_occured')
else:
    print('Craeted genepred file')
    print('---------------------')

genepred_to_gtf = subprocess.run('./genePredToGtf file new_bed.genepred new_bed2.gtf', shell=True)
if genepred_to_gtf.returncode !=0:
    print('Error occured')
else: 
    print('GTF filed created for featureCounts')
    print('----------------------------------')