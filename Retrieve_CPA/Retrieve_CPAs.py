Good_list = []
#retrieve all CPA homologs from HQ and Mediumquality bins
with open('HQ_MQ_bins.txt', 'r') as bins:
    for entry in bins:
        Good_list.append(entry.split('\n')[0])
print(len(Good_list))
print(len(set(Good_list)))
import subprocess
import glob
count = 0
ran_list = []
for MAG in glob.glob('Diamond_blastp/*tsv'):
    if (MAG.split('/')[1].split('_blastp')[0]) in Good_list:
        count = count + 1
    elif (MAG.split('/')[1].split('.fa_blastp')[0]) in Good_list:
        count = count + 1
print(count)

import glob
count = 0
ran_list = []
for MAG in glob.glob('Diamond_blastp/*tsv'):
    if (MAG.split('/')[1].split('_blastp')[0]) in Good_list:
        count = count + 1
        if 'metabat2_Metaspades' in MAG:
            subprocess.run(['mv', '{}'.format(MAG), '/home/mad149/Metagenome_grassmere/Diamond_blastp/Metabat_Metaspades'])
        elif 'maxbin2_Metaspades' in MAG:
            subprocess.run(['mv', '{}'.format(MAG), '/home/mad149/Metagenome_grassmere/Diamond_blastp/Maxbin_Metaspades'])   
        elif 'maxbin2_carefull' in MAG:
            subprocess.run(['mv', '{}'.format(MAG), '/home/mad149/Metagenome_grassmere/Diamond_blastp/Maxbin_Carefull'])   
        elif 'metabat2_carefull' in MAG:
            subprocess.run(['mv', '{}'.format(MAG), '/home/mad149/Metagenome_grassmere/Diamond_blastp/Metabat_Carefull'])   
        elif 'maxbin2_isolate' in MAG:
            subprocess.run(['mv', '{}'.format(MAG), '/home/mad149/Metagenome_grassmere/Diamond_blastp/Maxbin_Isolate'])   
        elif 'metabat2_isolate' in MAG:
            subprocess.run(['mv', '{}'.format(MAG), '/home/mad149/Metagenome_grassmere/Diamond_blastp/Metabat_Isolate'])   
        elif 'maxbin2_megahit' in MAG:
            subprocess.run(['mv', '{}'.format(MAG), '/home/mad149/Metagenome_grassmere/Diamond_blastp/Maxbin_Megahit'])   
        elif 'metabat2_megahit' in MAG:
            subprocess.run(['mv', '{}'.format(MAG), '/home/mad149/Metagenome_grassmere/Diamond_blastp/Metabat_Megahit'])  
    elif (MAG.split('/')[1].split('.fa_blastp')[0]) in Good_list:
        count = count + 1
        if 'metabat2_Metaspades' in MAG:
            subprocess.run(['mv', '{}'.format(MAG), '/home/mad149/Metagenome_grassmere/Diamond_blastp/Metabat_Metaspades'])
        elif 'maxbin2_Metaspades' in MAG:
            subprocess.run(['mv', '{}'.format(MAG), '/home/mad149/Metagenome_grassmere/Diamond_blastp/Maxbin_Metaspades'])   
        elif 'maxbin2_carefull' in MAG:
            subprocess.run(['mv', '{}'.format(MAG), '/home/mad149/Metagenome_grassmere/Diamond_blastp/Maxbin_Carefull'])   
        elif 'metabat2_carefull' in MAG:
            subprocess.run(['mv', '{}'.format(MAG), '/home/mad149/Metagenome_grassmere/Diamond_blastp/Metabat_Carefull'])   
        elif 'maxbin2_isolate' in MAG:
            subprocess.run(['mv', '{}'.format(MAG), '/home/mad149/Metagenome_grassmere/Diamond_blastp/Maxbin_Isolate'])   
        elif 'metabat2_isolate' in MAG:
            subprocess.run(['mv', '{}'.format(MAG), '/home/mad149/Metagenome_grassmere/Diamond_blastp/Metabat_Isolate'])   
        elif 'maxbin2_megahit' in MAG:
            subprocess.run(['mv', '{}'.format(MAG), '/home/mad149/Metagenome_grassmere/Diamond_blastp/Maxbin_Megahit'])   
        elif 'metabat2_megahit' in MAG:
            subprocess.run(['mv', '{}'.format(MAG), '/home/mad149/Metagenome_grassmere/Diamond_blastp/Metabat_Megahit'])  
    else:
        pass
print(count)

import os
import glob

for directory in os.listdir('Diamond_blastp'):
    if 'pynb' not in directory:
        print(directory)
        with open('{}_CPAs.fasta'.format(directory), 'w') as outfile:
            for blastp in glob.glob('Diamond_blastp/*/*tsv'):
                if directory in blastp:
                    with open(blastp, 'r') as parse:
                        count = 0
                        for line in parse:
                            if '_Protein' in line:
                                sequence=line.split('\n')[0].split('\t')[-1]
                                if len(sequence) > 255:                                  
                                    if '_blastp_' in blastp:
                                        title = '>' + (blastp.split('/')[-1].split('_blastp_vs_protein')[0]) + '_' + line.split('\t')[0] + '_CPA_{}_protein:'.format(count)+ line.split('\t')[1].split('Protein:')[-1]
                                        
                                    elif '.fa_blastp_' in blastp:
                                        title = '>' + (blastp.split('/')[-1].split('.fa_blastp_vs_protein')[0])+ '_' + line.split('\t')[0] + '_CPA_{}_protein:'.format(count)+ line.split('\t')[1].split('Protein:')[-1]
                                    #ignore sequences smaller than 70% of the CPA HMM, and of whom the sequence makes up more than 20% of the sequence
                                    if sequence.count('X') == 0:
                                        fasta = title + '\n' + sequence + '\n'
                                        count = count + 1
                                        outfile.write(fasta)
                                    elif (len(sequence)/sequence.count('X')) < 0.2:
                                        fasta = title + '\n' + sequence + '\n'
                                        count = count + 1
                                        outfile.write(fasta)
