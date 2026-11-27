from Bio.SeqUtils.ProtParam import ProteinAnalysis as PA
import glob
import statistics
from Bio import SeqIO


Ip_dictionary = {}
for entry in glob.glob('/home/mad149/Metagenome_grassmere/HQ_MG_mags/*faa'):
    iep_list=[]
    for record in SeqIO.parse('{}'.format(entry), 'fasta'):
        protein=PA(record.seq)
        iep_list.append(protein.isoelectric_point())

    MAG_id = entry.split('/')[-1].split('.fa')[0]
    
    median = statistics.median(iep_list)
    average= statistics.mean(iep_list)
    Ip_dictionary[MAG_id] = [median, average]

id_salinity = {'1': 32.3, '2': 32.3, '3': 30.2, '4':30.2, '5':30.8, '6':30.8, '7':22.3, '8':22.3, '9':17.2, '10':17.2, '11':11.2, '12':11.2, '13':5.8, '14':3.4, '15':31.3, '16':0}
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


from Bio import SeqIO
import glob
hq_mq_list = []
with open('/home/mad149/Metagenome_grassmere/HQ_MQ_mags.txt', 'r') as mags:
    for line in mags:
        hq_mq_list.append(line.split('\n')[0])
with open('/home/mad149/Metagenome_grassmere/HQ_MG_mags/counted_blastp_vs_MAGs.tsv', 'w') as output:

    header = 'MAG\tSalinity\tIp_median\tIp_average\tDEIK_Ratio\tRpS2_count\tRpL4_count\tMIP_count\tClcA_count\tMscS_count\tMscL_count\tOpuAC_count\tNa_ala_count\tCorA_count\tNa_Ca_count\tBCCT_count\tMgtE_count\tEctC_count\tMnhE_count\tTrehalose_PPase_count\tTrkH_count\tKup_count\tHppase_count\tNhaB_count\tNhaC_count\tNhaD_count\tKdp_count\tMtrA_count\tTreT_count\tNqrA_count\tKimA_count\ttotal_CPA_count\tUncharacterized_CPA_count\tKef_count\tNHX_count\tNhaA_count\tNhaS5_count\tCHX_count\tGerN_count\tCPA1_SL_count\tNhaP_CPA1_count\tSOD2_count\tUndescribed_CPA1_count\tUndProkarya_CPA1_IDR_count\tKef_subclade44514\tKef_subclade29950\n'

    output.write(header)



    for mag in hq_mq_list:
    
        # ------------------------------------------------
        # INITIALISE COUNTERS ONCE PER MAG
        # ------------------------------------------------
    
    
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
        GerN_count = 0
        CPA1_SL_count = 0
        Kef_subclade29950 = 0
        Kef_subclade44514= 0
        BCCT_count = 0
        MIP_count = 0
        RpS2_count = 0
        RpL4_count = 0
        ClcA_count = 0
        MscS_count = 0
        MscL_count = 0
        Na_ala_count = 0
        CorA_count = 0
        Na_Ca_count = 0
        MgtE_count = 0
        MnhE_count = 0
        Trehalose_PPase_count = 0
        TrkH_count = 0
        Hppase_count = 0
        NhaB_count = 0
        NhaC_count = 0
        NhaD_count = 0
        Kup_count = 0
        Kdp_count = 0
        OpuAC_count = 0
        TreT_count = 0
        EctC_count = 0
        MtrA_count = 0
        NqrA_count = 0
        KimA_count = 0
        Sequence = 'DEIK'
        
        for entry in glob.glob('/home/mad149/Metagenome_grassmere/HQ_MG_mags/homology_search/{}_Diamond_output/*.fasta'.format(mag)):
            for record in SeqIO.parse(entry, 'fasta'):
                protein_type = record.id.split('ein:')[1]
        
                if protein_type == 'Ribosomal_S2':
                    RpS2_count += 1
                    Sequence += str(record.seq)
        
                elif protein_type == 'Ribosomal_L4':
                    RpL4_count += 1
                    Sequence += str(record.seq)
        
                elif protein_type == 'MS_channel_2nd':
                    MscS_count += 1
        
                elif protein_type == 'MscL':
                    MscL_count += 1
        
                elif protein_type == 'CorA':
                    CorA_count += 1
        
                elif protein_type == 'Na_Ala_symp':
                    Na_ala_count += 1
        
                elif protein_type == 'Voltage_CLC':
                    ClcA_count += 1
        
                elif protein_type == 'BCCT':
                    BCCT_count += 1
        
                elif protein_type == 'MIP':
                    MIP_count += 1
        
                elif protein_type == 'Na_Ca_ex':
                    Na_Ca_count += 1
        
                elif protein_type == 'MgtE':
                    MgtE_count += 1
        
                elif protein_type == 'MNHE':
                    MnhE_count += 1
        
                elif protein_type == 'Trehalose_PPase':
                    Trehalose_PPase_count += 1
        
                elif protein_type == 'TrkH':
                    TrkH_count += 1
        
                elif protein_type == 'K_trans':
                    Kup_count += 1
        
                elif protein_type == 'H_PPase':
                    Hppase_count += 1
        
                elif protein_type == 'PF06450':
                    NhaB_count += 1
        
                elif protein_type == 'PF03553':
                    NhaC_count += 1
        
                elif protein_type == 'PF03600':
                    NhaD_count += 1
        
                elif protein_type == 'KdpA':
                    Kdp_count += 1
        
                elif protein_type == 'OpuAC':
                    OpuAC_count += 1
        
                elif protein_type == 'MtrA':
                    MtrA_count += 1
        
                elif protein_type == 'Ectoine_synth':
                    EctC_count += 1
        
                elif protein_type == 'TreT_GT1':
                    TreT_count += 1
        
                elif protein_type == 'NQRA_2nd':
                    NqrA_count += 1
        
                elif protein_type == 'PTHR47704.orig.30.pir':
                    KimA_count += 1
        
                elif protein_type == 'NHX':
                    NHX_count += 1
        
                elif protein_type == 'NhaA':
                    NhaA_count += 1
        
                elif protein_type == 'NhaS5':
                    NhaS5_count += 1
        
                elif protein_type == 'NhaPCPA1':
                    NhaP_CPA1_count += 1
        
                elif protein_type == 'Undescribed_CPA1':
                    Undescribed_CPA1_count += 1
        
                elif protein_type == 'CHX':
                    CHX_count += 1
        
                elif protein_type == 'SOD2':
                    SOD2_count += 1
        
                elif protein_type == 'GerN':
                    GerN_count += 1
        
                elif protein_type == 'CPA1_SL':
                    CPA1_SL_count += 1
        
                elif protein_type == 'UndProkaryaCPA1IDR':
                    Undescribed_CPA1_IDR_count += 1
        
                elif protein_type == 'Uncharacterized':
                    Uncharacterized_CPA_count += 1
                elif protein_type == 'Kef':
                    Kef_count +=1
                    Kef_hit_id = (record.id.split('_tax')[0].split(':')[-1])
                    Kef_subclade = (Kef_dictionary[Kef_hit_id])
                    if Kef_subclade == '29950':
                        Kef_subclade29950+=1
                    elif Kef_subclade == '44514':
                        Kef_subclade44514+=1

            Ip_median = Ip_dictionary[mag][0]
            Ip_average = Ip_dictionary[mag][1]
            Salinity=id_salinity[mag.split('_')[-1].split('.')[0]]
            if RpS2_count == 0 and RpL4_count == 0:
                    DEIK_ratio = 'NaN'
            else:
                DEIK_ratio =  str((Sequence.count('D') + Sequence.count('E'))/(Sequence.count('I') + Sequence.count('K')))
        Line = (
                mag + '\t' + 
                str(Salinity) + '\t' + 
                str(Ip_median) + '\t' +
                str(Ip_average) + '\t' + 
                DEIK_ratio + '\t' + 
                str(RpS2_count) + '\t' +
                str(RpL4_count) + '\t' +
                str(MIP_count) + '\t' +
                str(ClcA_count) + '\t' +
                str(MscS_count) + '\t' +
                str(MscL_count) + '\t' +
                str(OpuAC_count) + '\t' +
                str(Na_ala_count) + '\t' +
                str(CorA_count) + '\t' +
                str(Na_Ca_count) + '\t' +
                str(BCCT_count) + '\t' +
                str(MgtE_count) + '\t' +
                str(EctC_count) + '\t' +
                str(MnhE_count) + '\t' +
                str(Trehalose_PPase_count) + '\t' +
                str(TrkH_count) + '\t' +
                str(Kup_count) + '\t' +
                str(Hppase_count) + '\t' +
                str(NhaB_count) + '\t' +
                str(NhaC_count) + '\t' +
                str(NhaD_count) + '\t' +
                str(Kdp_count) + '\t' +
                str(MtrA_count) + '\t' +
                str(TreT_count) + '\t' +
                str(NqrA_count) + '\t' +
                str(KimA_count) + '\t' +
                str(total_CPA_count) + '\t' +
                str(Uncharacterized_CPA_count) + '\t' +
                str(Kef_count) + '\t' +
                str(NHX_count) + '\t' +
                str(NhaA_count) + '\t' +
                str(NhaS5_count) + '\t' +
                str(CHX_count) + '\t' +
                str(GerN_count) + '\t' +
                str(CPA1_SL_count) + '\t' +
                str(NhaP_CPA1_count) + '\t' +
                str(SOD2_count) + '\t' +
                str(Undescribed_CPA1_count) + '\t' +
                str(Undescribed_CPA1_IDR_count) + '\t' +
                str(Kef_subclade44514) + '\t' +
                str(Kef_subclade29950) + '\n'
            )
        
        output.write(Line)
