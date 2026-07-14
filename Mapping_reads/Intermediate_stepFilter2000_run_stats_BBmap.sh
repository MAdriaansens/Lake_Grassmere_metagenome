#!/bin/bash -e
#SBATCH --job-name      BBMap
#SBATCH --time          2:00:00
#SBATCH --mem           2GB
#SBATCH --cpus-per-task 1
#SBATCH --exclude=n[13-15]
#SBATCH --error         slurm_output_BBmap/TrimmFastQC_%A-%a.err
#SBATCH --output        slurm_output_BBmap/TrimmFastQC_%A-%a.out

#size filtering
module load seqtk/1.4-GCC-13.3.0
seqtk seq -L 2000 /home/mad149/Metagenome_grassmere/Assembl_3/Meta_spades_vanilla/spades_assembly_vanilla_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}/contigs.fasta > Step4_filter_size/2kb/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_vanilla_Spades_2Kbsize_filtered_contig.fna
seqtk seq -L 2000 /home/mad149/Metagenome_grassmere/Assembl_3/Meta_spades_vanilla/spades_assembly_vanilla_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}/scaffolds.fasta > Step4_filter_size/2kb/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_vanilla_Spades_2Kbsize_filtered_scaffold.fna

seqtk seq -L 2000 /home/mad149/Metagenome_grassmere/Assembl_3/Meta_spades_isolate/spades_assembly_isolate_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}/contigs.fasta > Step4_filter_size/2kb/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_isolate_Spades_2Kbsize_filtered_contig.fna
seqtk seq -L 2000 /home/mad149/Metagenome_grassmere/Assembl_3/Meta_spades_isolate/spades_assembly_isolate_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}/scaffolds.fasta > Step4_filter_size/2kb/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_isolate_Spades_2Kbsize_filtered_scaffold.fna

seqtk seq -L 2000 /home/mad149/Metagenome_grassmere/Assembl_3/Meta_spades_careful/spades_assembly_careful_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}/contigs.fasta > Step4_filter_size/2kb/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_careful_Spades_2Kbsize_filtered_contig.fna
seqtk seq -L 2000 /home/mad149/Metagenome_grassmere/Assembl_3/Meta_spades_careful/spades_assembly_careful_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}/scaffolds.fasta > Step4_filter_size/2kb/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_careful_Spades_2Kbsize_filtered_scaffold.fna

seqtk seq -L 2000 Metagenome_grassmere/Assembl_3/Megahit/Megahit_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}/final.contigs.fa > Step4_filter_size/2kb/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_MegaHIT_2Kbsize_filtered_scaffold.fna

module load BBMap/39.19-GCC-12.3.0

#do statistics using BBMap
stats.sh in=Step4_filter_size/2kb/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_isolate_Spades_2Kbsize_filtered_contig.fna 2>&1 > Step5_BBMap/Z37TGN${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_MetaSpades_size_2kfiltered_BBmap_contig.txt
stats.sh in=Step4_filter_size/2kb/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_isolate_Spades_2Kbsize_filtered_contig.fna 2>&1 > Step5_BBMap/Z37TGN${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_MetaSpades_size_2kfiltered_BBmap_contig.txt

stats.sh in=Step4_filter_size/2kb/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_careful_Spades_2Kbsize_filtered_scaffold.fna 2>&1 > Step5_BBMap/Z37TGN${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_MetaSpades_size_2kfiltered_BBmap_scaffold.txt
stats.sh in=Step4_filter_size/2kb/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_careful_Spades_2Kbsize_filtered_scaffold.fna 2>&1 > Step5_BBMap/Z37TGN${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_MetaSpades_size_2kfiltered_BBmap_scaffold.txt

stats.sh in=Step4_filter_size/2kb/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_vanilla_Spades_2Kbsize_filtered_scaffold.fna 2>&1 > Step5_BBMap/Z37TGN${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_MetaSpades_size_2kfiltered_BBmap_scaffold.txt
stats.sh in=Step4_filter_size/2kb/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_vanilla_Spades_2Kbsize_filtered_scaffold.fna 2>&1 > Step5_BBMap/Z37TGN${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_MetaSpades_size_2kfiltered_BBmap_scaffold.txt

stats.sh in=Step4_filter_size/2kb/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_MegaHIT_2Kbsize_filtered_scaffold.fna 2>&1 > Step5_BBMap/Z37TGN${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_MetaSpades_size_2kfiltered_MegaHit_contig.txt
