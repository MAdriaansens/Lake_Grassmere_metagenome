#!/bin/bash -e
#SBATCH --job-name      MegaHit
#SBATCH --time          24:00:00
#SBATCH --mem           100GB
#SBATCH --cpus-per-task 38
#SBATCH --exclude=n[13-15]
#SBATCH --error         slurm_output_CheckM2/TrimmFastQC_%A-%a.err
#SBATCH --output        slurm_output_CheckM2/TrimmFastQC_%A-%a.out

MODULEPATH=$MODULEPATH:/scratch/projects/sbs-apps/modulefiles
module --ignore_cache load checkm2/1.1.0

#checkm2 database --download
checkm2 predict -t 38 --input /home/mad149/Metagenome_grassmere/bins/bins --output_directory CheckM2/MegaHit_Sample1_checkm2
