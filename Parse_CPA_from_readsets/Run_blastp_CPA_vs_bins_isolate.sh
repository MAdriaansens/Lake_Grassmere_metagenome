#!/bin/bash -e
#SBATCH --job-name      Diamond_vs_bins
#SBATCH --time          8:00:00
#SBATCH --mem           10GB
#SBATCH --cpus-per-task 5
#SBATCH --exclude=n[13-15]
#SBATCH --error         slurm_output_Diamond/TrimmFastQC_%A-%a.err
#SBATCH --output        slurm_output_Diamond/TrimmFastQC_%A-%a.out
#SBATCH --array         0-68%68
declare -a array=($(seq 0 68))

module load DIAMOND/2.2.4-GCC-14.3.0

DB=/home/mad149/chapter_meta_analysis/Protein/fl/All_CPA_types_added_detail_uncharacterized.fasta

outdir=Diamond/Diamond_blastp/Bins

ID_LIST=/home/mad149/Metagenome_grassmere/Best_assembly_bins.txt
Line_number=${array[$SLURM_ARRAY_TASK_ID]}
ID=$(head -n ${array[$SLURM_ARRAY_TASK_ID]} ${ID_LIST} | tail -n1) 

echo ${ID}
sample=$(echo "$ID" | awk -F '\\.|spades_' '{print $2}')
echo ${sample}
file=(bins/Isolate/MetaBat/MetaBat_Isolate_spades_${sample}/MetaBat_Isolate_spades_Sample${sample}_checkm2/protein_files/${ID}.fa.faa )
echo ${file}

diamond blastp --query $file -d ${DB} --max-target-seqs 1 --evalue 0.00001 --threads $SLURM_CPUS_PER_TASK --outfmt 6 qseqid sseqid slen evalue bitscore qseq --out ${outdir}/${ID}_vs_all_CPA.tsv 
