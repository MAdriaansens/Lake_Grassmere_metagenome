#!/bin/bash -e
#SBATCH --job-name      Diamond
#SBATCH --time          48:00:00
#SBATCH --mem           120GB
#SBATCH --cpus-per-task 20
#SBATCH --exclude=n[13-15]
#SBATCH --error         slurm_output_diamond/TrimmFastQC_%A-%a.err
#SBATCH --output        slurm_output_diamond/TrimmFastQC_%A-%a.out
module load DIAMOND/2.2.4-GCC-14.3.0

DB=/home/mad149/chapter_meta_analysis/Protein/salt_resistance_database.dmnd
#mkdir Diamond_blastp/${array[$SLURM_ARRAY_TASK_ID]}_blastp_vs_protein_database

#for bin in bins/*/*/*_${array[$SLURM_ARRAY_TASK_ID]}/*fna; do
  #  entry=$(basename "$bin" .faa)
    #diamond blastx --query $bin --db ${DB}  --max-target-seqs 1 --evalue 0.00001 --threads $SLURM_CPUS_PER_TASK --outfmt 6 --out Diamond_blastx/${array[$SLURM_ARRAY_TASK_ID]}_vs_protein_database/${entry}_vs_protein_Database.tsv 
#done

#mkdir Diamond_blastp

#for bin in bins/*/*/*/*/protein_files/*.faa; do
#    entry=$(basename "$bin" .faa)
#    echo '${bin}'
#    diamond blastp --query $bin --db ${DB} --max-target-seqs 1 --evalue 0.00001 --threads $SLURM_CPUS_PER_TASK --outfmt 6 qseqid sseqid slen evalue bitscore qseq --out Diamond_blastp/${entry}_blastp_vs_protein_Database.tsv 
#done

for bin in /home/mad149/Metagenome_grassmere/bins/Isolate/MetaBat/*/*/protein_files/*.faa; do
    entry=$(basename "$bin" .faa)
    echo '${bin}'
    diamond blastp --query $bin --db ${DB} --max-target-seqs 1 --evalue 0.00001 --threads $SLURM_CPUS_PER_TASK --outfmt 6 qseqid sseqid slen evalue bitscore qseq --out Diamond_blastp/${entry}_blastp_vs_protein_Database.tsv 
done


for bin in /home/mad149/Metagenome_grassmere/bins/MegaHit/MetaBat/*/*/protein_files/*.faa; do
    entry=$(basename "$bin" .faa)
    echo '${bin}'
    diamond blastp --query $bin --db ${DB} --max-target-seqs 1 --evalue 0.00001 --threads $SLURM_CPUS_PER_TASK --outfmt 6 qseqid sseqid slen evalue bitscore qseq --out Diamond_blastp/${entry}_blastp_vs_protein_Database.tsv 
done
for bin in /home/mad149/Metagenome_grassmere/bins/CoAssembly/MetaBat/*/*/protein_files/*.faa; do
    entry=$(basename "$bin" .faa)
    echo '${bin}'
    diamond blastp --query $bin --db ${DB} --max-target-seqs 1 --evalue 0.00001 --threads $SLURM_CPUS_PER_TASK --outfmt 6 qseqid sseqid slen evalue bitscore qseq --out Diamond_blastp/${entry}_blastp_vs_protein_Database.tsv 
done
