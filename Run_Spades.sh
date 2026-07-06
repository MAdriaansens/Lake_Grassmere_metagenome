#!/bin/bash -e
#SBATCH --job-name      spades_assembly
#SBATCH --time          01:00:00
#SBATCH --mem           10G
#SBATCH --cpus-per-task 12
#SBATCH --error         Spades_output2/Bacscan2_%A-%a.err
#SBATCH --output        Spades_output2/Bacscan2_%A-%a.out

# Load modules
R1=/home/mad149/Metagenome_grassmere/subset_run/trimmomatic/Z37TGN_10_sample_10_R1_subset8000_bbduktrimmed.qc.fastq.gz 
R2=/home/mad149/Metagenome_grassmere/subset_run/trimmomatic/Z37TGN_10_sample_10_R2_subset8000.qc.fastq.gz

# Working directory
cd /home/mad149/Metagenome_grassmere/subset_run/assembly_metaspades
#module purge

#module load scikit-learn/1.5.2-gfbf-2024a
#module load scikit-learn/1.6.1-gfbf-2024a

echo $MODULEPATH 
module load SPAdes/4.1.0-GCC-13.3.0

# Run SPAdes
spades.py -h
spades.py --meta -k 33,55,77,99,121 -t $SLURM_CPUS_PER_TASK \
          -1 ${R1} -2 ${R2} \
          -o spades_assembly/
