#!/bin/bash -e
#SBATCH --job-name      Diamond
#SBATCH --time          8:00:00
#SBATCH --mem           4GB
#SBATCH --cpus-per-task 10
#SBATCH --exclude=n[13-15]
#SBATCH --error         slurm_output_diamond/TrimmFastQC_%A-%a.err
#SBATCH --output        slurm_output_diamond/TrimmFastQC_%A-%a.out
#SBATCH --array         0-16
declare -a array=($(seq 1 16))
module load DIAMOND/2.2.4-GCC-14.3.0



CPA=/home/mad149/chapter_meta_analysis/Protein/fl/All_CPA_types_added_detail_uncharacterized.fasta
Bin_CPA=/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/retrieved_from_bins/PF00999_CPA_vsCPA_HQMQ_bins_hmmaligned_filtered_fl.fasta
Combined_Bin_Adriaansens_CPA=/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/Bins_Adriaansens_combined_Fl.fasta
cat ${CPA} ${Bin_CPA} > ${Combined_Bin_Adriaansens_CPA}



diamond blastp --query /home/mad149/Metagenome_grassmere/Assembl_3/Meta_spades_isolate/Prodigal/contigs_${array[$SLURM_ARRAY_TASK_ID]}_Isolate_spades_translated_proteins.faa -d ${Combined_Bin_Adriaansens_CPA} --max-target-seqs 1 --evalue 0.00001 --threads $SLURM_CPUS_PER_TASK --outfmt 6 qseqid sseqid slen evalue bitscore qseq --out /home/mad149/Metagenome_grassmere/Diamond/Diamond_blastp/Contigs/${array[$SLURM_ARRAY_TASK_ID]}_Metaspades_isolate_blastp_vs_protein_CPA.tsv
