#!/bin/bash -e
#SBATCH --job-name      Hmmalign
#SBATCH --time          4:00:00
#SBATCH --mem           2GB
#SBATCH --cpus-per-task 1
#SBATCH --exclude=n[13-15]
#SBATCH --error         slurm_output/TrimmFastQC_%A-%a.err
#SBATCH --output        slurm_output/TrimmFastQC_%A-%a.out


HMMDB=/home/mad149/HMM_databases/individual_hmms


module load HMMER/3.4-gompi-2025a
hmmalign --trim --amino -o CPA_vs_HQMQ_bins_hmmaligned.sthk /home/mad149/HMM_databases/individual_hmms/PF00999.hmm CPA_sequences_vs_HQMQ_bins_rerun.fasta


python parse_stockholm.py CPA_vs_HQMQ_bins_hmmaligned.sthk PF00999_CPA_vsCPA_HQMQ_bins_hmmaligned_filtered.fasta 263
