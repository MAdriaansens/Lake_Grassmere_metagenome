#!/bin/bash -e
#SBATCH --job-name      Trimming_FastQC
#SBATCH --time          4:00:00
#SBATCH --mem           20GB
#SBATCH --cpus-per-task 4
#SBATCH --exclude=n[13-15]
#SBATCH --error         slurm_output/TrimmFastQC_%A-%a.err
#SBATCH --output        slurm_output/TrimmFastQC_%A-%a.out
#SBATCH --array         0-1
declare -a array=($(seq 0 16))

module load FastQC/0.12.1-Java-11

MAG_Path=/scratch/projects/sbs/project/grassmere_metagenomic_Adriaansens
Fastq1=/home/mad149/Metagenome_grassmere/Fastq_1
cd ${Fastq1}
fastqc ${MAG_Path}/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_sample_${array[$SLURM_ARRAY_TASK_ID]}_R1.fastq.gz ${MAG_Path}/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_sample_${array[$SLURM_ARRAY_TASK_ID]}_R2.fastq.gz

cd /home/mad149/Metagenome_grassmere/Trimm_2
Trimm2=/home/mad149/Metagenome_grassmere/Trimm_2

module load Trimmomatic/0.39-Java-17
trimmomatic PE -threads 4 -phred33 -trimlog Illumina_Nextera_adapter.faa \
               ${MAG_Path}/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_sample_${array[$SLURM_ARRAY_TASK_ID]}_R1.fastq.gz ${MAG_Path}/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_sample_${array[$SLURM_ARRAY_TASK_ID]}_R2.fastq.gz \
               Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_sample_${array[$SLURM_ARRAY_TASK_ID]}_R1.qc.fastq.gz Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_sample_${array[$SLURM_ARRAY_TASK_ID]}_s1.fastq.gz Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_sample_${array[$SLURM_ARRAY_TASK_ID]}_R2.qc.fastq.gz Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_sample_${array[$SLURM_ARRAY_TASK_ID]}_s2.fastq.gz \
               ILLUMINACLIP:NexteraPE-PE.fa:1:25:7 SLIDINGWINDOW:4:30 MINLEN:80

fastqc Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_sample_${array[$SLURM_ARRAY_TASK_ID]}_R1.qc.fastq.gz Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_sample_${array[$SLURM_ARRAY_TASK_ID]}_R2.qc.fastq.gz
