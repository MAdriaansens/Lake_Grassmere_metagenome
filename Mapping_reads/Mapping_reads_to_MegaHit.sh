#!/bin/bash -e
#SBATCH --job-name      BBMap
#SBATCH --time          48:00:00
#SBATCH --mem           60GB
#SBATCH --cpus-per-task 20
#SBATCH --exclude=n[13-15]
#SBATCH --error         slurm_output_BBmap/TrimmFastQC_%A-%a.err
#SBATCH --output        slurm_output_BBmap/TrimmFastQC_%A-%a.out
#SBATCH --array         0-15
declare -a array=($(seq 2 16))

MAG_Path=
module load seqtk/1.4-GCC-13.3.0
seqtk seq -L 500 Assembl_3/Megahit/Megahit_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}/final.contigs.fa > /home/mad149/Metagenome_grassmere/Step4_filter_size/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_MegaHit_500b_size_filtered.fna
mkdir Step6_map_reads/${array[$SLURM_ARRAY_TASK_ID]}

module load BBMap/39.19-GCC-12.3.0
module load SAMtools/1.21-GCC-13.3.0

for i in {1..16}
do
    cd /home/mad149/Metagenome_grassmere/Step6_map_reads/${array[$SLURM_ARRAY_TASK_ID]}
    mkdir ${array[$SLURM_ARRAY_TASK_ID]}_vs_$i
    #make ref
    cd /home/mad149/Metagenome_grassmere/Step6_map_reads/${array[$SLURM_ARRAY_TASK_ID]}/${array[$SLURM_ARRAY_TASK_ID]}_vs_$i
    bbmap.sh threads=$SLURM_CPUS_PER_TASK ref=/home/mad149/Metagenome_grassmere/Step4_filter_size/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_MegaHit_500b_size_filtered.fna
    bbmap.sh threads=$SLURM_CPUS_PER_TASK minid=0.98 in=/home/mad149/Metagenome_grassmere/Trimm_2/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_sample_${array[$SLURM_ARRAY_TASK_ID]}_R1.qc.fastq.gz in2=/home/mad149/Metagenome_grassmere/Trimm_2/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_sample_${array[$SLURM_ARRAY_TASK_ID]}_R2.qc.fastq.gz out=/home/mad149/Metagenome_grassmere/Step6_map_reads/${array[$SLURM_ARRAY_TASK_ID]}/${array[$SLURM_ARRAY_TASK_ID]}_vs_$i/mapped_reads_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_vs_${i}_MegaHit_scaffold.sam bamscript=sort_bam.sh
    sh sort_bam.sh
done
