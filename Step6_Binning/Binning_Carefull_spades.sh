#!/bin/bash -e
#SBATCH --job-name      IsoMaxbin
#SBATCH --time          10:00:00
#SBATCH --mem           80GB
#SBATCH --cpus-per-task 15
#SBATCH --exclude=n[13-15]
#SBATCH --error         slurm_output_Maxbin/Carefull_bin_%A-%a.err
#SBATCH --output        slurm_output_Maxbin/Carefull_bin_%A-%a.out
#SBATCH --array         0-16
declare -a array=($(seq 1 16))

MODULEPATH=$MODULEPATH:/scratch/projects/sbs-apps/modulefiles
module --ignore_cache load maxbin2/2.2.7 metabat/2.17

module load SAMtools/1.21-GCC-13.3.0



module load seqtk/1.4-GCC-13.3.0
seqtk seq -L 2000 Assembl_3/Meta_spades_careful/spades_assembly_careful_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}/scaffolds.fasta > Step4_filter_size/2k/Carefull_spades_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_2k_filter.fa 

cd bins/Carefull

jgi_summarize_bam_contig_depths --outputDepth metabat_carefullspades_${array[$SLURM_ARRAY_TASK_ID]}.txt /home/mad149/Metagenome_grassmere/Step6_map_reads/Careful_spades/${array[$SLURM_ARRAY_TASK_ID]}_Spades_carefull/*/*.bam

cut -f1,4,6,8,10 metabat_carefullspades_${array[$SLURM_ARRAY_TASK_ID]}.txt > maxbin2_carefullspades_${array[$SLURM_ARRAY_TASK_ID]}.txt

mkdir MetaBat/MetaBat_Carefull_spades_${array[$SLURM_ARRAY_TASK_ID]}
metabat2 -t $SLURM_CPUS_PER_TASK -m 2000 \
         -i /home/mad149/Metagenome_grassmere/Step4_filter_size/2k/Carefull_spades_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_2k_filter.fa  \
         -a /home/mad149/Metagenome_grassmere/bins/Carefull/metabat_carefullspades_${array[$SLURM_ARRAY_TASK_ID]}.txt \
         -o MetaBat/MetaBat_Carefull_spades_${array[$SLURM_ARRAY_TASK_ID]}/metabat2_carefull_spades_${array[$SLURM_ARRAY_TASK_ID]}
         
mkdir MaxBin2/MaxBin2_Carefull_spades_${array[$SLURM_ARRAY_TASK_ID]}
run_MaxBin.pl -thread $SLURM_CPUS_PER_TASK -min_contig_length 2000 \
              -contig /home/mad149/Metagenome_grassmere/Step4_filter_size/2k/Carefull_spades_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_2k_filter.fa \
              -abund /home/mad149/Metagenome_grassmere/bins/Carefull/maxbin2_carefullspades_${array[$SLURM_ARRAY_TASK_ID]}.txt \
              -out MaxBin2/MaxBin2_Carefull_spades_${array[$SLURM_ARRAY_TASK_ID]}/maxbin2_carefull_spades__${array[$SLURM_ARRAY_TASK_ID]}
