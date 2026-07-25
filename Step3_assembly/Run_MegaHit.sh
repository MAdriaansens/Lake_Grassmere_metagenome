#!/bin/bash -e
#SBATCH --job-name      MegaHit
#SBATCH --time          24:00:00
#SBATCH --mem           20GB
#SBATCH --cpus-per-task 15
#SBATCH --exclude=n[13-15]
#SBATCH --error         slurm_output_MegaHit/TrimmFastQC_%A-%a.err
#SBATCH --output        slurm_output_MegaHit/TrimmFastQC_%A-%a.out


Path=/home/mad149/Metagenome_grassmere/Assembl_3/Megahit
MODULEPATH=$MODULEPATH:/scratch/projects/sbs-apps/modulefiles
module --ignore_cache load megahit/1.2.9

megahit -1 Trimm_2/Z37TGN_13_sample_13_R1.qc.fastq.gz -2 Trimm_2/Z37TGN_13_sample_13_R2.qc.fastq.gz -t $SLURM_CPUS_PER_TASK -o ${Path}/Megahit_Z37TGN_13 –-k-min 27 –-k-max 127 –-k-step 10 -–min-contig-len 500 –-prunelevel 3 –-no-mercy –-min-count 3 –-no-local 
