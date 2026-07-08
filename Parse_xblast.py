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

import os
SRR_list='/home/mad149/Metagenome_grassmere/output_xblast'
from Bio import SeqIO

NhaBfile ='/home/mad149/chapter_meta_analysis/Protein/fl/NhaB_fl.fasta'
NhaCfile ='/home/mad149/chapter_meta_analysis/Protein/fl/NhaC_fl.fasta'
NhaDfile ='/home/mad149/chapter_meta_analysis/Protein/fl/NhaD_fl.fasta'
IT_dict = {}

for record in SeqIO.parse(NhaBfile, 'fasta'):
    IT_dict[record.id] = 'NhaB'
for record in SeqIO.parse(NhaCfile, 'fasta'):
    IT_dict[record.id] = 'NhaC'
for record in SeqIO.parse(NhaDfile, 'fasta'):
    IT_dict[record.id] = 'NhaD'
    


SRR_entries = []
for SRR_id in os.listdir('/home/mad149/Metagenome_grassmere/output_xblast'):
    if 'm8' in SRR_id:
        SRR_entries.append(SRR_id.split('_sample')[0])
    

print(len(SRR_entries))
ID = list(set(SRR_entries))
print('ids done {}'.format(len(ID)))


    
def return_dictionary_diamond_blast(Directory, SRR_id):
    SRR_directory = {}
    SRR_parse_list = []
    SRR_parse_list.append(SRR_id + '_sample_{}_R1_vs_Salt_DB.m8'.format(SRR_id.split('_')[1]))
    SRR_parse_list.append(SRR_id + '_sample_{}_R2_vs_Salt_DB.m8'.format(SRR_id.split('_')[1]))
    for SRR in SRR_parse_list:
        if os.path.exists('{}/{}'.format(Directory, SRR)):
           with open('{}/{}'.format(Directory, SRR), 'r') as M8:
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
        else:
            print(Directory, SRR)
            pass
    return(SRR_directory)



