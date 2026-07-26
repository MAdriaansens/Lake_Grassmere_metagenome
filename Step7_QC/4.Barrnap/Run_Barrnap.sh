#!/bin/bash -e
#SBATCH --job-name      barrnap
#SBATCH --time          48:00:00
#SBATCH --mem           100GB
#SBATCH --cpus-per-task 20
#SBATCH --exclude=n[13-15]
#SBATCH --error         slurm_output_barrnap/TrimmFastQC_%A-%a.err
#SBATCH --output        slurm_output_barrnap/TrimmFastQC_%A-%a.out

module load barrnap/0.9-gompi-2023a

for bin in bins/*/*/*/*.fna; do
    entry=$(basename "$bin" .fna)
    barrnap $bin --threads $SLURM_CPUS_PER_TASK --outseq barrnap/${entry}_rna_sequences.fasta
done
