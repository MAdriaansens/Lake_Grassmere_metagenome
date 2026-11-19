#!/bin/bash -e
#SBATCH --job-name      Diamond
#SBATCH --time          8:00:00
#SBATCH --mem           4GB
#SBATCH --cpus-per-task 10
#SBATCH --exclude=n[13-15]
#SBATCH --error         slurm_output_diamond/TrimmFastQC_%A-%a.err
#SBATCH --output        slurm_output_diamond/TrimmFastQC_%A-%a.out

module load DIAMOND/2.2.4-GCC-14.3.0

CPA=/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/Adriaansens_CPAs.fasta

diamond blastp --query Assembl_3/Meta_spades_isolate/Prodigal/contigs_${array[$SLURM_ARRAY_TASK_ID]}_Isolate_spades_translated_proteins.faa -d ${CPA} --max-target-seqs 1 --evalue 0.00001 --threads $SLURM_CPUS_PER_TASK --outfmt 6 qseqid sseqid slen evalue bitscore qseq --out Diamond/Diamond_blastp/Contigs/${array[$SLURM_ARRAY_TASK_ID]}_Metaspades_isolate_blastp_vs_protein_CPA.tsv 
