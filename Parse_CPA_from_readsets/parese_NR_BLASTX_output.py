Kef_dictionary = {}
Kef_list = []
Kef_groupdict = {}
Mj_dictionary={}
with open('/home/mad149/chapter_meta_analysis/Archaea_types_subclades_per_protein_id.tsv', 'r') as Archaea_info:
    for line in Archaea_info:
        if line.split('\t')[2] == '29930':
            Kef_dictionary[line.split('\t')[0].split('_tax')[0]] = line.split('\t')[3]
            Kef_groupdict[line.split('\t')[0].split('_tax')[0]] = line.split('\t')[4]
        elif line.split('\t')[2] == '18786':
            Mj_dictionary[line.split('\t')[0].split('_tax')[0]] = 'MjNah1'
with open('/home/mad149/chapter_meta_analysis/Bacteria_types_subclades_per_protein_id.tsv', 'r') as Bacteria_info:
    for line in Bacteria_info:
        if line.split('\t')[2] == '29930':
            Kef_dictionary[line.split('\t')[0].split('_tax')[0]] = line.split('\t')[3]
            Kef_groupdict[line.split('\t')[0].split('_tax')[0]] = line.split('\t')[4]
        elif line.split('\t')[2] == '18786':
            Mj_dictionary[line.split('\t')[0].split('_tax')[0]] = 'MjNah1'
with open('/home/mad149/chapter_meta_analysis/Eukarya_types_subclades_per_protein_id.tsv', 'r') as Eukarya_info:
    for line in Eukarya_info:
        if line.split('\t')[2] == '29930':
            Kef_dictionary[line.split('\t')[0].split('_tax')[0]] = line.split('\t')[3]
            Kef_groupdict[line.split('\t')[0].split('_tax')[0]] = line.split('\t')[4]
        elif line.split('\t')[2] == '18786':
            Mj_dictionary[line.split('\t')[0].split('_tax')[0]] = 'MjNah1'



import glob
sample_list = []
for entries in glob.glob('/home/mad149/Metagenome_grassmere/output_xblast_NRCPA/*m8'):
    sample_list.append(entries.split('_sample_')[0].split('_')[-1])
    #print(entries)
sample_list = set(sample_list)


