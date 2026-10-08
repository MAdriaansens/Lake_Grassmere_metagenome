Filtered_list =[]
from Bio import SeqIO
Quick_dict={}
for record in SeqIO.parse('/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/NR_CPA_sequences_GTDB226_bins_contigs_hmmaligned_filtered.fasta.fasta', 'fasta'):
    Filtered_list.append(record.id)
    Quick_dict[record.id] = record.seq
import glob
test_list = []
blast_bins_dict={}
for entry in glob.glob('/home/mad149/Metagenome_grassmere/Diamond/Diamond_blastp/Bins/*'):
    with open(entry, 'r') as bin_blastp:
        for line in bin_blastp:
            test_list.append(line.split('\t')[0])
            blast_bins_dict[line.split('\t')[0]] = line.split('\t')[1]
print(len(test_list))
print(len(set(test_list)))


bin_CPA_best_hit_CPA = {}
for entry in Filtered_list:
    if 'metabat' in entry:
        if ("NODE" + entry.split("NODE", 1)[1]) in blast_bins_dict:
            bin_CPA_best_hit_CPA[entry] = blast_bins_dict[ ("NODE" + entry.split("NODE", 1)[1])]
test_list = []
blast_contigs_dict={}
#this gives the CPA to which a CPA in a contig was best hit by, since we first did bins and then included bins we have a directory telling us 
#if a bin CPA hit a contig CPA we know to which CPA that bin CPA hit best to
for entry in glob.glob('/home/mad149/Metagenome_grassmere/Diamond/Diamond_blastp/Contigs/*'):
    with open(entry, 'r') as contig_blastp:
        for line in contig_blastp:
            test_list.append(line.split('\t')[0])
            blast_contigs_dict[line.split('\t')[0]] = line.split('\t')[1]
print(len(test_list))
print(len(set(test_list)))
print(line.split('\t')[0])
print( blast_contigs_dict[line.split('\t')[0]])

