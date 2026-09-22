#!/bin/bash -e
#SBATCH --job-name      XBLAST
#SBATCH --time          12:00:00
#SBATCH --mem           20GB
#SBATCH --cpus-per-task 5
#SBATCH --error         slurm_xblastoutput2/Bacscan2_%A-%a.err
#SBATCH --output        slurm_xblastoutput2/Bacscan2_%A-%a.out
#SBATCH --array         0-16
declare -a array=($(seq 0 16))

METADIR=/scratch/projects/sbs/project/grassmere_metagenomic_Adriaansens/data
module load DIAMOND/2.1.8-GCC-12.3.0

cd /home/mad149/Metagenome_grassmere/output_xblast_NRCPA
DB=/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/NR_CPA_sequences_GTDB226_bins_contigs.fasta

#echo "running R1"
#diamond blastx --threads ${SLURM_CPUS_PER_TASK} --evalue 0.00001  --max-target-seqs 1  --outfmt 6 qseqid sseqid slen evalue bitscore qseq qseq_translated --db ${DB} -q ${METADIR}/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_sample_${array[$SLURM_ARRAY_TASK_ID]}_R2.fastq.gz --out Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_sample_${array[$SLURM_ARRAY_TASK_ID]}_R1_vs_NRCPA_DB.m8

#echo "running R2"
#diamond blastx --threads ${SLURM_CPUS_PER_TASK} --evalue 0.00001 --max-target-seqs 1 --outfmt 6 qseqid sseqid slen evalue bitscore qseq qseq_translated --db ${DB} -q ${METADIR}/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_sample_${array[$SLURM_ARRAY_TASK_ID]}_R2.fastq.gz --out Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_sample_${array[$SLURM_ARRAY_TASK_ID]}_R2_vs_NRCPA_DB.m8
DB=/home/mad149/Metagenome_grassmere/CPA_full_tree_70seq_reps.fasta

echo "running R1"
diamond blastx --threads ${SLURM_CPUS_PER_TASK} --evalue 0.00001  --max-target-seqs 1  --outfmt 6 qseqid sseqid slen evalue bitscore qseq qseq_translated --db ${DB} -q ${METADIR}/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_sample_${array[$SLURM_ARRAY_TASK_ID]}_R2.fastq.gz --out Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_sample_${array[$SLURM_ARRAY_TASK_ID]}_R1_vs_treeCPA_DB.m8

echo "running R2"
diamond blastx --threads ${SLURM_CPUS_PER_TASK} --evalue 0.00001 --max-target-seqs 1 --outfmt 6 qseqid sseqid slen evalue bitscore qseq qseq_translated --db ${DB} -q ${METADIR}/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_sample_${array[$SLURM_ARRAY_TASK_ID]}_R2.fastq.gz --out Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_sample_${array[$SLURM_ARRAY_TASK_ID]}_R2_vs_treeCPA_DB.m8

