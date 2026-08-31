#!/bin/bash -e
#SBATCH --job-name      Prodigal_contig
#SBATCH --time          24:00:00
#SBATCH --mem           20GB
#SBATCH --cpus-per-task 5
#SBATCH --exclude=n[13-15]
#SBATCH --error         slurm_output_prodigal/TrimmFastQC_%A-%a.err
#SBATCH --output        slurm_output_prodigal/TrimmFastQC_%A-%a.out
#SBATCH --array         0-16

module load prodigal/2.6.3-GCCcore-12.3.0
declare -a array=($(seq 1 16))

for contig in Assembl_3/Meta_spades_isolate/spades_assembly_isolate_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}/contigs.fasta; do
    entry=$(basename "$contig" .fasta)
    prodigal -i $contig -a Assembl_3/Meta_spades_isolate/Prodigal/${entry}_${array[$SLURM_ARRAY_TASK_ID]}_Isolate_spades_translated_proteins.faa
done
