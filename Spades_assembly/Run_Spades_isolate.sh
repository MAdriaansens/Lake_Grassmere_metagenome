#!/bin/bash -e
#SBATCH --job-name      IsoSpades
#SBATCH --time          10:00:00
#SBATCH --mem           60GB
#SBATCH --cpus-per-task 18
#SBATCH --exclude=n[13-15]
#SBATCH --error         slurm_spades_output/IsoSpades_%A-%a.err
#SBATCH --output        slurm_spades_output/IsoSpades_%A-%a.out
#SBATCH --array         0-16
declare -a array=($(seq 0 16 ))

cd Assembl_3/Meta_spades_isolate

module load SPAdes/4.1.0-GCC-13.3.0
Trim=/home/mad149/Metagenome_grassmere/Trimm_2

spades.py --isolate --only-assembler -1 ${Trim}/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_sample_${array[$SLURM_ARRAY_TASK_ID]}_R1.qc.fastq.gz -2 ${Trim}/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_sample_${array[$SLURM_ARRAY_TASK_ID]}_R2.qc.fastq.gz -o spades_assembly_careful_isolate_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]} -t $SLURM_CPUS_PER_TASK -k 25,55,65,75   
          