import sys
count  = 0
with open('/home/mad149/Metagenome_grassmere/xblast_output_5Juli_LGM_Incl_extrafocus_Kef.tsv', 'w') as output:
    header = 'SRA_id' + '\t' + 'RpS2_count' + '\t' + 'RpL4_count' + '\t' + 'DEIK_ratio' + '\t' + 'RK_ratio' + '\t' + 'MIP_count' + '\t' + 'ClcA_count' + '\t' + \
    'MscS_count' + '\t' + 'MscL_count' + '\t' + 'OpuAC_count' + '\t' + 'Na_ala_count' + '\t' + 'CorA_count' + '\t' + 'Na_Ca_count' + '\t' + 'BCCT_count' + '\t' + 'MgtE_count' + '\t' + 'EctC_count' + \
    '\t' + 'MnhE_count' + '\t' + 'Trehalose_PPase_count' + '\t' + 'TrkH_count' + '\t' + 'Kup_count' + '\t' + 'Hppase_count' + '\t' + 'NhaB_count' + '\t' + 'NhaC_count' + '\t' + 'NhaD_count' + '\t' + 'Kdp_count' + \
    '\t' + 'MtrA_count' + '\t' + 'AApermease_count' + '\t' + 'BranchedchainAA_transp_count' + '\t' + 'TreT_count' + '\t' + 'NqrA_count' + '\t' + 'KimA_count' + '\t' + 'Betain_ald_dehyd_count' + '\t' \
    + 'total_CPA_count' + '\t' + 'Uncharacterized_CPA_count' + '\t' + 'Kef_count' + '\t' + 'CPA1_count' + '\t' + 'NhaA_count' + '\t' + 'NhaS5_count' + '\t' + 'CHX_count' + '\t' + 'GerN_count' + '\t' + 'CPA1_SL_count' + '\t' + 'NhaP_CPA1_count' + '\t' + 'SOD2_count' + '\t' + 'Undescribed_CPA1_count' + '\t' +'UndProkarya_CPA1_IDK_count' + '\t' +'Kef_subclade44514' + '\t' +'Kef_subclade29950' + '\t' +'Kef_subclade42457' + '\t' +'Kef_subclade44199' + '\t' +'Kef_subclade42947' + '\t' +'Kef_subclade42415' + '\t' +'Kef_subclade44013' + '\t' +'Kef_subclade44600'+ '\t' +'Kef_subclade43808' + '\t' +'Kef_subclade43312' + '\t' +'Kef_subclade43225' + '\t' +'Kef_subclade43377' + '\t' +'Kef_subclade43531' + '\t' +'Kef_subclade43598' +  '\t' +'Kef_subclade43720' + '\t' +'Kef_subclade44121' + '\t' +'Kef_subclade43954' + '\t' +'Kef_subclade43914' + '\t' +'Kef_subclade42396' + '\t' +'Kef_subclade44582' + '\t' +'Kef_subclade44712' + '\t' +'Missing_kef' + '\t' + 'Kef_group34971' + '\t' + 'Kef_group35454' + '\t' + 'Kef_group37918' + '\t' + 'Kef_group38119' + '\t' + 'Kef_group38142' + '\t' + 'missing_kef_group' + '\t' + 'MjNah1_count'+'\n'
    output.write(header)
    for SRR_id in ID:
        print(SRR_id)
        xblast_output_dictionary = {}
        xblast_output_dictionary = dict(return_dictionary_diamond_blast(SRR_list, SRR_id))

        SRA_id = SRR_id
        #CPAs
        total_CPA_count = 0
        CPA1_count = 0
        Kef_count = 0
        NhaA_count = 0
        Uncharacterized_CPA_count = 0
        NhaS5_count = 0
        CHX_count = 0
        Undescribed_CPA1_count = 0
        SOD2_count = 0
        NhaP_CPA1_count = 0
        Undescribed_CPA1_IDK_count = 0
        GerN_count = 0
        CPA1_SL_count =0
        BCCT_count =0
        MIP_count = 0
        RpS2_count = 0
        RpL4_count = 0
        ClcA_count =0
        MscS_count =0
        MscL_count =0
        Na_ala_count = 0
        CorA_count = 0
        Na_Ca_count = 0
        MgtE_count = 0
        MnhE_count =0
        Trehalose_PPase_count = 0
        TrkH_count  = 0
        Hppase_count =0
        NhaB_count = 0
        NhaC_count = 0
        NhaD_count =0
        Kup_count = 0
        Kdp_count = 0
        OpuAC_count = 0
        TreT_count =0
        EctC_count = 0
        MtrA_count = 0
        AApermease_count = 0
        NqrA_count = 0
        Betain_ald_dehyd_count = 0
        KimA_count = 0
        BranchedchainAA_transp_count = 0
        Sequence=''
        Kef_subclade29950=0
        Kef_subclade42457=0
        Kef_subclade44199=0
        Kef_subclade42947=0
        Kef_subclade42415=0
        Kef_subclade44013=0
        Kef_subclade44600=0
        Kef_subclade43808=0
        Kef_subclade44514=0
        Kef_subclade43312=0
        Kef_subclade43225=0
        Kef_subclade43377=0
        Kef_subclade43531=0
        Kef_subclade43598=0
        Kef_subclade43720=0
        Kef_subclade44121=0
        Kef_subclade43954=0
        Kef_subclade43914=0
        Kef_subclade42396=0
        Kef_subclade44582=0
        Kef_subclade44712=0
        Kef_group34971=0
        Kef_group35454= 0
        Kef_group37918=0
        MjNah1_count = 0
        Kef_group38119=0
        Kef_group38142=0
        missing_kef_group=0
        Missing_kef = 0
        for key in xblast_output_dictionary.keys():
            if 'rotein:' in xblast_output_dictionary[key][0]:
                if xblast_output_dictionary[key][0].split('protein:')[-1] == 'Ribosomal_S2':
                    RpS2_count = RpS2_count + 1
                    Sequence = Sequence + xblast_output_dictionary[key][-1]
                elif xblast_output_dictionary[key][0].split('protein:')[-1] == 'Ribosomal_L4':
                    RpL4_count = RpL4_count + 1
                    Sequence = Sequence + xblast_output_dictionary[key][-1]
                elif xblast_output_dictionary[key][0].split('protein:')[-1] == 'MS_channel_2nd':
                    MscS_count =MscS_count + 1
                elif xblast_output_dictionary[key][0].split('protein:')[-1] == 'MscL':
                    MscL_count =MscL_count + 1
                elif xblast_output_dictionary[key][0].split('protein:')[-1] == 'CorA':
                    CorA_count =CorA_count + 1
                elif xblast_output_dictionary[key][0].split('protein:')[-1] == 'Na_Ala_symp':
                    Na_ala_count =Na_ala_count + 1
                elif xblast_output_dictionary[key][0].split('protein:')[-1] == 'Voltage_CLC':
                    ClcA_count = ClcA_count + 1
                elif xblast_output_dictionary[key][0].split('protein:')[-1] == 'BCCT':
                    BCCT_count = BCCT_count + 1
                elif xblast_output_dictionary[key][0].split('protein:')[-1] == 'MIP':
                    MIP_count = MIP_count + 1
                elif xblast_output_dictionary[key][0].split('protein:')[-1] == 'Na_Ca_ex':
                    Na_Ca_count = Na_Ca_count + 1
                elif xblast_output_dictionary[key][0].split('protein:')[-1] == 'MgtE':
                    MgtE_count = MgtE_count + 1
                elif xblast_output_dictionary[key][0].split('protein:')[-1] == 'MNHE':
                    MnhE_count = MnhE_count + 1
                elif xblast_output_dictionary[key][0].split('protein:')[-1] == 'Trehalose_PPase':
                    Trehalose_PPase_count = Trehalose_PPase_count + 1
                elif xblast_output_dictionary[key][0].split('protein:')[-1] == 'TrkH':
                    TrkH_count = TrkH_count + 1
                elif xblast_output_dictionary[key][0].split('protein:')[-1] == 'K_trans':
                     Kup_count = Kup_count + 1
                elif xblast_output_dictionary[key][0].split('protein:')[-1] == 'H_PPase':
                     Hppase_count = Hppase_count + 1
                elif xblast_output_dictionary[key][0].split('protein:')[-1] == 'PF06450':
                    NhaB_count = NhaB_count + 1
                elif xblast_output_dictionary[key][0].split('protein:')[-1] == 'PF03553':
                    NhaC_count = NhaC_count + 1
                elif xblast_output_dictionary[key][0].split('protein:')[-1] == 'PF03600':
                    NhaD_count = NhaD_count + 1
                elif xblast_output_dictionary[key][0].split('protein:')[-1] == 'KdpA':
                    Kdp_count = Kdp_count + 1
                elif xblast_output_dictionary[key][0].split('protein:')[-1] == 'OpuAC':
                    OpuAC_count = OpuAC_count + 1
                elif xblast_output_dictionary[key][0].split('protein:')[-1] == 'MtrA':
                    MtrA_count = MtrA_count + 1
                elif xblast_output_dictionary[key][0].split('protein:')[-1] == 'Branch_AA_trans':
                    BranchedchainAA_transp_count = BranchedchainAA_transp_count + 1
                elif xblast_output_dictionary[key][0].split('protein:')[-1] == 'Ectoine_synth':
                    EctC_count = EctC_count + 1
                elif xblast_output_dictionary[key][0].split('protein:')[-1] == 'AA_permease_2':
                    AApermease_count = AApermease_count + 1
                elif xblast_output_dictionary[key][0].split('protein:')[-1] == 'TreT_GT1':
                    TreT_count = TreT_count + 1
                elif xblast_output_dictionary[key][0].split('protein:')[-1] == 'NQRA_2nd':
                    NqrA_count = NqrA_count + 1
                elif xblast_output_dictionary[key][0].split('protein:')[-1] == 'PTHR47704.orig.30.pir':
                    KimA_count = KimA_count + 1
                elif xblast_output_dictionary[key][0].split('protein:')[-1] == 'BADH':
                    Betain_ald_dehyd_count = Betain_ald_dehyd_count  + 1
                else:
                    if 'Protein:' in xblast_output_dictionary[key][0]:

                        total_CPA_count = total_CPA_count + 1

                        if xblast_output_dictionary[key][0].split('Protein:')[-1]  == 'Kef':
                            Kef_count = Kef_count + 1
                            Kef_hit_id = (xblast_output_dictionary[key][0].split('_tax')[0])
                            Kef_subclade = (Kef_dictionary[Kef_hit_id])
                            Kef_group = (Kef_groupdict[Kef_hit_id])
                            if Kef_subclade == '29950':
                                Kef_subclade29950+=1
                                if Kef_group == '34971':
                                    Kef_group34971+=1
                                elif Kef_group == '35454':
                                    Kef_group35454+=1
                                elif Kef_group == '37918':
                                    Kef_group37918+=1
                                elif Kef_group == '38119':
                                    Kef_group38119+=1
                                elif Kef_group == '38142':
                                    Kef_group38142+=1
                                else:
                                    missing_kef_group +=1
                            elif Kef_subclade == '42457':
                                Kef_subclade42457+=1
                            elif Kef_subclade == '44199':
                                Kef_subclade44199+=1
                            elif Kef_subclade == '42947':
                                Kef_subclade42947+=1
                            elif Kef_subclade == '42415':
                                Kef_subclade42415+=1
                            elif Kef_subclade == '44013':
                                Kef_subclade44013+=1
                            elif Kef_subclade == '44600':
                                Kef_subclade44600+=1
                            elif Kef_subclade == '43808':
                                Kef_subclade43808+=1
                            elif Kef_subclade == '44514':
                                Kef_subclade44514+=1
                            elif Kef_subclade == '43312':
                                Kef_subclade43312+=1
                            elif Kef_subclade == '43225':
                                Kef_subclade43225+=1
                            elif Kef_subclade == '43377':
                                Kef_subclade43377+=1
                            elif Kef_subclade == '43531':
                                Kef_subclade43531+=1
                            elif Kef_subclade == '43598':
                                Kef_subclade43598+=1
                            elif Kef_subclade == '43720':
                                Kef_subclade43720+=1
                            elif Kef_subclade == '44121':
                                Kef_subclade44121+=1
                            elif Kef_subclade == '43954':
                                Kef_subclade43954+=1
                            elif Kef_subclade == '43914':
                                Kef_subclade43914+=1
                            elif Kef_subclade == '42396':
                                Kef_subclade42396+=1
                            elif Kef_subclade == '44582':
                                Kef_subclade44582+=1
                            elif Kef_subclade == '44712':
                                Kef_subclade44712+=1
                            else:
                                Missing_kef +=1
        
                        elif xblast_output_dictionary[key][0].split('Protein:')[-1]== 'CPA1':
                            CPA1_count = CPA1_count + 1
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
                        elif xblast_output_dictionary[key][0].split('Protein:')[-1] == 'UndProkaryaCPA1IDK':
                            Undescribed_CPA1_IDK_count = Undescribed_CPA1_IDK_count + 1
                        elif xblast_output_dictionary[key][0].split('Protein:')[-1] =='Uncharacterized':
                            Uncharacterized_CPA_count = Uncharacterized_CPA_count + 1
                            if key in Mj_dictionary.keys():
                                MjNah1_count +=1
                                
            else:
                id_hit = xblast_output_dictionary[key][0]
                if 'NhaB' == (IT_dict[id_hit]):
                    NhaB_count = NhaB_count + 1

                elif 'NhaC' == (IT_dict[id_hit]):
                    NhaC_count = NhaC_count + 1

                elif 'NhaD' == (IT_dict[id_hit]):
                    NhaD_count = NhaD_count + 1
                

                    #print('count:', 'count:')
        DEIK_ratio =  str((Sequence.count('D') + Sequence.count('E'))/(Sequence.count('I') + Sequence.count('K')))
        RK_ratio =  str(Sequence.count('R')/Sequence.count('K'))
        count = count + 1
        Line = SRA_id + '\t' + str(RpS2_count) + '\t' + str(RpL4_count) + '\t' + str(DEIK_ratio) + '\t' + str(RK_ratio) + '\t' + str(MIP_count) + '\t' + str(ClcA_count) + '\t' + \
        str(MscS_count) + '\t' + str(MscL_count) + '\t' + str(OpuAC_count) + '\t' + str(Na_ala_count) + '\t' + str(CorA_count) + '\t' + str(Na_Ca_count) + '\t' + str(BCCT_count) + '\t' + str(MgtE_count) + '\t' + str(EctC_count) + \
        '\t' + str(MnhE_count) + '\t' + str(Trehalose_PPase_count) + '\t' + str(TrkH_count) + '\t' + str(Kup_count) + '\t' + str(Hppase_count) + '\t' + str(NhaB_count) + '\t' + str(NhaC_count) + '\t' + str(NhaD_count ) + '\t' + str(Kdp_count) + \
        '\t' + str(MtrA_count) + '\t' + str(AApermease_count) + '\t' + str(BranchedchainAA_transp_count) + '\t' + str(TreT_count) + '\t' + str(NqrA_count) + '\t' + str(KimA_count) + '\t' + str(Betain_ald_dehyd_count) + '\t' \
        + str(total_CPA_count) + '\t' + str(Uncharacterized_CPA_count) + '\t' + str(Kef_count) + '\t' + str(CPA1_count) + '\t' + str(NhaA_count) + '\t' + str(NhaS5_count) + '\t' + str(CHX_count) + '\t' + str(GerN_count) + '\t' + str(CPA1_SL_count) + '\t' + str(NhaP_CPA1_count) + '\t' + str(SOD2_count) + '\t' + str(Undescribed_CPA1_count) + '\t' + str(Undescribed_CPA1_IDK_count) + '\t' + str(Kef_subclade44514) + '\t' + str(Kef_subclade29950) + '\t' + str(Kef_subclade42457) + '\t' + str(Kef_subclade44199) + '\t' + str(Kef_subclade42947) + '\t' + str(Kef_subclade42415) + '\t' + str(Kef_subclade44013) + '\t' + str(Kef_subclade44600)+ '\t' + str(Kef_subclade43808) + '\t' + str(Kef_subclade43312) + '\t' + str(Kef_subclade43225) + '\t' + str(Kef_subclade43377) + '\t' + str(Kef_subclade43531) + '\t' + str(Kef_subclade43598) +  '\t' + str(Kef_subclade43720) + '\t' + str(Kef_subclade44121) + '\t' + str(Kef_subclade43954) + '\t' + str(Kef_subclade43914) + '\t' + str(Kef_subclade42396) + '\t' + str(Kef_subclade44582) + '\t' + str(Kef_subclade44712) + '\t' + str(Missing_kef) + str(Kef_group34971) + '\t' + str(Kef_group35454) + '\t' + str(Kef_group37918) + '\t' + str(Kef_group38119) + '\t' + str(Kef_group38142) + '\t' + str(missing_kef_group) + '\t' + str(MjNah1_count) +'\n'
        output.write(Line)
        print('{}/16'.format(count))
print('finished')
