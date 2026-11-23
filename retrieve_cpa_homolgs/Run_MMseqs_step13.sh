#!/bin/bash -e
#SBATCH --job-name      MMseqs
#SBATCH --time          8:00:00
#SBATCH --mem           30GB
#SBATCH --cpus-per-task 20
#SBATCH --exclude=n[13-15]
#SBATCH --error         slurm_output/TrimmFastQC_%A-%a.err
#SBATCH --output        slurm_output/TrimmFastQC_%A-%a.out

module load MMseqs2/14-7e284-gompi-2023a
NRCPA=/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/PF00999NR_CPA_sequences_Adriaansens_bins_contigs_hmmaligned_filtered.fasta
mmseqs easy-cluster  --min-seq-id 0.7 -c 0.0 ${NRCPA} PF00999NR_CPA_sequences_Adriaansens_bins_contigs_hmmaligned_filtered_clustered_70.fasta  temp
rm -r temp
