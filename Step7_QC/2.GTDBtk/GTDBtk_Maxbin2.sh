#!/bin/bash -e
#SBATCH --job-name      GTDBtkIso
#SBATCH --time          5:00:00
#SBATCH --mem           200GB
#SBATCH --cpus-per-task 38
#SBATCH --exclude=n[13-15]
#SBATCH --error         slurm_output_GTDBTK/IsoTrimmFastQC_%A-%a.err
#SBATCH --output        slurm_output_GTDBTK/IsoTrimmFastQC_%A-%a.out
#SBATCH --array         0-16
declare -a array=($(seq 1 16))
#change path accordingly
MODULEPATH=$MODULEPATH:/scratch/projects/sbs-apps/modulefiles
module --ignore_cache load gtdbtk/2.7.2
#mkdir bins/Isolate/MaxBin2/MaxBin2_Isolate_spades_${array[$SLURM_ARRAY_TASK_ID]}/GTDBTK_output

gtdbtk classify_wf --genome_dir bins/Metaspades/MaxBin2/MaxBin2_Metaspades_${array[$SLURM_ARRAY_TASK_ID]} --out_dir bins/Metaspades/MaxBin2/MaxBin2_Metaspades_${array[$SLURM_ARRAY_TASK_ID]}/GTDBTK_output --cpus 38
