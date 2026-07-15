#!/bin/bash -e
#SBATCH --job-name      CMap_reads
#SBATCH --time          6:00:00
#SBATCH --mem           10GB
#SBATCH --cpus-per-task 15
#SBATCH --exclude=n[13-15]
#SBATCH --error         slurm_output_6BBmap/Carefull_%A-%a.err
#SBATCH --output        slurm_output_6BBmap/Carefull_%A-%a.out
#SBATCH --array         0-1
declare -a array=('10')

MAG_Path=/scratch/projects/sbs/project/grassmere_metagenomic_Adriaansens/data
cd /home/mad149/Metagenome_grassmere/Step4_filter_size/500b

module load seqtk/1.4-GCC-13.3.0


seqtk seq -L 500 /home/mad149/Metagenome_grassmere/Assembl_3/Meta_spades_careful/spades_assembly_careful_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}/scaffolds.fasta > /home/mad149/Metagenome_grassmere/Step4_filter_size/500b/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_CarefulSpades_500bsize_filtered_contigs.fna

seqtk seq -L 500 /home/mad149/Metagenome_grassmere/Assembl_3/Meta_spades_careful/spades_assembly_careful_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}/scaffolds.fasta > /home/mad149/Metagenome_grassmere/Step4_filter_size/500b/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_CarefulSpades_500bsize_filtered_scaffolds.fna

module load SAMtools/1.21-GCC-13.3.0
cd /home/mad149/Metagenome_grassmere/Step6_map_reads

mkdir Map_reads_scaffold_500b_CarefulSpades_${array[$SLURM_ARRAY_TASK_ID]}

cd Map_reads_scaffold_500b_CarefulSpades_${array[$SLURM_ARRAY_TASK_ID]}
module load BBMap/39.19-GCC-12.3.0

bbmap.sh threads=$SLURM_CPUS_PER_TASK ref=/home/mad149/Metagenome_grassmere/Step4_filter_size/500b/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_CarefulSpades_500bsize_filtered_scaffolds.fna 

bbmap.sh threads=$SLURM_CPUS_PER_TASK minid=0.98 in=${MAG_Path}/YPQMX3_1_rerun_sample_10_10_R1.fastq.gz in2=${MAG_Path}/YPQMX3_1_rerun_sample_10_10_R2.fastq.gz out=mapped_reads_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_scaffold.sam

samtools view -H mapped_reads_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_scaffold.sam | grep "^@SQ" | sed 's/^@SQ\t//' | cut -f 1,2 | sed 's/SN://g; s/LN://g' | awk '$2 > 2000' > all_scaffolds_Careful${array[$SLURM_ARRAY_TASK_ID]}_greater_2000.txt

samtools view -L all_scaffolds_Careful${array[$SLURM_ARRAY_TASK_ID]}_greater_2000.txt -h mapped_reads_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_scaffold.sam > mapped_reads_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_scaffold_filtered2000Careful.sam

mkdir /home/mad149/Metagenome_grassmere/Step6_map_reads/Map_reads_contigs_CarefulSpades_500b_${array[$SLURM_ARRAY_TASK_ID]}

cd /home/mad149/Metagenome_grassmere/Step6_map_reads/Map_reads_contigs_CarefulSpades_500b_${array[$SLURM_ARRAY_TASK_ID]}

bbmap.sh threads=$SLURM_CPUS_PER_TASK ref=/home/mad149/Metagenome_grassmere/Step4_filter_size/500b/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_CarefulSpades_500bsize_filtered_contigs.fna

bbmap.sh threads=$SLURM_CPUS_PER_TASK minid=0.98 in=${MAG_Path}/YPQMX3_1_rerun_sample_10_10_R1.fastq.gz in2=${MAG_Path}/YPQMX3_1_rerun_sample_10_10_R2.fastq.gz out=mapped_reads_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_contig.sam
samtools view -H mapped_reads_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_contig.sam | grep "^@SQ" | sed 's/^@SQ\t//' | cut -f 1,2 | sed 's/SN://g; s/LN://g' | awk '$2 > 2000' > all_contigs_Careful${array[$SLURM_ARRAY_TASK_ID]}_greater_2000.txt

samtools view -L all_contigs_Careful${array[$SLURM_ARRAY_TASK_ID]}_greater_2000.txt -h mapped_reads_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_contig.sam > mapped_reads_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_contig_filtered2000Careful.sam
