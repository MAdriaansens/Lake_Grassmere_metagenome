#!/bin/bash -e
#SBATCH --job-name      Read_mapping
#SBATCH --time          1:00:00
#SBATCH --mem           30GB
#SBATCH --cpus-per-task 12
#SBATCH --exclude=n[13-15]
#SBATCH --error         slurm_output_CheckM2/TrimmFastQC_%A-%a.err
#SBATCH --output        slurm_output_CheckM2/TrimmFastQC_%A-%a.out
#SBATCH --array         0-2%3
declare -a array=($(seq 67 69))
module load Bowtie2/2.5.4-GCC-13.3.0 SAMtools/1.21-GCC-13.3.0

bin_dir=/home/mad149/Metagenome_grassmere/HQ_MG_mags
bin_cov_dir=/home/mad149/Metagenome_grassmere/Read_mapping_to_MAGs

ID_LIST=/home/mad149/Metagenome_grassmere/HQ_MQ_mags.txt
Line_number=${array[$SLURM_ARRAY_TASK_ID]}

Output=/home/mad149/Metagenome_grassmere/HQ_MG_mags/homology_search
MAG_ID=$(head -n ${array[$SLURM_ARRAY_TASK_ID]} ${ID_LIST} | tail -n1)


#step 1 build Bowtie2 index

mkdir -p ${bin_cov_dir}/bw_index_${MAG_ID}
bowtie2-build ${bin_dir}/${MAG_ID}.fa.fna ${bin_cov_dir}/bw_index_${MAG_ID}/${MAG_ID}_bw


#input file name metabat2_isolate_spades_12.27
temp="${MAG_ID##*_}"
sample="${temp%%.*}"

Trimmed_reads=/home/mad149/Metagenome_grassmere/Trimm_2

mkdir -p ${bin_cov_dir}/bw_index_${MAG_ID}/Mapping

#Map reads bowtie, since the reads are 150bp we use --score-min L,0,-0.18 to get around 97
#4/150*100 = 2.6%. 
bowtie2 --end-to-end --score-min L,0,-0.18 --threads $SLURM_CPUS_PER_TASK --sensitive \
            -x ${bin_cov_dir}/bw_index_${MAG_ID}/${MAG_ID}_bw \
            -1 ${Trimmed_reads}/Z37TGN_${sample}_sample_${sample}_R1.qc.fastq.gz \
            -2 ${Trimmed_reads}/Z37TGN_${sample}_sample_${sample}_R2.qc.fastq.gz \
            -S ${bin_cov_dir}/bw_index_${MAG_ID}/Mapping/${MAG_ID}_vs_Sample_${sample}.sam
            
samtools sort -@ $SLURM_CPUS_PER_TASK \
            -o ${bin_cov_dir}/bw_index_${MAG_ID}/Mapping/${MAG_ID}_vs_Sample_${sample}.bam ${bin_cov_dir}/bw_index_${MAG_ID}/Mapping/${MAG_ID}_vs_Sample_${sample}.sam

samtools index ${bin_cov_dir}/bw_index_${MAG_ID}/Mapping/${MAG_ID}_vs_Sample_${sample}.bam
samtools idxstats ${bin_cov_dir}/bw_index_${MAG_ID}/Mapping/${MAG_ID}_vs_Sample_${sample}.bam > ${bin_cov_dir}/bw_index_${MAG_ID}/Mapping/${MAG_ID}_vs_Sample_${sample}_idxstats.tsv
MODULEPATH=$MODULEPATH:/scratch/projects/sbs-apps/modulefiles

module --ignore_cache load metabat/2.17
jgi_summarize_bam_contig_depths --outputDepth ${bin_cov_dir}/bw_index_${MAG_ID}/Mapping/${MAG_ID}_vs_Sample_${sample}_cov_table.txt ${bin_cov_dir}/bw_index_${MAG_ID}/Mapping/${MAG_ID}_vs_Sample_${sample}.bam

#for f in ~*.fa.fna; do     name=$(basename "$f" .fa.fna);     len=$(awk '!/^>/ {seqlen+=length($0)} END {print seqlen}' "$f");     echo -e "${name}\t${len}"; done > HQ_MQ_mag_lengths.txt
