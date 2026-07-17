#!/bin/bash -e
#SBATCH --job-name      CheckM1
#SBATCH --time          24:00:00
#SBATCH --mem           100GB
#SBATCH --cpus-per-task 38
#SBATCH --exclude=n[13-15]
#SBATCH --error         slurm_output_CheckM1/TrimmFastQC_%A-%a.err
#SBATCH --output        slurm_output_CheckM1/TrimmFastQC_%A-%a.out

MODULEPATH=$MODULEPATH:/scratch/projects/sbs-apps/modulefiles
module --ignore_cache load checkm/1.2.3

#checkm2 database --download
checkm lineage_wf -t 38 /home/mad149/Metagenome_grassmere/bins/bins CheckM1/MegaHit_Sample1_checkm1
