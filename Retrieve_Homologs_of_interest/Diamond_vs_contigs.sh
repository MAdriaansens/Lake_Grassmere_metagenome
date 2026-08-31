#!/bin/bash -e
#SBATCH --job-name      Diamond
#SBATCH --time          20:00:00
#SBATCH --mem           12GB
#SBATCH --cpus-per-task 20
#SBATCH --exclude=n[13-15]
#SBATCH --error         slurm_output_diamond/TrimmFastQC_%A-%a.err
#SBATCH --output        slurm_output_diamond/TrimmFastQC_%A-%a.out
#SBATCH --array         0-16

declare -a array=($(seq 1 16))
module load DIAMOND/2.2.4-GCC-14.3.0

DB=/home/mad149/chapter_meta_analysis/Protein/salt_resistance_database.dmnd

diamond blastp --query Assembl_3/Meta_spades_isolate/Prodigal/contigs_${array[$SLURM_ARRAY_TASK_ID]}_Isolate_spades_translated_proteins.faa --db ${DB} --max-target-seqs 1 --evalue 0.00001 --threads $SLURM_CPUS_PER_TASK --outfmt 6 qseqid sseqid slen evalue bitscore qseq --out Retrieve_Homologs_across-contigs/Diamond_blastp/Database/${array[$SLURM_ARRAY_TASK_ID]}_Metaspades_isolate_blastp_vs_protein_Database.tsv 

CPA=Retrieve_Homologs_across-contigs/HMMalign/PF00999_CPA_vsCPA_HQMQ_bins_hmmaligned.fasta

diamond blastp --query Assembl_3/Meta_spades_isolate/Prodigal/contigs_${array[$SLURM_ARRAY_TASK_ID]}_Isolate_spades_translated_proteins.faa -d ${CPA} --max-target-seqs 1 --evalue 0.00001 --threads $SLURM_CPUS_PER_TASK --outfmt 6 qseqid sseqid slen evalue bitscore qseq --out Retrieve_Homologs_across-contigs/Diamond_blastp/INH/${array[$SLURM_ARRAY_TASK_ID]}_Metaspades_isolate_blastp_vs_protein_CPAe.tsv 

TrkH=Retrieve_Homologs_across-contigs/HMMalign/PF02386_TrkH_vsTrkH_HQMQ_bins_hmmaligned.fasta

diamond blastp --query Assembl_3/Meta_spades_isolate/Prodigal/contigs_${array[$SLURM_ARRAY_TASK_ID]}_Isolate_spades_translated_proteins.faa -d ${TrkH} --max-target-seqs 1 --evalue 0.00001 --threads $SLURM_CPUS_PER_TASK --outfmt 6 qseqid sseqid slen evalue bitscore qseq --out Retrieve_Homologs_across-contigs/Diamond_blastp/INH/${array[$SLURM_ARRAY_TASK_ID]}_Metaspades_isolate_blastp_vs_protein_TrkH.tsv 

HPPase=Retrieve_Homologs_across-contigs/HMMalign/PF03030_HPPase_vsHPPase_HQMQ_bins_hmmaligned.fasta

diamond blastp --query Assembl_3/Meta_spades_isolate/Prodigal/contigs_${array[$SLURM_ARRAY_TASK_ID]}_Isolate_spades_translated_proteins.faa -d ${HPPase} --max-target-seqs 1 --evalue 0.00001 --threads $SLURM_CPUS_PER_TASK --outfmt 6 qseqid sseqid slen evalue bitscore qseq --out Retrieve_Homologs_across-contigs/Diamond_blastp/INH/${array[$SLURM_ARRAY_TASK_ID]}_Metaspades_isolate_blastp_vs_protein_Hppase.tsv 
