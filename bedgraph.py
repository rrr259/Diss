#!/usr/bin/python3
import os 
import pandas as pd

print('Creating bedgraph files for vizualization at IGV')

counts_file = 'counts.txt'
df = pd.read_csv(counts_file, sep='\t', comment = '#')

#now need to separate counts by strands so can have two sep files for both strands 
df_counts_pos = df[df['Strand'] == '+']
df_counts_neg = df[df['Strand'] == '-']

# craeting dataframe for + bedgraph 
df_bed_pos = pd.DataFrame()
df_bed_pos['chr'] = df_counts_pos['Chr']
df_bed_pos['start'] = df_counts_pos['Start'] -1 
df_bed_pos['end'] = df_counts_pos['End']
df_bed_pos['score'] = df_counts_pos.iloc[:, -1]

df_bed_pos.to_csv('pos.bedgraph', sep='\t', header=False, index=False)

#creating dataframe for - bedgraph 
df_bed_neg = pd.DataFrame()
df_bed_neg['chr'] = df_counts_neg['Chr']
df_bed_neg['start'] = df_counts_neg['Start'] -1 
df_bed_neg['end'] = df_counts_neg['End']
df_bed_neg['score'] = df_counts_neg.iloc[:, -1]

df_bed_neg.to_csv('neg.bedgraph', sep='\t', header=False, index=False )

print('Bedgraph files are created')

