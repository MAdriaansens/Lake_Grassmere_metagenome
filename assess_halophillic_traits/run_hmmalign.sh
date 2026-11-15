#!/bin/bash -e
#SBATCH --job-name      BacB_hmmalign
#SBATCH --time          10:00:00
#SBATCH --mem           5GB
#SBATCH --cpus-per-task 1
#SBATCH --error         slurm_output/BacB_%A-%a.err
#SBATCH --output        slurm_output/BacB_%A-%a.out
#SBATCH --array         0-69%69

declare -a array=($(seq 0 69))

ID_LIST=/home/mad149/Metagenome_grassmere/HQ_MQ_mags.txt
Line_number=${array[$SLURM_ARRAY_TASK_ID]}

Output=/home/mad149/Metagenome_grassmere/HQ_MG_mags/homology_search
SRR_ID=$(head -n ${array[$SLURM_ARRAY_TASK_ID]} ${ID_LIST} | tail -n1)
echo "${SRR_ID}"
Infile=/home/mad149/Metagenome_grassmere/HQ_MG_mags/homology_search/${SRR_ID}_Diamond_output/${SRR_ID}_blastp_protein_Database_protein_seq.faa

HMMalign=/home/mad149/Metagenome_grassmere/HQ_MG_mags/homology_search/${SRR_ID}_Diamond_output
HMMdir=/home/mad149/HMM_databases/individual_hmms
module load HMMER/3.4-gompi-2023a

hmmalign  --amino --trim -o ${HMMalign}/PF00230hmm_MIPvs_${SRR_ID}_hmmaligned.sthk ${HMMdir}/PF00230_MIP.hmm ${Infile}

hmmalign  --amino --trim -o ${HMMalign}/PF00318_Rps2hmmvs_${SRR_ID}_hmmaligned.sthk ${HMMdir}/PF00318_Rps2.hmm ${Infile}

hmmalign  --amino --trim -o ${HMMalign}/PF00573_Rpl4hmmvs_${SRR_ID}_hmmaligned.sthk ${HMMdir}/PF00573_Rpl4.hmm ${Infile}

hmmalign  --amino --trim -o ${HMMalign}/PF00654_ClcAhmmvs_${SRR_ID}_hmmaligned.sthk ${HMMdir}/PF00654_ClcA.hmm ${Infile}

hmmalign  --amino --trim -o ${HMMalign}/PF00924_MscShmmvs_${SRR_ID}_hmmaligned.sthk ${HMMdir}/PF00924_MscS.hmm ${Infile}

hmmalign  --amino --trim -o ${HMMalign}/PF01235_Na_Ala_symhmmvs_${SRR_ID}_hmmaligned.sthk ${HMMdir}/PF01235_Na_Ala_sym.hmm ${Infile}

hmmalign  --amino --trim -o ${HMMalign}/PF01544_CorA.hmmvs_${SRR_ID}_hmmaligned.sthk ${HMMdir}/PF01544_CorA.hmm ${Infile}

hmmalign  --amino --trim -o ${HMMalign}/PF01699_Na_Ca_exhmmvs_${SRR_ID}_hmmaligned.sthk ${HMMdir}/PF01699_Na_Ca_ex.hmm ${Infile}

hmmalign  --amino --trim -o ${HMMalign}/PF01741_MscLhmmvs_${SRR_ID}_hmmaligned.sthk ${HMMdir}/PF01741_MscL.hmm ${Infile}

hmmalign  --amino --trim -o ${HMMalign}/PF01769_MgtEhmmvs_${SRR_ID}_hmmaligned.sthk ${HMMdir}/PF01769_MgtE.hmm ${Infile}

hmmalign  --amino --trim -o ${HMMalign}/PF01899_MnhE_ClcAhmmvs_${SRR_ID}_hmmaligned.sthk ${HMMdir}/PF01899_MnhE.hmm ${Infile}

hmmalign  --amino --trim -o ${HMMalign}/PF02028_BCCT_ClcAhmmvs_${SRR_ID}_hmmaligned.sthk ${HMMdir}/PF02028_BCCT.hmm ${Infile}

hmmalign  --amino --trim -o ${HMMalign}/PF02358_Trehalose_HPPashemmvs_${SRR_ID}_hmmaligned.sthk ${HMMdir}/PF02358_Trehalose_PPase.hmm ${Infile}

hmmalign  --amino --trim -o ${HMMalign}/PF02386_TrkHhmmvs_${SRR_ID}_hmmaligned.sthk ${HMMdir}/PF02386_TrkH.hmm ${Infile}

hmmalign  --amino --trim -o ${HMMalign}/PF02705_KUPhmmvs_${SRR_ID}_hmmaligned.sthk ${HMMdir}/PF02705_KUP.hmm ${Infile}

hmmalign  --amino --trim -o ${HMMalign}/PF03030_HPPAsehmmvs_${SRR_ID}_hmmaligned.sthk ${HMMdir}/PF03030_HPPAse.hmm ${Infile}

hmmalign  --amino --trim -o ${HMMalign}/PF03814_kdphmmvs_${SRR_ID}_hmmaligned.sthk ${HMMdir}/PF03814_kdp.hmm ${Infile}

hmmalign  --amino --trim -o ${HMMalign}/PF04069_OpuAChmmvs_${SRR_ID}_hmmaligned.sthk ${HMMdir}/PF04069_OpuAC.hmm ${Infile}

hmmalign  --amino --trim -o ${HMMalign}/PF04208_MtrAhmmvs_${SRR_ID}_hmmaligned.sthk ${HMMdir}/PF04208_MtrA.hmm ${Infile}

hmmalign  --amino --trim -o ${HMMalign}/PF06339_EctChmmvs_${SRR_ID}_hmmaligned.sthk ${HMMdir}/PF06339_EctC.hmm ${Infile}

hmmalign  --amino --trim -o ${HMMalign}/PF21269_TreThmmvs_${SRR_ID}_hmmaligned.sthk ${HMMdir}/PF21269_TreT.hmm ${Infile}

hmmalign  --amino --trim -o ${HMMalign}/PF24836_NQRAhmmvs_${SRR_ID}_hmmaligned.sthk ${HMMdir}/PF24836_NQRA.hmm ${Infile}

hmmalign  --amino --trim -o ${HMMalign}/PTHR47704_KimAhmmvs_${SRR_ID}_hmmaligned.sthk ${HMMdir}/PTHR47704_KimA.hmm ${Infile}

hmmalign  --amino --trim -o ${HMMalign}/CPA_PF00999_vs_${SRR_ID}_hmmaligned.sthk ${HMMdir}/PF00999.hmm ${Infile}

hmmalign  --amino --trim -o ${HMMalign}/NhaB_PF06450_vs_${SRR_ID}_hmmaligned.sthk /home/mad149/HMM_databases/individual_hmms/PF06450_NhaB.hmm ${Infile}

hmmalign  --amino --trim -o ${HMMalign}/NhaC_PF03553_vs_${SRR_ID}_hmmaligned.sthk ${HMMdir}/PF03553_NhaC.hmm ${Infile}

hmmalign  --amino --trim -o ${HMMalign}/NhaD_PF03600_vs_${SRR_ID}_hmmaligned.sthk ${HMMdir}/PF03600_NhaD.hmm ${Infile}