for number in list(range(1, 17)):
    Hit_dict={}
    with open('/home/mad149/Metagenome_grassmere/output_xblast_NRCPA/NRCPA/Z37TGN_{}_sample_{}_R1_vs_NRCPA_DB.m8'.format(number, number), 'r') as R1:
        for line in R1:
            read_id = line.split('\t')[0]
            sequence =  line.split('\t')[-1].split('\n')[0]
            hit_protein = line.split('\t')[1]

            e_value = float(line.split('\t')[3].split('e')[0])*10**float(line.split('\t')[3].split('e')[-1])
            bit_value = float(line.split('\t')[-3])
            if read_id not in Hit_dict:
                Hit_dict[read_id] = [hit_protein, e_value, bit_value, sequence]
            else:
                if hit_protein != Hit_dict[read_id][0]:
                    if e_value > Hit_dict[read_id][1]:
                        pass
                    elif e_value < Hit_dict[read_id][1]:
                            #print(e_value, Hit_dict[read_id][1])
                        Hit_dict[read_id] = [hit_protein, e_value, bit_value, sequence]
                    else:
                        if bit_value > Hit_dict[read_id][2]:
                            Hit_dict[read_id] = [hit_protein, e_value, bit_value, sequence]
                        else:
                            #print(len(line.split('\t')[-1].split('\n')[0]), len(Hit_dict[read_id][-1]))
                            if len(line.split('\t')[-1].split('\n')[0]) > len(Hit_dict[read_id][-1]):
                                Hit_dict[read_id] = [hit_protein, e_value, bit_value, sequence]
                            elif len(line.split('\t')[-1].split('\n')[0]) < len(Hit_dict[read_id][-1]):
                                pass
                            else:
                                #in this scenario the read maps onto two different sequences however they are both from the same organism
                                #we see that they have the same subfmailies and often the same family or genera, if 
                                if 'metabat' in line.split('\t')[1]:
                                    print(line)
                                    if bin_CPA_best_hit_CPA[line.split('\t')[1]].split('_Protein:')[-1] == Hit_dict[read_id][0].split('_Protein:')[-1]:
                                        pass
                                    else:
                                        print('error')
                                elif line.split('\t')[1].split(':')[-1] == Hit_dict[read_id][0].split('_Protein:')[-1]:
                                    pass
                                else:
                                    print('check it out')
                                    break 
                                    
    with open('/home/mad149/Metagenome_grassmere/output_xblast_NRCPA/NRCPA/Z37TGN_{}_sample_{}_R1_vs_NRCPA_DB.m8'.format(number, number), 'r') as R2:
        for line in R2:
            read_id = line.split('\t')[0]
            sequence =  line.split('\t')[-1].split('\n')[0]
            hit_protein = line.split('\t')[1]
            e_value = float(line.split('\t')[3].split('e')[0])*10**float(line.split('\t')[3].split('e')[-1])
            bit_value = float(line.split('\t')[-3])
            if read_id not in Hit_dict:
                Hit_dict[read_id] = [hit_protein, e_value, bit_value, sequence]
            else:
                if hit_protein != Hit_dict[read_id][0]:
                    if e_value > Hit_dict[read_id][1]:
                        pass
                    elif e_value < Hit_dict[read_id][1]:
                            #print(e_value, Hit_dict[read_id][1])
                        Hit_dict[read_id] = [hit_protein, e_value, bit_value, sequence]
                    else:
                        if bit_value > Hit_dict[read_id][2]:
                            Hit_dict[read_id] = [hit_protein, e_value, bit_value, sequence]
                        else:
                            #print(len(line.split('\t')[-1].split('\n')[0]), len(Hit_dict[read_id][-1]))
                            if len(line.split('\t')[-1].split('\n')[0]) > len(Hit_dict[read_id][-1]):
                                Hit_dict[read_id] = [hit_protein, e_value, bit_value, sequence]
                            elif len(line.split('\t')[-1].split('\n')[0]) < len(Hit_dict[read_id][-1]):
                                pass
                            else:
                                #in this scenario the read maps onto two different sequences however they are both from the same organism
                                #we see that they have the same subfmailies and often the same family or genera, if 
                                if 'metabat' in line.split('\t')[1]:
                                    print(line)
                                    if bin_CPA_best_hit_CPA[line.split('\t')[1]].split('_Protein:')[-1] == Hit_dict[read_id][0].split('_Protein:')[-1]:
                                        pass
                                    else:
                                        print('error')
                                elif line.split('\t')[1].split(':')[-1] == Hit_dict[read_id][0].split('_Protein:')[-1]:
                                    pass
                                else:
                                    print('check it out')
                                    break 
    from collections import Counter
    Hit_list =[]
    with open('/home/mad149/Metagenome_grassmere/output_xblast_NRCPA/Z37TGN_sample_{}_vs_NRCPA_DB_counted_and_mapped.tsv'.format(number), 'w') as output:
        header = 'Protein_id' + '\t' + 'subfamily' + '\t' + 'Reads_mapped_to_protein' + '\n'
        output.write(header)
        for key in Hit_dict:
            Hit_list.append(Hit_dict[key][0])
        for Hit in list(set(Hit_list)):
            Protein_id = Hit
            if '_tax:' in Protein_id:
                subfamily = Protein_id.split('_Protein:')[-1]
            else:
                #we got to which ever protein originally hit this cpa in a bin
                if Protein_id in bin_CPA_best_hit_CPA:
                    subfamily = bin_CPA_best_hit_CPA[Protein_id].split('_Protein:')[-1]
                #this means we map onto a contig CPA
                else:
                    if '_tax:' in blast_contigs_dict[Protein_id.split('_contig_')[1]]:
                        subfamily = blast_contigs_dict[Protein_id.split('_contig_')[1]].split('_Protein:')[-1]
                    else:
                        if blast_contigs_dict[Protein_id.split('_contig_')[1]] in bin_CPA_best_hit_CPA:
                            subfamily = bin_CPA_best_hit_CPA[blast_contigs_dict[Protein_id.split('_contig_')[1]]].split('_Protein:')[-1]
                        else:
                            subfamily = (blast_bins_dict['NODE' + blast_contigs_dict[Protein_id.split('_contig_')[1]].split('NODE')[1]]).split('_Protein:')[-1]
            Reads_mapped_to_protein = Hit_list.count(Hit)
            line = Protein_id + '\t' + subfamily + '\t' + str(Reads_mapped_to_protein) + '\n'
            output.write(line)
