#!/bin/bash -e
#SBATCH --job-name      Trimming_FastQC
#SBATCH --time          24:00:00
#SBATCH --mem           140GB
#SBATCH --cpus-per-task 16
#SBATCH --exclude=n[13-15]
#SBATCH --error         slurm_output/TrimmFastQC_%A-%a.err
#SBATCH --output        slurm_output/TrimmFastQC_%A-%a.out

cd Assembl_3

module load SPAdes/4.1.0-GCC-13.3.0
Trim=/home/mad149/Metagenome_grassmere/Trimm_2
#what we do here is instead of running an array we run one single read set
spades.py --meta -k 33,55,77,99,121 -t $SLURM_CPUS_PER_TASK \
          -1 ${Trim}/Z37TGN_13_sample_13_R1.qc.fastq.gz -2 ${Trim}/Z37TGN_13_sample_13_R2.qc.fastq.gz \
          -o spades_assembly_Z37TGN_13/
