from Bio import SeqIO
import glob
hq_mq_list = []
with open('/home/mad149/Metagenome_grassmere/HQ_MQ_mags.txt', 'r') as mags:
    for line in mags:
        hq_mq_list.append(line.split('\n')[0])
with open('/home/mad149/Metagenome_grassmere/HQ_MG_mags/counted_blastp_vs_MAGs.tsv', 'w') as output:

    header = 'MAG\tDEIK_Ratio\tRpS2_count\tRpL4_count\tMIP_count\tClcA_count\tMscS_count\tMscL_count\tOpuAC_count\tNa_ala_count\tCorA_count\tNa_Ca_count\tBCCT_count\tMgtE_count\tEctC_count\tMnhE_count\tTrehalose_PPase_count\tTrkH_count\tKup_count\tHppase_count\tNhaB_count\tNhaC_count\tNhaD_count\tKdp_count\tMtrA_count\tAApermease_count\tBranchedchainAA_transp_count\tTreT_count\tNqrA_count\tKimA_count\tBetain_ald_dehyd_count\ttotal_CPA_count\tUncharacterized_CPA_count\tKef_count\tCPA1_count\tNhaA_count\tNhaS5_count\tCHX_count\tGerN_count\tCPA1_SL_count\tNhaP_CPA1_count\tSOD2_count\tUndescribed_CPA1_count\tUndProkarya_CPA1_IDK_count\tKef_subclade44514\tKef_subclade29950\tKef_subclade42457\tKef_subclade44199\tKef_subclade42947\tKef_subclade42415\tKef_subclade44013\tKef_subclade44600\tKef_subclade43808\tKef_subclade43312\tKef_subclade43225\tKef_subclade43377\tKef_subclade43531\tKef_subclade43598\tKef_subclade43720\tKef_subclade44121\tKef_subclade43954\tKef_subclade43914\tKef_subclade42396\tKef_subclade44582\tKef_subclade44712\tMissing_kef\tKef_group34971\tKef_group35454\tKef_group37918\tKef_group38119\tKef_group38142\tmissing_kef_group\tMjNah1_count\n'

    output.write(header)



    for mag in hq_mq_list:
    
        # ------------------------------------------------
        # INITIALISE COUNTERS ONCE PER MAG
        # ------------------------------------------------
    
    
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
        CPA1_SL_count = 0
    
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
        AApermease_count = 0
        NqrA_count = 0
        Betain_ald_dehyd_count = 0
        KimA_count = 0
        
        
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
                    CPA1_count += 1
        
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
        
                elif protein_type == 'UndProkaryaCPA1IDK':
                    Undescribed_CPA1_IDK_count += 1
        
                elif protein_type == 'Uncharacterized':
                    Uncharacterized_CPA_count += 1
            DEIK_ratio =  str((Sequence.count('D') + Sequence.count('E'))/(Sequence.count('I') + Sequence.count('K')))
            Line = (
                mag + '\t' + DEIK_ratio + '\t' +
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
                str(AApermease_count) + '\t' +
                str(BranchedchainAA_transp_count) + '\t' +
                str(TreT_count) + '\t' +
                str(NqrA_count) + '\t' +
                str(KimA_count) + '\t' +
                str(Betain_ald_dehyd_count) + '\t' +
                str(total_CPA_count) + '\t' +
                str(Uncharacterized_CPA_count) + '\t' +
                str(Kef_count) + '\t' +
                str(CPA1_count) + '\t' +
                str(NhaA_count) + '\t' +
                str(NhaS5_count) + '\t' +
                str(CHX_count) + '\t' +
                str(GerN_count) + '\t' +
                str(CPA1_SL_count) + '\t' +
                str(NhaP_CPA1_count) + '\t' +
                str(SOD2_count) + '\t' +
                str(Undescribed_CPA1_count) + '\t' +
                str(Undescribed_CPA1_IDK_count) + '\n'
            )
        
        output.write(Line)
