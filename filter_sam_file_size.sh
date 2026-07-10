module load SAMtools
samtools view -H mapped_reads_Z37TGN_6_scaffold.sam | grep "^@SQ" | sed 's/^@SQ\t//' | cut -f 1,2 | sed 's/SN://g; s/LN://g' | awk '$2 > 2000'
> all_scaffolds_greater_2000.txt

samtools view -L all_scaffolds_greater_2000.txt -h mapped_reads_Z37TGN_6_scaffold.sam > filtered.sam
