Best_hit_CPA_bins={}
import glob
with open('/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/retrieved_from_bins/CPA_sequences_vs_HQMQ_bins_rerun.fasta', 'w') as outfile:
    for blastp in glob.glob('/home/mad149/Metagenome_grassmere/Diamond/Diamond_blastp/Bins/metabat2_isolate_*_CPA.tsv'):
        with open(blastp, 'r') as parse:
                count = 0
                for line in parse:   
                    if '_Protein' in line:
                        sequence=line.split('\n')[0].split('\t')[-1]
                        if len(sequence) > 262:                                  
                            
                            title = '>' + (blastp.split('/')[-1].split('_vs_all_CPA.tsv')[0])+ '_CPA_count{}'.format(count) +'_' + line.split('\t')[0] + '_Protein:' + line.split('\t')[1].split('Protein:')[-1]
                            x_count = sequence.count('X')
                            
                            if x_count == 0 or (len(sequence) / x_count) < 0.2:
                                fasta = title + '\n' + sequence + '\n'
                                outfile.write(fasta)
                                Best_hit_CPA_bins[title.split('>')[1]] = line.split('\t')[1] 
                                count += 1
                                


with open('/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/retrieved_from_contigs/CPA_sequences_vs_contigs_rerun.fasta', 'w') as outfile:
    for blastp in glob.glob('/home/mad149/Metagenome_grassmere/Diamond/Diamond_blastp/Contigs/*.tsv'):
        print(blastp)
        with open(blastp, 'r') as parse:
                count = 0
                for line in parse:   
                    if '_Protein' in line:
                        sequence=line.split('\n')[0].split('\t')[-1]
                        if len(sequence) > 262:                                  
                            
                            title = '>' + (blastp.split('/')[-1].split('_blastp_vs_protein_CPA.tsv')[0])+ '_contig_CPA_count{}'.format(count) +'_' + line.split('\t')[0] + '_Protein:' + line.split('\t')[1].split('Protein:')[-1]

                            x_count = sequence.count('X')
                            
                            if x_count == 0 or (len(sequence) / x_count) < 0.2:
                                fasta = title + '\n' + sequence + '\n'
                                outfile.write(fasta)
                                Best_hit_CPA_bins[title.split('>')[1]] = line.split('\t')[1] 
                                count += 1
from Bio import SeqIO
def find_error(input_fasta, Best_hit_CPA_bins):
    error='all good'
    for record in SeqIO.parse(input_fasta, 'fasta'):
        if 'NODE' in record.id:
            if record.id not in Best_hit_CPA_bins:
                error='error was found'
                print("ERROR in {}".format(input_fasta))
                break
    print(error, input_fasta)
    
find_error('/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/retrieved_from_bins/CPA_sequences_vs_HQMQ_bins_rerun.fasta', Best_hit_CPA_bins)
find_error('/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/retrieved_from_bins/PF00999_CPA_vsCPA_HQMQ_bins_hmmaligned_filtered_fl.fasta', Best_hit_CPA_bins)
find_error('/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/retrieved_from_contigs/CPA_sequences_vs_contigs_rerun.fasta', Best_hit_CPA_bins)
find_error('/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/retrieved_from_contigs/NR_CPA_sequences_contigs_hmmaligned_filtered_fl.fasta', Best_hit_CPA_bins)
find_error('/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/PF00999NR_CPA_sequences_Adriaansens_bins_contigs_hmmaligned_filtered.fasta', Best_hit_CPA_bins)
find_error('/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/PF00999NR_CPA_sequences_Adriaansens_bins_contigs_hmmaligned_filtered_clustered_70.fasta_rep_seq.fasta', Best_hit_CPA_bins)

#should all return 'all good'

hit_dictionary={}
for i in range(1,15):
    with open('/home/mad149/Metagenome_grassmere/output_xblast_NRCPA/Z37TGN_{}_sample_{}_R1_vs_NRCPA_DB.m8'.format(i,i), 'r') as blastp:
        for line in blastp:
            if 'NODE' in line:
                if line.split('\t')[1] not in Best_hit_CPA_bins:
                    print(line)
    with open('/home/mad149/Metagenome_grassmere/output_xblast_NRCPA/Z37TGN_{}_sample_{}_R2_vs_NRCPA_DB.m8'.format(i,i), 'r') as blastp:
        for line in blastp:
            if 'NODE' in line:
                if line.split('\t')[1] not in Best_hit_CPA_bins:
                    print(line)
