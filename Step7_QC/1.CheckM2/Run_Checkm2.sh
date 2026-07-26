#!/bin/bash -e
#SBATCH --job-name      CheckM2
#SBATCH --time          8:00:00
#SBATCH --mem           60GB
#SBATCH --cpus-per-task 38
#SBATCH --exclude=n[13-15]
#SBATCH --error         slurm_output_CheckM2/TrimmFastQC_%A-%a.err
#SBATCH --output        slurm_output_CheckM2/TrimmFastQC_%A-%a.out
#SBATCH --array         0-16
declare -a array=($(seq 1 16))
MODULEPATH=$MODULEPATH:/scratch/projects/sbs-apps/modulefiles
module --ignore_cache load checkm2/1.1.0


for f in bins/Metaspades/MetaBat/MetaBat_Metaspades_${array[$SLURM_ARRAY_TASK_ID]}/*.fa; do mv -- "$f" "${f%.fa}.fna"; done

#checkm2 database --download
checkm2 predict -t 38 --input bins/Metaspades/MetaBat/MetaBat_Metaspades_${array[$SLURM_ARRAY_TASK_ID]} --output_directory bins/Metaspades/MetaBat/MetaBat_Metaspades_${array[$SLURM_ARRAY_TASK_ID]}/MetaBat_Metaspades_Sample${array[$SLURM_ARRAY_TASK_ID]}_checkm2


for f in bins/Metaspades/MaxBin2/MaxBin2_Metaspades_${array[$SLURM_ARRAY_TASK_ID]}/*.fasta; do mv -- "$f" "${f%.fasta}.fna"; done

checkm2 predict -t 38 --input bins/Metaspades/MaxBin2/MaxBin2_Metaspades_${array[$SLURM_ARRAY_TASK_ID]} --output_directory bins/Metaspades/MaxBin2/MaxBin2_Metaspades_${array[$SLURM_ARRAY_TASK_ID]}/MaxBin2_Metaspades_Sample${array[$SLURM_ARRAY_TASK_ID]}_checkm2
