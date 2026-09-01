Good_list = []

with open('Best_assembly_bins.txt', 'r') as bins:
    for entry in bins:
        Good_list.append(entry.split('\n')[0])
print(len(Good_list))
print(len(set(Good_list)))
print(Good_list)

import subprocess

import glob
count = 0
ran_list = []
for MAG in glob.glob('Diamond_blastp/Metabat_Isolate/*tsv'):
    if (MAG.split('/')[-1].split('_blastp')[0]) in Good_list:
        count = count + 1
    elif (MAG.split('/')[-1].split('.fa_blastp')[0]) in Good_list:
        count = count + 1
print(count)

import glob
count = 0
ran_list = []
for MAG in glob.glob('Diamond_blastp/Metabat_Isolate/*tsv'):
    if (MAG.split('/')[-1].split('.fa_blastp')[0]) in Good_list:
        print(MAG)
        subprocess.run(['mv', '{}'.format(MAG), '/home/mad149/Metagenome_grassmere/Diamond_blastp/Best_bins_postDrep/'])    
    else:
        pass
print(count)
import os
import glob

with open('MetaBat_isolate_postDrep_CPAs.fasta'.format(directory), 'w') as outfile:
    for blastp in glob.glob('Diamond_blastp/Best_bins_postDrep/*tsv'):
        with open(blastp, 'r') as parse:
                        count = 0
                        for line in parse:
                            if '_Protein' in line:
                                sequence=line.split('\n')[0].split('\t')[-1]
                                if len(sequence) > 262:                                  
                                    if '_blastp_' in blastp:
                                        title = '>' + (blastp.split('/')[-1].split('_blastp_vs_protein')[0]) + '_' + line.split('\t')[0] + '_CPA_{}_protein:'.format(count)+ line.split('\t')[1].split('Protein:')[-1]
                                        
                                    elif '.fa_blastp_' in blastp:
                                        title = '>' + (blastp.split('/')[-1].split('.fa_blastp_vs_protein')[0])+ '_' + line.split('\t')[0] + '_CPA_{}_protein:'.format(count)+ line.split('\t')[1].split('Protein:')[-1]
                                    if sequence.count('X') == 0:
                                        fasta = title + '\n' + sequence + '\n'
                                        count = count + 1
                                        outfile.write(fasta)
                                    elif (len(sequence)/sequence.count('X')) < 0.2:
                                        fasta = title + '\n' + sequence + '\n'
                                        count = count + 1
                                        outfile.write(fasta)
import os
import glob

with open('MetaBat_isolate_postDrep_Hpase.fasta', 'w') as outfile:
    for blastp in glob.glob('Diamond_blastp/Best_bins_postDrep/*tsv'):
        with open(blastp, 'r') as parse:
                        count = 0
                        for line in parse:
                            if 'H_PPase' in line:
                                print(line)
                                sequence=line.split('\n')[0].split('\t')[-1]
                                if len(sequence) > 452:                                  
                                    if '_blastp_' in blastp:
                                        title = '>' + (blastp.split('/')[-1].split('_blastp_vs_protein')[0]) + '_' + line.split('\t')[0] + '_Hppase_{}_protein:'.format(count)+ line.split('\t')[1].split('Protein:')[-1]
                                        
                                    elif '.fa_blastp_' in blastp:
                                        title = '>' + (blastp.split('/')[-1].split('.fa_blastp_vs_protein')[0])+ '_' + line.split('\t')[0] + '_Hppase_{}_protein:'.format(count)+ line.split('\t')[1].split('Protein:')[-1]
                                    if sequence.count('X') == 0:
                                        fasta = title + '\n' + sequence + '\n'
                                        count = count + 1
                                        outfile.write(fasta)
                                    elif (len(sequence)/sequence.count('X')) < 0.2:
                                        fasta = title + '\n' + sequence + '\n'
                                        count = count + 1
                                        outfile.write(fasta)import os
import glob

with open('MetaBat_isolate_postDrep_TrkH.fasta'.format(directory), 'w') as outfile:
    for blastp in glob.glob('Diamond_blastp/Best_bins_postDrep/*tsv'):
        with open(blastp, 'r') as parse:
                        count = 0
                        for line in parse:
                            if 'TrkH' in line:
                                print(line)
                                sequence=line.split('\n')[0].split('\t')[-1]
                                if len(sequence) > 350:                                  
                                    if '_blastp_' in blastp:
                                        title = '>' + (blastp.split('/')[-1].split('_blastp_vs_protein')[0]) + '_' + line.split('\t')[0] + '_TrkH_{}_protein:'.format(count)+ line.split('\t')[1].split('Protein:')[-1]
                                        
                                    elif '.fa_blastp_' in blastp:
                                        title = '>' + (blastp.split('/')[-1].split('.fa_blastp_vs_protein')[0])+ '_' + line.split('\t')[0] + '_TrkH_{}_protein:'.format(count)+ line.split('\t')[1].split('Protein:')[-1]
                                    if sequence.count('X') == 0:
                                        fasta = title + '\n' + sequence + '\n'
                                        count = count + 1
                                        outfile.write(fasta)
                                    elif (len(sequence)/sequence.count('X')) < 0.2:
                                        fasta = title + '\n' + sequence + '\n'
                                        count = count + 1
                                        outfile.write(fasta)