hit_dictionary={}
for i in range(1,15):
    with open('/home/mad149/Metagenome_grassmere/output_xblast_NRCPA/Z37TGN_{}_sample_{}_R1_vs_NRCPA_DB.m8'.format(i,i), 'r') as blastp:
        for line in blastp:
            read_id = line.split('\t')[0]
            protein_hit_id = line.split('\t')[1]
            e_value = float(line.split('\t')[3])
            if read_id not in hit_dictionary:
                hit_dictionary[read_id] = (protein_hit_id, e_value)
            else:
                old_e_value = hit_dictionary[read_id][1]
                if e_value < old_e_value:
                    hit_dictionary[read_id] = (protein_hit_id, e_value)
                elif e_value > old_e_value:
                    pass
                elif e_value == old_e_value:
                    hit_dictionary.pop(read_id)
    with open('/home/mad149/Metagenome_grassmere/output_xblast_NRCPA/Z37TGN_{}_sample_{}_R2_vs_NRCPA_DB.m8'.format(i,i), 'r') as blastp:
        for line in blastp:
            read_id = line.split('\t')[0]
            protein_hit_id = line.split('\t')[1]
            e_value = float(line.split('\t')[3])
            if read_id not in hit_dictionary:
                hit_dictionary[read_id] = (protein_hit_id, e_value)
            else:
                old_e_value = hit_dictionary[read_id][1]
                if e_value < old_e_value:
                    hit_dictionary[read_id] = (protein_hit_id, e_value)
                elif e_value > old_e_value:
                    pass
                elif e_value == old_e_value:
                    hit_dictionary.pop(read_id)  


hit_list = []
for value in set(hit_dictionary.values()):
    hit_list.append(value[0])
unique_hit_list = list(set(hit_list))
print(len(unique_hit_list))


import os
import glob
import csv
from collections import Counter, defaultdict


# ============================================================
# 1. Load GTDB-Tk taxonomy
# ============================================================

GTDBtk_dict = {}

taxonomy_file = (
    '/home/mad149/Metagenome_grassmere/'
    'Suppl_Chapter_Four_STable4dot12.csv'
)

with open(taxonomy_file, 'r', newline='') as gtdb:
    reader = csv.reader(gtdb)

    for row in reader:
        if len(row) >= 2:
            GTDBtk_dict[row[0].strip()] = row[1].strip()

new_hit_dictionary = {}
from collections import Counter
with open('/home/mad149/Metagenome_grassmere/treeCPAs_hit_per_sample.tsv', 'w') as output:
    header = 'protein_hit' + '\t' + 'best_tree_CPA' + '\t' + 'count_hit' + '\t' + 'sample' + '\n'
    output.write(header)
    for i in range(1, 15):
        protein_hit_list = []
        for read_file in ['R1', 'R2']:
            filename = '/home/mad149/Metagenome_grassmere/output_xblast_NRCPA/Z37TGN_{}_sample_{}_{}_vs_NRCPA_DB.m8'.format(i, i, read_file)
            with open(filename, 'r') as blastp:
                for line in blastp:
                    columns = line.strip().split('\t')
                    read_id = columns[0]
                    protein_hit_id = columns[1]
                    e_value = float(columns[3])
                    if read_id not in new_hit_dictionary:
                        new_hit_dictionary[read_id] = (protein_hit_id, e_value)
                        protein_hit_list.append(protein_hit_id)
                    else:
                        old_protein, old_e_value = new_hit_dictionary[read_id]
                        if e_value < old_e_value:
                            new_hit_dictionary[read_id] = (protein_hit_id, e_value)
                            protein_hit_list[protein_hit_list.index(old_protein)] = protein_hit_id
                        elif e_value == old_e_value:
                            new_hit_dictionary.pop(read_id)
                            protein_hit_list.remove(old_protein)
        counts = Counter(protein_hit_list)
        for unique_hit in unique_hit_list:
            if 'NODE' not in unique_hit[0]:
                #then a tree CPA was it
                count_hit = counts[unique_hit[0]]
                tree_CPA = unique_hit[0]
                Line = (unique_hit[0] + '\t' +  tree_CPA +'\t' + str(count_hit) + '\t' + str(i)+'\n')
                output.write(Line)
            elif 'Metaspades_isolate_contig' in unique_hit[0]:
                count_hit = counts[unique_hit[0]]
                tree_CPA = Best_hit_CPA_bins[unique_hit[0]]
                if 'NODE' in tree_CPA:
                    #means a mag is the closest hit to a contig CPA
                    MAG_id = (tree_CPA.split('_CPA_count')[0])
                    taxa=GTDBtk_dict[MAG_id] 
                    subfamily=tree_CPA.split(':')[-1]
                    new_title = MAG_id + '_taxa:' + taxa + '_Protein:' + subfamily
                    Line = (unique_hit[0] + '\t' +  new_title +'\t' + str(count_hit) + '\t' + str(i)+'\n')
                    output.write(Line)
                else:
                    Line = (unique_hit[0] + '\t' +  tree_CPA +'\t' + str(count_hit) + '\t' + str(i)+'\n')
                    output.write(Line)
            elif 'metabat2_isolate_spades' in unique_hit[0]:
                count_hit = counts[unique_hit[0]]
                tree_CPA = Best_hit_CPA_bins[unique_hit[0]]
                Line = (unique_hit[0] + '\t' +  tree_CPA +'\t' + str(count_hit) + '\t' + str(i)+'\n')
                output.write(Line)
                
        
        print('done {}'.format(filename))

