#!/bin/bash -e
#SBATCH --job-name      Prodigal_contig
#SBATCH --time          48:00:00
#SBATCH --mem           50GB
#SBATCH --cpus-per-task 2
#SBATCH --exclude=n[13-15]
#SBATCH --error         slurm_output_prodigal/TrimmFastQC_%A-%a.err
#SBATCH --output        slurm_output_prodigal/TrimmFastQC_%A-%a.out

module load prodigal/2.6.3-GCCcore-12.3.0

for contig in Assembl_3/Meta_spades_isolate/spades_assembly_isolate_Z37TGN_*/contigs.fasta; do
    entry=$(basename "$contig" .fasta)
    prodigal -i $contig -a Assembl_3/Meta_spades_isolate/Prodigal/${entry}_Isolate_spades_translated_proteins.faa
done

for contig in Assembl_3/MetaSpades/spades_assembly_Z37TGN_*/contigs.fasta; do
    entry=$(basename "$contig" .fasta)
    prodigal -i $contig -a Assembl_3/MetaSpades/Prodigal/${entry}_Metaspades_translated_proteins.faa
done
