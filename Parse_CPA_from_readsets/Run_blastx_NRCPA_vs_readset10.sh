#!/bin/bash -e
#SBATCH --job-name      XBLAST
#SBATCH --time          12:00:00
#SBATCH --mem           20GB
#SBATCH --cpus-per-task 10
#SBATCH --error         slurm_xblastoutput2/Bacscan2_%A-%a.err
#SBATCH --output        slurm_xblastoutput2/Bacscan2_%A-%a.out

METADIR=/scratch/projects/sbs/project/grassmere_metagenomic_Adriaansens/data
module load DIAMOND/2.1.8-GCC-12.3.0

cd /home/mad149/Metagenome_grassmere/output_xblast_NRCPA

DB=/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/NR_CPA_sequences_GTDB226_bins_contigs_hmmaligned_filtered.fasta.fasta

diamond blastx --threads ${SLURM_CPUS_PER_TASK} --evalue 0.00001  --max-target-seqs 1  --outfmt 6 qseqid sseqid slen evalue bitscore qseq qseq_translated --db ${DB} -q ${METADIR}/YPQMX3_1_rerun_sample_10_10_R1.fastq.gz --out Z37TGN_10_sample_10_R1_vs_NRCPA_DB.m8

diamond blastx --threads ${SLURM_CPUS_PER_TASK} --evalue 0.00001 --max-target-seqs 1 --outfmt 6 qseqid sseqid slen evalue bitscore qseq qseq_translated --db ${DB} -q ${METADIR}/YPQMX3_1_rerun_sample_10_10_R2.fastq.gz --out Z37TGN_10_sample_10_R2_vs_NRCPA_DB.m8

DB=/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/Tree_sequences_CPA_TREE_ALIGNEDMMSEQ1_PF00999_28April_final_iteration_filtered_HMMalign.fasta
diamond blastx --threads ${SLURM_CPUS_PER_TASK} --evalue 0.00001  --max-target-seqs 1  --outfmt 6 qseqid sseqid slen evalue bitscore qseq qseq_translated --db ${DB} -q ${METADIR}/YPQMX3_1_rerun_sample_10_10_R1.fastq.gz --out Z37TGN_10_sample_10_R1_vs_treeCPA_DB.m8

echo "running R2"
diamond blastx --threads ${SLURM_CPUS_PER_TASK} --evalue 0.00001 --max-target-seqs 1 --outfmt 6 qseqid sseqid slen evalue bitscore qseq qseq_translated --db ${DB} -q ${METADIR}/YPQMX3_1_rerun_sample_10_10_R2.fastq.gz --out Z37TGN_10_sample_10_R2_vs_treeCPA_DB.m8


DB=/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/NR_CPA_sequences_GTDB226_bins_contigs_hmmaligned_filtered_clustered_70.fasta_rep_seq.fasta
diamond blastx --threads ${SLURM_CPUS_PER_TASK} --evalue 0.00001  --max-target-seqs 1  --outfmt 6 qseqid sseqid slen evalue bitscore qseq qseq_translated --db ${DB} -q ${METADIR}/YPQMX3_1_rerun_sample_10_10_R1.fastq.gz --out Z37TGN_10_sample_10_R1_vs_NRCPA_70seqidDB.m8

echo "running R2"
diamond blastx --threads ${SLURM_CPUS_PER_TASK} --evalue 0.00001 --max-target-seqs 1 --outfmt 6 qseqid sseqid slen evalue bitscore qseq qseq_translated --db ${DB} -q ${METADIR}/YPQMX3_1_rerun_sample_10_10_R2.fastq.gz --out Z37TGN_10_sample_10_R2_vs_NRCPA_70seqidDB.m8
