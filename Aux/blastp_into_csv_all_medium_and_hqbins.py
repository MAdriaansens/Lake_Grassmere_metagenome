
listentry=[]
count=0
with open('All_mags_medium_to_hq.txt', 'r') as p:
    for line in p.readlines():
        if line in listentry:
            print(line)
        else:
            listentry.append(line)
print(len(listentry))
import glob

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



with open('blastp_output_before_dRep_july29.tsv', 'w') as p:
    header = 'Bin_name' + '\t' + 'Binning' + '\t' + 'Assembly' + '\t' + 'Sample_number' + '\t' + 'DEIK-ratio' + '\t' + 'RpS2_count' + '\t' + 'RpL4_count' + '\t' + 'MIP_count' + '\t' + 'ClcA_count' + '\t' + \
        'MscS_count' + '\t' + 'MscL_count' + '\t' + 'OpuAC_count' + '\t' + 'Na_ala_count' + '\t' + 'CorA_count' + '\t' + 'Na_Ca_count' + '\t' + 'BCCT_count' + '\t' + 'MgtE_count' + '\t' + 'EctC_count' + \
        '\t' + 'MnhE_count' + '\t' + 'Trehalose_PPase_count' + '\t' + 'TrkH_count' + '\t' + 'Kup_count' + '\t' + 'Hppase_count' + '\t' + 'NhaB_count' + '\t' + 'NhaC_count' + '\t' + 'NhaD_count' + '\t' + 'Kdp_count' + \
        '\t' + 'MtrA_count' + '\t' + 'AApermease_count' + '\t' + 'BranchedchainAA_transp_count' + '\t' + 'TreT_count' + '\t' + 'NqrA_count' + '\t' + 'KimA_count' + '\t' + 'Betain_ald_dehyd_count' + '\t' \
        + 'Uncharacterized_CPA_count' + '\t' + 'Kef_count' + '\t' + 'NHX_count' + '\t' + 'NhaA_count' + '\t' + 'NhaS5_count' + '\t' + 'CHX_count' + '\t' + 'GerN_count' + '\t' + 'CPA1_SL_count' + '\t' + 'NhaP_CPA1_count' + '\t' + 'SOD2_count' + '\t' + 'Undescribed_CPA1_count' + '\t' +'UndProkarya_CPA1_IDR_count' + '\n'
    
    p.write(header)
    for BlastP in glob.glob('/home/mad149/Metagenome_grassmere/Diamond_blastp/*'):
        Bin_name = BlastP.split('/')[-1].split('_blastp')[0]
        Binning=Bin_name.split('_')[0]
        Assembly = Bin_name.split('_')[1]
        
        Sample_number = Bin_name.split('_')[-1].split('.')[0]
        if 'coassembly' in Bin_name:
            Sample_number = 'CoAssembly_of_{}'.format(Sample_number)
        with open(BlastP, 'r') as output:
            sequence = ''
            DEIK_ratio=0
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
    
            for line in output:
                Protein= (line.split('\t')[1].split('tein:')[-1])
                if Protein == 'Ribosomal_S2':
                    RpS2_count = RpS2_count + 1
                    sequence = sequence +(line.split('\t')[-1])
                elif Protein == 'Ribosomal_L4':
                    RpL4_count = RpL4_count + 1
                    sequence = sequence +(line.split('\t')[-1])
                elif Protein == 'MS_channel_2nd':
                    MscS_count =MscS_count + 1
                elif Protein == 'MscL':
                    MscL_count =MscL_count + 1
                elif Protein == 'CorA':
                    CorA_count =CorA_count + 1
                elif Protein == 'Na_Ala_symp':
                    Na_ala_count =Na_ala_count + 1
                elif Protein == 'Voltage_CLC':
                    ClcA_count = ClcA_count + 1
                elif Protein == 'BCCT':
                    BCCT_count = BCCT_count + 1
                elif Protein == 'MIP':
                    MIP_count = MIP_count + 1
                elif Protein == 'Na_Ca_ex':
                    Na_Ca_count = Na_Ca_count + 1
                elif Protein == 'MgtE':
                    MgtE_count = MgtE_count + 1
                elif Protein == 'MNHE':
                    MnhE_count = MnhE_count + 1
                elif Protein == 'Trehalose_PPase':
                    Trehalose_PPase_count = Trehalose_PPase_count + 1
                elif Protein == 'TrkH':
                    TrkH_count = TrkH_count + 1
                elif Protein == 'K_trans':
                    Kup_count = Kup_count + 1
                elif Protein == 'H_PPase':
                    Hppase_count = Hppase_count + 1
                elif Protein == 'PF06450':
                    NhaB_count = NhaB_count + 1
                elif Protein == 'PF03553':
                    NhaC_count = NhaC_count + 1
                elif Protein == 'PF03600':
                    NhaD_count = NhaD_count + 1
                elif Protein == 'KdpA':
                    Kdp_count = Kdp_count + 1
                elif Protein == 'OpuAC':
                    OpuAC_count = OpuAC_count + 1
                elif Protein == 'MtrA':
                    MtrA_count = MtrA_count + 1
                elif Protein == 'Branch_AA_trans':
                    BranchedchainAA_transp_count = BranchedchainAA_transp_count + 1
                elif Protein == 'Ectoine_synth':
                    EctC_count = EctC_count + 1
                elif Protein == 'AA_permease_2':
                    AApermease_count = AApermease_count + 1
                elif Protein == 'TreT_GT1':
                    TreT_count = TreT_count + 1
                elif Protein == 'NQRA_2nd':
                     NqrA_count = NqrA_count + 1
                elif Protein == 'PTHR47704.orig.30.pir':
                     KimA_count = KimA_count + 1
                elif Protein == 'BADH':
                     Betain_ald_dehyd_count = Betain_ald_dehyd_count  + 1
                elif Protein== 'CPA1':
                    NHX_count = NHX_count + 1
                elif Protein == 'NhaA':
                    NhaA_count = NhaA_count + 1
                elif Protein == 'NhaS5':
                    NhaS5_count = NhaS5_count + 1
                elif Protein == 'NhaPCPA1':
                    NhaP_CPA1_count= NhaP_CPA1_count + 1
                elif Protein == 'Undescribed_CPA1':
                    Undescribed_CPA1_count= Undescribed_CPA1_count + 1
                elif Protein == 'CHX':
                    CHX_count = CHX_count + 1
                elif Protein == 'SOD2':
                    SOD2_count = SOD2_count + 1
                elif Protein == 'GerN':
                    GerN_count = GerN_count + 1
                elif Protein == 'CPA1_SL':
                    CPA1_SL_count = CPA1_SL_count + 1
                elif Protein == 'UndProkaryaCPA1IDK':
                    Undescribed_CPA1_IDR_count = Undescribed_CPA1_IDR_count + 1
                elif Protein =='Uncharacterized':
                    Uncharacterized_CPA_count = Uncharacterized_CPA_count + 1
                elif Protein =='Kef':
                    Kef_count = Kef_count + 1
                else:
                    if 'NhaB' == (IT_dict[Protein]):
                        NhaB_count = NhaB_count + 1
    
                    elif 'NhaC' == (IT_dict[Protein]):
                        NhaC_count = NhaC_count + 1
    
                    elif 'NhaD' == (IT_dict[Protein]):
                        NhaD_count = NhaD_count + 1
        
        DEIK_ratio = ((sequence.count('D') + sequence.count('E')+1)/(sequence.count('I') + sequence.count('K')+1))
        if DEIK_ratio == 1:
            DEIK_ratio = 'NA'
        Line = Bin_name + '\t' + Binning + '\t' + Assembly + '\t' + Sample_number + '\t' + str(DEIK_ratio) + '\t' + str(RpS2_count) + '\t' + str(RpL4_count) + '\t' + str(MIP_count) + '\t' + str(ClcA_count) + '\t' + \
            str(MscS_count) + '\t' + str(MscL_count) + '\t' + str(OpuAC_count) + '\t' + str(Na_ala_count) + '\t' + str(CorA_count) + '\t' + str(Na_Ca_count) + '\t' + str(BCCT_count) + '\t' + str(MgtE_count) + '\t' + str(EctC_count) + \
            '\t' + str(MnhE_count) + '\t' + str(Trehalose_PPase_count) + '\t' + str(TrkH_count) + '\t' + str(Kup_count) + '\t' + str(Hppase_count) + '\t' + str(NhaB_count) + '\t' + str(NhaC_count) + '\t' + str(NhaD_count ) + '\t' + str(Kdp_count) + \
            '\t' + str(MtrA_count) + '\t' + str(AApermease_count) + '\t' + str(BranchedchainAA_transp_count) + '\t' + str(TreT_count) + '\t' + str(NqrA_count) + '\t' + str(KimA_count) + '\t' + str(Betain_ald_dehyd_count) + \
            '\t' + str(Uncharacterized_CPA_count) + '\t' + str(Kef_count) + '\t' + str(NHX_count) + '\t' + str(NhaA_count) + '\t' + str(NhaS5_count) + '\t' + str(CHX_count) + '\t' + str(GerN_count) + '\t' + str(CPA1_SL_count) + '\t' + str(NhaP_CPA1_count) + '\t' + str(SOD2_count) + '\t' + str(Undescribed_CPA1_count) + '\t' + str(Undescribed_CPA1_IDR_count) + '\n'
        p.write(Line)
