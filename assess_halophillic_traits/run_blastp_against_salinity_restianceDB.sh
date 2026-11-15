#!/bin/bash -e
#SBATCH --job-name      Diamond_test
#SBATCH --time          6:00:00
#SBATCH --mem           20GB
#SBATCH --cpus-per-task 15
#SBATCH --exclude=n[13-15]
#SBATCH --error         slurm_test/BacscanR_%A-%a.err
#SBATCH --output        slurm_test/BacscanR_%A-%a.out
#SBATCH --array         0-69%69
declare -a array=($(seq 0 69))

ID_LIST=/home/mad149/Metagenome_grassmere/HQ_MQ_mags.txt
Line_number=${array[$SLURM_ARRAY_TASK_ID]}

Output=/home/mad149/Metagenome_grassmere/HQ_MG_mags/homology_search
SRR_ID=$(head -n ${array[$SLURM_ARRAY_TASK_ID]} ${ID_LIST} | tail -n1) 
echo "${SRR_ID}"


module load DIAMOND/2.2.4-GCC-14.3.0
DB=/home/mad149/chapter_meta_analysis/Protein/salt_resistance_database.dmnd

#mkdir ${Output}/${SRR_ID}_Diamond_output

diamond blastp --query /home/mad149/Metagenome_grassmere/HQ_MG_mags/${SRR_ID}.fa.faa --db ${DB} --max-target-seqs 1 --evalue 0.00001 --threads $SLURM_CPUS_PER_TASK --outfmt 6 qseqid sseqid slen evalue bitscore qseq --out ${Output}/${SRR_ID}_Diamond_output/${SRR_ID}_blastp_protein_Database.tsv 
