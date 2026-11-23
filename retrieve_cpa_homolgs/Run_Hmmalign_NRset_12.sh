#!/bin/bash -e
#SBATCH --job-name      Hmmalign
#SBATCH --time          4:00:00
#SBATCH --mem           20GB
#SBATCH --cpus-per-task 1
#SBATCH --exclude=n[13-15]
#SBATCH --error         slurm_output/TrimmFastQC_%A-%a.err
#SBATCH --output        slurm_output/TrimmFastQC_%A-%a.out


HMMDB=/home/mad149/HMM_databases/individual_hmms


module load HMMER/3.4-gompi-2025a
hmmalign --trim --amino -o NR_CPA_sequences_Adriaansens_bins_contigs_hmmaligned.sthk /home/mad149/HMM_databases/individual_hmms/PF00999.hmm NR_CPA_sequences_Adriaansens_bins_contigs.fasta


python parse_stockholm.py NR_CPA_sequences_Adriaansens_bins_contigs_hmmaligned.sthk PF00999NR_CPA_sequences_Adriaansens_bins_contigs_hmmaligned_filtered.fasta 263
