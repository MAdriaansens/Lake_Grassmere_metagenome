#!/bin/bash -e
#SBATCH --job-name      Map_readsBBMap
#SBATCH --time          6:00:00
#SBATCH --mem           12GB
#SBATCH --cpus-per-task 1
#SBATCH --exclude=n[13-15]
#SBATCH --error         slurm_output_6BBmap/TrimmFastQC_%A-%a.err
#SBATCH --output        slurm_output_6BBmap/TrimmFastQC_%A-%a.out
#SBATCH --array         0-16
declare -a array=($(seq 0 16))

#for Metaspades/Vanilla spades
MAG_Path=/scratch/projects/sbs/project/grassmere_metagenomic_Adriaansens
cd /home/mad149/Metagenome_grassmere/Step4_filter_size/500b

module load seqtk/1.4-GCC-13.3.0

seqtk seq -L 500 /home/mad149/Metagenome_grassmere/Assembl_3/spades_assembly_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}/contigs.fasta > /home/mad149/Metagenome_grassmere/Step4_filter_size/500b/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_MetaSpades_500bsize_filtered_contigs.fna

seqtk seq -L 500 /home/mad149/Metagenome_grassmere/Assembl_3/spades_assembly_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}/scaffolds.fasta > /home/mad149/Metagenome_grassmere/Step4_filter_size/500b/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_MetaSpades_500bsize_filtered_scaffolds.fna


cd /home/mad149/Metagenome_grassmere/Step6_map_reads

mkdir Map_reads_scaffold_500b_VanillaSpades_${array[$SLURM_ARRAY_TASK_ID]}

cd Map_reads_scaffold_500b_VanillaSpades_${array[$SLURM_ARRAY_TASK_ID]}

module load BBMap/39.19-GCC-12.3.0

bbmap.sh ref=/home/mad149/Metagenome_grassmere/Step4_filter_size/500b/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_MetaSpades_500bsize_filtered_scaffolds.fna 

bbmap.sh minid=0.98 in=${MAG_Path}/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_sample_${array[$SLURM_ARRAY_TASK_ID]}_R1.fastq.gz in2=${MAG_Path}/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_sample_${array[$SLURM_ARRAY_TASK_ID]}_R2.fastq.gz out=mapped_reads_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_scaffold.sam


mkdir /home/mad149/Metagenome_grassmere/Step6_map_reads/Map_reads_contigs_vanillaSpades_500b_${array[$SLURM_ARRAY_TASK_ID]}

cd /home/mad149/Metagenome_grassmere/Step6_map_reads/Map_reads_contigs_vanillaSpades_500b_${array[$SLURM_ARRAY_TASK_ID]}
bbmap.sh ref=/home/mad149/Metagenome_grassmere/Step4_filter_size/500b/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_MetaSpades_500bsize_filtered_contigs.fna

bbmap.sh minid=0.98 in=${MAG_Path}/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_sample_${array[$SLURM_ARRAY_TASK_ID]}_R1.fastq.gz in2=${MAG_Path}/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_sample_${array[$SLURM_ARRAY_TASK_ID]}_R2.fastq.gz out=mapped_reads_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_contig.sam