for number in list(range(1, 17)):
    Hit_dict={}
    with open('/home/mad149/Metagenome_grassmere/output_xblast_NRCPA/Seqid70_NR/Z37TGN_{}_sample_{}_R1_vs_NRCPA_70seqidDB.m8'.format(number, number), 'r') as R1:
        for line in R1:
            read_id = line.split('\t')[0]
            sequence =  line.split('\t')[-1].split('\n')[0]
            hit_protein = line.split('\t')[1]

            e_value = float(line.split('\t')[3].split('e')[0])*10**float(line.split('\t')[3].split('e')[-1])
            bit_value = float(line.split('\t')[-3])
            if read_id not in Hit_dict:
                Hit_dict[read_id] = [hit_protein, e_value, bit_value, sequence]
            else:
                if hit_protein != Hit_dict[read_id][0]:
                    if e_value > Hit_dict[read_id][1]:
                        pass
                    elif e_value < Hit_dict[read_id][1]:
                            #print(e_value, Hit_dict[read_id][1])
                        Hit_dict[read_id] = [hit_protein, e_value, bit_value, sequence]
                    else:
                        if bit_value > Hit_dict[read_id][2]:
                            Hit_dict[read_id] = [hit_protein, e_value, bit_value, sequence]
                        else:
                            #print(len(line.split('\t')[-1].split('\n')[0]), len(Hit_dict[read_id][-1]))
                            if len(line.split('\t')[-1].split('\n')[0]) > len(Hit_dict[read_id][-1]):
                                Hit_dict[read_id] = [hit_protein, e_value, bit_value, sequence]
                            elif len(line.split('\t')[-1].split('\n')[0]) < len(Hit_dict[read_id][-1]):
                                pass
                            else:
                                #in this scenario the read maps onto two different sequences however they are both from the same organism
                                #we see that they have the same subfmailies and often the same family or genera, if 
                                if 'metabat' in line.split('\t')[1]:
                                    print(line)
                                    if bin_CPA_best_hit_CPA[line.split('\t')[1]].split('_Protein:')[-1] == Hit_dict[read_id][0].split('_Protein:')[-1]:
                                        pass
                                    else:
                                        print('error')
                                elif line.split('\t')[1].split(':')[-1] == Hit_dict[read_id][0].split('_Protein:')[-1]:
                                    pass
                                else:
                                    print('check it out')
                                    break 
                                    
    with open('/home/mad149/Metagenome_grassmere/output_xblast_NRCPA/Seqid70_NR/Z37TGN_{}_sample_{}_R2_vs_NRCPA_70seqidDB.m8'.format(number, number), 'r') as R2:
        for line in R2:
            read_id = line.split('\t')[0]
            sequence =  line.split('\t')[-1].split('\n')[0]
            hit_protein = line.split('\t')[1]
            e_value = float(line.split('\t')[3].split('e')[0])*10**float(line.split('\t')[3].split('e')[-1])
            bit_value = float(line.split('\t')[-3])
            if read_id not in Hit_dict:
                Hit_dict[read_id] = [hit_protein, e_value, bit_value, sequence]
            else:
                if hit_protein != Hit_dict[read_id][0]:
                    if e_value > Hit_dict[read_id][1]:
                        pass
                    elif e_value < Hit_dict[read_id][1]:
                            #print(e_value, Hit_dict[read_id][1])
                        Hit_dict[read_id] = [hit_protein, e_value, bit_value, sequence]
                    else:
                        if bit_value > Hit_dict[read_id][2]:
                            Hit_dict[read_id] = [hit_protein, e_value, bit_value, sequence]
                        else:
                            #print(len(line.split('\t')[-1].split('\n')[0]), len(Hit_dict[read_id][-1]))
                            if len(line.split('\t')[-1].split('\n')[0]) > len(Hit_dict[read_id][-1]):
                                Hit_dict[read_id] = [hit_protein, e_value, bit_value, sequence]
                            elif len(line.split('\t')[-1].split('\n')[0]) < len(Hit_dict[read_id][-1]):
                                pass
                            else:
                                #in this scenario the read maps onto two different sequences however they are both from the same organism
                                #we see that they have the same subfmailies and often the same family or genera, if 
                                if 'metabat' in line.split('\t')[1]:
                                    print(line)
                                    if bin_CPA_best_hit_CPA[line.split('\t')[1]].split('_Protein:')[-1] == Hit_dict[read_id][0].split('_Protein:')[-1]:
                                        pass
                                    else:
                                        print('error')
                                elif line.split('\t')[1].split(':')[-1] == Hit_dict[read_id][0].split('_Protein:')[-1]:
                                    pass
                                else:
                                    print('check it out')
                                    break 
    from collections import Counter
    Hit_list =[]
    with open('/home/mad149/Metagenome_grassmere/output_xblast_NRCPA/Z37TGN_sample_{}_vs_NRCPA_70seqidDB_counted_and_mapped.tsv'.format(number), 'w') as output:
        header = 'Protein_id' + '\t' + 'subfamily' + '\t' + 'Reads_mapped_to_protein' + '\n'
        output.write(header)
        for key in Hit_dict:
            Hit_list.append(Hit_dict[key][0])
        for Hit in list(set(Hit_list)):
            Protein_id = Hit
            if '_tax:' in Protein_id:
                subfamily = Protein_id.split('_Protein:')[-1]
            else:
                #we got to which ever protein originally hit this cpa in a bin
                if Protein_id in bin_CPA_best_hit_CPA:
                    subfamily = bin_CPA_best_hit_CPA[Protein_id].split('_Protein:')[-1]
                #this means we map onto a contig CPA
                else:
                    if '_tax:' in blast_contigs_dict[Protein_id.split('_contig_')[1]]:
                        subfamily = blast_contigs_dict[Protein_id.split('_contig_')[1]].split('_Protein:')[-1]
                    else:
                        if blast_contigs_dict[Protein_id.split('_contig_')[1]] in bin_CPA_best_hit_CPA:
                            subfamily = bin_CPA_best_hit_CPA[blast_contigs_dict[Protein_id.split('_contig_')[1]]].split('_Protein:')[-1]
                        else:
                            subfamily = (blast_bins_dict['NODE' + blast_contigs_dict[Protein_id.split('_contig_')[1]].split('NODE')[1]]).split('_Protein:')[-1]
            Reads_mapped_to_protein = Hit_list.count(Hit)
            line = Protein_id + '\t' + subfamily + '\t' + str(Reads_mapped_to_protein) + '\n'
            output.write(line)
