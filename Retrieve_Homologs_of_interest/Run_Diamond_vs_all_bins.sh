#!/bin/bash -e
#SBATCH --job-name      Hmmalign
#SBATCH --time          4:00:00
#SBATCH --mem           2GB
#SBATCH --cpus-per-task 1
#SBATCH --exclude=n[13-15]
#SBATCH --error         slurm_output/TrimmFastQC_%A-%a.err
#SBATCH --output        slurm_output/TrimmFastQC_%A-%a.out

TrkH=MetaBat_isolate_postDrep_TrkHs.fasta
CPA=MetaBat_isolate_postDrep_CPAs.fasta
HPPase=MetaBat_isolate_postDrep_Hpase.fasta
HMMDB=/home/mad149/HMM_databases/individual_hmms


#${HMMDB}/PF02386_TrkH.hmm
#${HMMDB}/PF03030_HPPAse.hmm
#${HMMDB}/PF00999.hmm


#hmmalign --trim --amino -o HMMalign/Hppase_Hmmaligned.sthk /home/mad149/HMM_databases/individual_hmms/PF03030_HPPAse.hmm MetaBat_isolate_postDrep_Hpase.fasta  
#hmmalign --trim --amino -o HMMalign/TrkH_Hmmaligned.sthk /home/mad149/HMM_databases/individual_hmms/PF02386_TrkH.hmm MetaBat_isolate_postDrep_TrkHs.fasta 
#hmmalign --trim --amino -o HMMalign/CPA_Hmmaligned.sthk /home/mad149/HMM_databases/individual_hmms/PF00999.hmm MetaBat_isolate_postDrep_CPAs.fasta 


python parse_stockholm.py HMMalign/CPA_Hmmaligned.sthk HMMalign/PF00999_CPA_vsCPA_HQMQ_bins_hmmaligned 263

python parse_stockholm.py HMMalign/TrkH_Hmmaligned.sthk HMMalign/PF02386_TrkH_vsTrkH_HQMQ_bins_hmmaligned 351

python parse_stockholm.py HMMalign/Hppase_Hmmaligned.sthk HMMalign/PF03030_HPPase_vsHPPase_HQMQ_bins_hmmaligned 453