with open('/home/mad149/Metagenome_grassmere/reads_mapped_persample_to_CPANR_database_LG.tsv', 'w') as output:
    header = 'Sample' + '\t' +'total_CPA_count' + '\t' + 'Uncharacterized_CPA_count' + '\t' + 'Kef_count' + '\t' + 'NHX(CPA1)_count' + '\t' + 'NhaA_count' + '\t' + 'NhaS5_count' + '\t' + 'CHX_count' + '\t' + 'GerN_count' + '\t' + 'CPA1_SL_count' + '\t' + 'NhaP_CPA1_count' + '\t' + 'SOD2_count' + '\t' + 'Undescribed_CPA1_count' + '\t' +'UndProkarya_CPA1_IDR_count' +'\n'
    output.write(header)
    for sample in sample_list:
        xblast_list_of_interest=[]
        SRR_directory = {}
        SRR_id ='test'
        if sample == '10':
            xblast_list_of_interest.append('/home/mad149/Metagenome_grassmere/output_xblast_NRCPA/Z37TGN_{}_sample__R2_vs_NRCPA_DB.m8'.format(sample))
            xblast_list_of_interest.append('/home/mad149/Metagenome_grassmere/output_xblast_NRCPA/Z37TGN_{}_sample__R1_vs_NRCPA_DB.m8'.format(sample))
        else:
            xblast_list_of_interest.append('/home/mad149/Metagenome_grassmere/output_xblast_NRCPA/Z37TGN_{}_sample_{}_R1_vs_NRCPA_DB.m8'.format(sample, sample))
            xblast_list_of_interest.append('/home/mad149/Metagenome_grassmere/output_xblast_NRCPA/Z37TGN_{}_sample_{}_R2_vs_NRCPA_DB.m8'.format(sample, sample))
        for xblast_output in xblast_list_of_interest:
            with open('{}'.format(xblast_output), 'r') as M8:
                  for line in M8:
                    if line.split('\t')[0] not in SRR_directory:
                        #qseqid sseqid slen evalue bitscore qseq qseq_translated
    
                        SRR_directory[line.split('\t')[0]] = [line.split('\t')[1], line.split('\t')[3], line.split('\t')[-3],line.split('\t')[5].split('\n')[0], line.split('\t')[6].split('\n')[0]]
                    else:
                        #test if protein is identical let it pass, so we do not count it twice
                        if line.split('\t')[1].split('_')[-1] ==  SRR_directory[line.split('\t')[0]][0].split('_')[-1]:
    
                            pass
                        #else protein is not identical so we pick the most significant hit
    
                        else:
                            if float(line.split('\t')[3]) > float(SRR_directory[line.split('\t')[0]][1]):
                               #if new value has a bigger evalue we pass
                                pass
                            elif float(line.split('\t')[3]) < float(SRR_directory[line.split('\t')[0]][1]):
                                #if new value has a smaller evalue we write it in
                                SRR_directory[line.split('\t')[0]] = [line.split('\t')[1], line.split('\t')[3], line.split('\t')[-3],line.split('\t')[5].split('\n')[0], line.split('\t')[6].split('\n')[0]]
                            else:
                                if line.split('\t')[-3] ==  SRR_directory[line.split('\t')[0]][2]:
                                    del SRR_directory[line.split('\t')[0]]
                                    #neither have a higher bit value so I skip them
                                elif line.split('\t')[-3] >  SRR_directory[line.split('\t')[0]][2]:
                                    #the new one has a higher bit value and is selcted
                                    #protein id, e-value, bitscore, protein sequence
                                    SRR_directory[line.split('\t')[0]] = [line.split('\t')[1], line.split('\t')[3], line.split('\t')[-3],line.split('\t')[5].split('\n')[0], line.split('\t')[6].split('\n')[0]]
                                else:
                                    #the original has a higher bit value
                                    pass
            
        xblast_output_dictionary = {}
        xblast_output_dictionary = SRR_directory
    
        SRA_id = sample
        #CPAs
        total_CPA_count = 0
        NHX_count = 0
        Kef_count = 0
        NhaA_count = 0
        Uncharacterized_CPA_count = 0
        NhaS5_count = 0
        CHX_count = 0
        Undescribed_CPA1_count = 0
        SOD2_count = 0
        NhaP_CPA1_count = 0
        Undescribed_CPA1_IDR_count = 0
        GerN_count=0
        CPA1_SL_count=0
        for key in xblast_output_dictionary.keys():
            if 'Protein:' in xblast_output_dictionary[key][0]:
    
                total_CPA_count = total_CPA_count + 1
    
                if xblast_output_dictionary[key][0].split('Protein:')[-1]  == 'Kef':
                    Kef_count = Kef_count + 1      
                elif xblast_output_dictionary[key][0].split('Protein:')[-1]== 'NHX':
                    NHX_count = NHX_count + 1
                elif xblast_output_dictionary[key][0].split('Protein:')[-1] == 'NhaA':
                    NhaA_count = NhaA_count + 1
                elif xblast_output_dictionary[key][0].split('Protein:')[-1] == 'NhaS5':
                    NhaS5_count = NhaS5_count + 1
                elif xblast_output_dictionary[key][0].split('Protein:')[-1] == 'NhaPCPA1':
                    NhaP_CPA1_count= NhaP_CPA1_count + 1
                elif xblast_output_dictionary[key][0].split('Protein:')[-1] == 'Undescribed_CPA1':
                    Undescribed_CPA1_count= Undescribed_CPA1_count + 1
                elif xblast_output_dictionary[key][0].split('Protein:')[-1] == 'CHX':
                    CHX_count = CHX_count + 1
                elif xblast_output_dictionary[key][0].split('Protein:')[-1] == 'SOD2':
                    SOD2_count = SOD2_count + 1
                elif xblast_output_dictionary[key][0].split('Protein:')[-1] == 'GerN':
                    GerN_count = GerN_count + 1
                elif xblast_output_dictionary[key][0].split('Protein:')[-1] == 'CPA1_SL':
                    CPA1_SL_count = CPA1_SL_count + 1
                elif xblast_output_dictionary[key][0].split('Protein:')[-1] == 'UndProkaryaCPA1IDK' or xblast_output_dictionary[key][0].split('Protein:')[-1] == 'UndProkaryaCPA1IDR':
                    Undescribed_CPA1_IDR_count = Undescribed_CPA1_IDR_count + 1
                elif xblast_output_dictionary[key][0].split('Protein:')[-1] =='Uncharacterized':
                    Uncharacterized_CPA_count = Uncharacterized_CPA_count + 1
                    
                                    
    
    
                        #print('count:', 'count:')
            
        Line = sample + '\t' + str(total_CPA_count) + '\t' + str(Uncharacterized_CPA_count) + '\t' + str(Kef_count) + '\t' + str(NHX_count) + '\t' + str(NhaA_count) + '\t' + str(NhaS5_count) + '\t' + str(CHX_count) + '\t' + str(GerN_count) + '\t' + str(CPA1_SL_count) + '\t' + str(NhaP_CPA1_count) + '\t' + str(SOD2_count) + '\t' + str(Undescribed_CPA1_count) + '\t' + str(Undescribed_CPA1_IDR_count) +'\n'
        print(Line)
        output.write(Line)