for number in list(range(1, 17)):
    Hit_dict={}
    with open('/home/mad149/Metagenome_grassmere/output_xblast_NRCPA/treeCPA/Z37TGN_{}_sample_{}_R1_vs_treeCPA_DB.m8'.format(number, number), 'r') as R1:
        for line in R1:
            read_id = line.split('\t')[0]
            sequence =  line.split('\t')[-1].split('\n')[0]
            hit_protein = line.split('\t')[1]

            e_value = float(line.split('\t')[3].split('e')[0])*10**float(line.split('\t')[3].split('e')[-1])
            bit_value = float(line.split('\t')[-3])
            if read_id not in Hit_dict:
                Hit_dict[read_id] = [hit_protein, e_value, bit_value, sequence]
            else:
                if hit_protein != Hit_dict[read_id][0]:
                    if e_value > Hit_dict[read_id][1]:
                        pass
                    elif e_value < Hit_dict[read_id][1]:
                            #print(e_value, Hit_dict[read_id][1])
                        Hit_dict[read_id] = [hit_protein, e_value, bit_value, sequence]
                    else:
                        if bit_value > Hit_dict[read_id][2]:
                            Hit_dict[read_id] = [hit_protein, e_value, bit_value, sequence]
                        else:
                            #print(len(line.split('\t')[-1].split('\n')[0]), len(Hit_dict[read_id][-1]))
                            if len(line.split('\t')[-1].split('\n')[0]) > len(Hit_dict[read_id][-1]):
                                Hit_dict[read_id] = [hit_protein, e_value, bit_value, sequence]
                            elif len(line.split('\t')[-1].split('\n')[0]) < len(Hit_dict[read_id][-1]):
                                pass
                            else:
                                #in this scenario the read maps onto two different sequences however they are both from the same organism
                                #we see that they have the same subfmailies and often the same family or genera, if 
                                if 'metabat' in line.split('\t')[1]:
                                    print(line)
                                    if bin_CPA_best_hit_CPA[line.split('\t')[1]].split('_Protein:')[-1] == Hit_dict[read_id][0].split('_Protein:')[-1]:
                                        pass
                                    else:
                                        print('error')
                                elif line.split('\t')[1].split(':')[-1] == Hit_dict[read_id][0].split('_Protein:')[-1]:
                                    pass
                                else:
                                    print('check it out')
                                    break 
                                    
    with open('/home/mad149/Metagenome_grassmere/output_xblast_NRCPA/treeCPA/Z37TGN_{}_sample_{}_R2_vs_treeCPA_DB.m8'.format(number, number), 'r') as R2:
        for line in R2:
            read_id = line.split('\t')[0]
            sequence =  line.split('\t')[-1].split('\n')[0]
            hit_protein = line.split('\t')[1]
            e_value = float(line.split('\t')[3].split('e')[0])*10**float(line.split('\t')[3].split('e')[-1])
            bit_value = float(line.split('\t')[-3])
            if read_id not in Hit_dict:
                Hit_dict[read_id] = [hit_protein, e_value, bit_value, sequence]
            else:
                if hit_protein != Hit_dict[read_id][0]:
                    if e_value > Hit_dict[read_id][1]:
                        pass
                    elif e_value < Hit_dict[read_id][1]:
                            #print(e_value, Hit_dict[read_id][1])
                        Hit_dict[read_id] = [hit_protein, e_value, bit_value, sequence]
                    else:
                        if bit_value > Hit_dict[read_id][2]:
                            Hit_dict[read_id] = [hit_protein, e_value, bit_value, sequence]
                        else:
                            #print(len(line.split('\t')[-1].split('\n')[0]), len(Hit_dict[read_id][-1]))
                            if len(line.split('\t')[-1].split('\n')[0]) > len(Hit_dict[read_id][-1]):
                                Hit_dict[read_id] = [hit_protein, e_value, bit_value, sequence]
                            elif len(line.split('\t')[-1].split('\n')[0]) < len(Hit_dict[read_id][-1]):
                                pass
                            else:
                                #in this scenario the read maps onto two different sequences however they are both from the same organism
                                #we see that they have the same subfmailies and often the same family or genera, if 
                                if 'metabat' in line.split('\t')[1]:
                                    print(line)
                                    if bin_CPA_best_hit_CPA[line.split('\t')[1]].split('_Protein:')[-1] == Hit_dict[read_id][0].split('_Protein:')[-1]:
                                        pass
                                    else:
                                        print('error')
                                elif line.split('\t')[1].split(':')[-1] == Hit_dict[read_id][0].split('_Protein:')[-1]:
                                    pass
                                else:
                                    print('check it out')
                                    break 
    from collections import Counter
    Hit_list =[]
    with open('/home/mad149/Metagenome_grassmere/output_xblast_NRCPA/Z37TGN_sample_{}_vs_treeCPAreps_counted_and_mapped.tsv'.format(number), 'w') as output:
        header = 'Protein_id' + '\t' + 'subfamily' + '\t' + 'Reads_mapped_to_protein' + '\n'
        output.write(header)
        for key in Hit_dict:
            Hit_list.append(Hit_dict[key][0])
        for Hit in list(set(Hit_list)):
            Protein_id = Hit
            if '_tax:' in Protein_id:
                subfamily = Protein_id.split('_Protein:')[-1]
            else:
                #we got to which ever protein originally hit this cpa in a bin
                if Protein_id in bin_CPA_best_hit_CPA:
                    subfamily = bin_CPA_best_hit_CPA[Protein_id].split('_Protein:')[-1]
                #this means we map onto a contig CPA
                else:
                    if '_tax:' in blast_contigs_dict[Protein_id.split('_contig_')[1]]:
                        subfamily = blast_contigs_dict[Protein_id.split('_contig_')[1]].split('_Protein:')[-1]
                    else:
                        if blast_contigs_dict[Protein_id.split('_contig_')[1]] in bin_CPA_best_hit_CPA:
                            subfamily = bin_CPA_best_hit_CPA[blast_contigs_dict[Protein_id.split('_contig_')[1]]].split('_Protein:')[-1]
                        else:
                            subfamily = (blast_bins_dict['NODE' + blast_contigs_dict[Protein_id.split('_contig_')[1]].split('NODE')[1]]).split('_Protein:')[-1]
            Reads_mapped_to_protein = Hit_list.count(Hit)
            line = Protein_id + '\t' + subfamily + '\t' + str(Reads_mapped_to_protein) + '\n'
            output.write(line)
