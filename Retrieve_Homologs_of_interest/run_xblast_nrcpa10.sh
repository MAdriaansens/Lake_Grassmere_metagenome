#!/bin/bash -e
#SBATCH --job-name      XBLAST
#SBATCH --time          12:00:00
#SBATCH --mem           20GB
#SBATCH --cpus-per-task 15
#SBATCH --error         slurm_xblastoutput2/Bacscan2_%A-%a.err
#SBATCH --output        slurm_xblastoutput2/Bacscan2_%A-%a.out

DB=/home/mad149/Metagenome_grassmere/NR_CPA_sequences_GTDB226_bins_contigs_Diamond_db_Sept1.dmnd
METADIR=/scratch/projects/sbs/project/grassmere_metagenomic_Adriaansens
module load DIAMOND/2.1.8-GCC-12.3.0

cd /home/mad149/Metagenome_grassmere/output_xblast_NRCPA

echo "running R1"
diamond blastx --threads ${SLURM_CPUS_PER_TASK} --evalue 0.00001  --max-target-seqs 1  --outfmt 6 qseqid sseqid slen evalue bitscore qseq qseq_translated --db ${DB} -q ${METADIR}/YPQMX3_1_rerun_sample_10_10_R1.fastq.gz --out Z37TGN_10_sample_${array[$SLURM_ARRAY_TASK_ID]}_R1_vs_NRCPA_DB.m8

echo "running R2"
diamond blastx --threads ${SLURM_CPUS_PER_TASK} --evalue 0.00001 --max-target-seqs 1 --outfmt 6 qseqid sseqid slen evalue bitscore qseq qseq_translated --db ${DB} -q ${METADIR}/YPQMX3_1_rerun_sample_10_10_R2.fastq.gz --out Z37TGN_10_sample_${array[$SLURM_ARRAY_TASK_ID]}_R2_vs_NRCPA_DB.m8


