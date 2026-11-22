#!/bin/bash -e
#SBATCH --job-name      BacB_hmmalign
#SBATCH --time          5:00:00
#SBATCH --mem           10GB
#SBATCH --cpus-per-task 1
#SBATCH --error         slurm_output/BacB_%A.err
#SBATCH --output        slurm_output/BacB_%A.out
module load HMMER/3.4-gompi-2025a
HMM=/home/mad149/HMM_databases/individual_hmms

module load Python

Seq_CPA=/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/retrieved_from_contigs/CPA_sequences_vs_contigs_rerun.fasta

hmmalign  --amino --trim -o NR_CPA_sequences_GTDB226_bins_contigs_hmmaligned.sthk ${HMM}/PF00999.hmm ${Seq_CPA}
python parse_stockholm.py NR_CPA_sequences_GTDB226_bins_contigs_hmmaligned.sthk NR_CPA_sequences_contigs_hmmaligned_filtered.fasta 263
