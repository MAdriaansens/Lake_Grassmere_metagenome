#!/bin/bash -e
#SBATCH --job-name      IMap_reads
#SBATCH --time          2:00:00
#SBATCH --mem           6GB
#SBATCH --cpus-per-task 15
#SBATCH --exclude=n[13-15]
#SBATCH --error         slurm_output_6BBmap/Isolate_%A-%a.err
#SBATCH --output        slurm_output_6BBmap/Isolate_%A-%a.out
#SBATCH --array         0-1
declare -a array=('10')

MAG_Path=/scratch/projects/sbs/project/grassmere_metagenomic_Adriaansens/data
cd /home/mad149/Metagenome_grassmere/Step4_filter_size/500b

module load seqtk/1.4-GCC-13.3.0

seqtk seq -L 500 Assembl_3/Megahit/Megahit_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}/final.contigs.fa > /home/mad149/Metagenome_grassmere/Step4_filter_size/500b/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_MegaHit_500bsize_filtered_contigs.fna



module load SAMtools/1.21-GCC-13.3.0

cd /home/mad149/Metagenome_grassmere/Step6_map_reads


mkdir /home/mad149/Metagenome_grassmere/Step6_map_reads/Map_reads_contigs_MegaHit_500b_${array[$SLURM_ARRAY_TASK_ID]}

cd /home/mad149/Metagenome_grassmere/Step6_map_reads/Map_reads_contigs_MegaHit_500b_${array[$SLURM_ARRAY_TASK_ID]}
bbmap.sh threads=$SLURM_CPUS_PER_TASK ref=/home/mad149/Metagenome_grassmere/Step4_filter_size/500b/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_TrimmomaticJuly7_MegaHit_500bsize_filtered_contigs.fna

bbmap.sh threads=$SLURM_CPUS_PER_TASK minid=0.98 in=${MAG_Path}/YPQMX3_1_rerun_sample_10_10_R1.fastq.gz in2=${MAG_Path}/YPQMX3_1_rerun_sample_10_10_R2.fastq.gz  out=mapped_reads_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_contig.sam

samtools view -H mapped_reads_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_contig.sam | grep "^@SQ" | sed 's/^@SQ\t//' | cut -f 1,2 | sed 's/SN://g; s/LN://g' | awk '$2 > 2000' > all_contigs_MegaHit${array[$SLURM_ARRAY_TASK_ID]}_greater_2000.txt

samtools view -L all_contigs_MegaHit${array[$SLURM_ARRAY_TASK_ID]}_greater_2000.txt -h mapped_reads_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_contig.sam > mapped_reads_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_contig_filtered2000MegaHit.sam
