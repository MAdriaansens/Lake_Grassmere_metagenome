#goal is to get the read counts to NR CPA 70% seq id and tree CPA homologs.

#first we get all unique treeCPAs hit

hit_dictionary={}
for i in range(1,15):
    with open('/home/mad149/Metagenome_grassmere/output_xblast_NRCPA/Z37TGN_{}_sample_{}_R1_vs_treeCPA_DB.m8'.format(i,i), 'r') as blastp:
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
    with open('/home/mad149/Metagenome_grassmere/output_xblast_NRCPA/Z37TGN_{}_sample_{}_R2_vs_treeCPA_DB.m8'.format(i,i), 'r') as blastp:
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

#then we count how often they occur within each read set

new_hit_dictionary = {}
from collections import Counter
with open('/home/mad149/Metagenome_grassmere/treeCPAs_hit_per_sample.tsv', 'w') as output:
    header = 'protein_hit' + '\t'  + 'count_hit' + '\t' + 'sample' + '\n'
    output.write(header)
    for i in range(1, 15):
        protein_hit_list = []
        for read_file in ['R1', 'R2']:
            filename = '/home/mad149/Metagenome_grassmere/output_xblast_NRCPA/Z37TGN_{}_sample_{}_{}_vs_treeCPA_DB.m8'.format(i, i, read_file)
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
            count_hit = counts[unique_hit]
            Line = (unique_hit + '\t' +  str(count_hit) + '\t' + str(i)+'\n')
            output.write(Line)
        
        print('done {}'.format(filename))

# then repeat these steps for NR 70% seq id

hit_dictionary={}
for i in range(1,15):
    with open('/home/mad149/Metagenome_grassmere/output_xblast_NRCPA/Z37TGN_{}_sample_{}_R1_vs_NRCPA_70seqidDB.m8'.format(i,i), 'r') as blastp:
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
    with open('/home/mad149/Metagenome_grassmere/output_xblast_NRCPA/Z37TGN_{}_sample_{}_R2_vs_NRCPA_70seqidDB.m8'.format(i,i), 'r') as blastp:
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

new_hit_dictionary = {}
from collections import Counter
with open('/home/mad149/Metagenome_grassmere/NRCPA_70seqid_hit_per_sample.tsv', 'w') as output:
    header = 'protein_hit' + '\t'  + 'count_hit' + '\t' + 'sample' + '\n'
    output.write(header)
    for i in range(1, 15):
        protein_hit_list = []
        for read_file in ['R1', 'R2']:
            filename = '/home/mad149/Metagenome_grassmere/output_xblast_NRCPA/Z37TGN_{}_sample_{}_{}_vs_NRCPA_70seqidDB.m8'.format(i, i, read_file)
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
            count_hit = counts[unique_hit]
            Line = (unique_hit + '\t' +  str(count_hit) + '\t' + str(i)+'\n')
            output.write(Line)
        
        print('done {}'.format(filename))

