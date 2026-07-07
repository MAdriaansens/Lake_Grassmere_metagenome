module load Trimmomatic/0.39-Java-17

trimmomatic PE -threads 1 -phred33 -trimlog Illumina_Nextera_adapter.faa \
               Z37TGN_10_sample_10_R1_subset8000.fastq.gz Z37TGN_10_sample_10_R2_subset8000.fastq.gz\
               Z37TGN_10_sample_10_R1_subset8000.qc.fastq.gz Z37TGN_10_sample_10_s1_subset8000.fastq.gz Z37TGN_10_sample_10_R2_subset8000.qc.fastq.gz Z37TGN_10_sample_10_s2_subset8000.fastq.gz \
               ILLUMINACLIP:NexteraPE-PE.fa:1:25:7 SLIDINGWINDOW:4:30 MINLEN:80
               
#https://github.com/timflutre/trimmomatic/blob/master/adapters/NexteraPE-PE.fa




module load BBMap/39.19-GCC-12.3.0
bbduk.sh in=Z37TGN_10_sample_10_R1_subset8000.qc.fastq.gz out=Z37TGN_10_sample_10_R1_subset8000_bbduktrimmed.qc.fastq.gz ftl=2

module load FastQC/0.12.1-Java-11
fastqc Z37TGN_10_sample_10_R1_subset8000_bbduktrimmed.qc.fastq.gz Z37TGN_10_sample_10_R2_subset8000.qc.fastq.gz

spades.py --meta -k 33,55,77,99,121 -t $SLURM_CPUS_PER_TASK \
          -1 ${Trim}/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_sample_${array[$SLURM_ARRAY_TASK_ID]}_R1.qc.fastq.gz -2 ${Trim}/Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}_sample_${array[$SLURM_ARRAY_TASK_ID]}_R2.qc.fastq.gz \
          -o spades_assembly_Z37TGN_${array[$SLURM_ARRAY_TASK_ID]}

module load prodigal/2.6.3-GCCcore-12.3.0
prodigal -i Assembl_3/spades_assembly_Z37TGN_15/contigs.fasta -o Prodigal/Z37GTN_15/Z37GTN_sample_15_genes.fna -a Prodigal/Z37GTN_15/Z37GTN_sample_15_proteins.faa -p meta
