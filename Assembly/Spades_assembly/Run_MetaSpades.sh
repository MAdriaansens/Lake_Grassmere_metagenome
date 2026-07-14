#!/bin/bash -e
#SBATCH --job-name      MetaSpades
#SBATCH --time          24:00:00
#SBATCH --mem           60GB
#SBATCH --cpus-per-task 16
#SBATCH --exclude=n[13-15]
#SBATCH --error         slurm_output/Spades_%A-%a.err
#SBATCH --output        slurm_output/Spades_%A-%a.out
#SBATCH --array         0-12
declare -a array=($(seq 1 12))

cd Assembl_3

module load SPAdes/4.1.0-GCC-13.3.0
Trim=/home/mad149/Metagenome_grassmere/Trimm_2

spades.py --meta -k 33,55,77,99,121 -t $SLURM_CPUS_PER_TASK \
          -1 ${Trim}/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_sample_${array[$SLURM_ARRAY_TASK_ID]}_R1.qc.fastq.gz -2 ${Trim}/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_sample_${array[$SLURM_ARRAY_TASK_ID]}_R2.qc.fastq.gz \
          -o spades_assembly_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}/
