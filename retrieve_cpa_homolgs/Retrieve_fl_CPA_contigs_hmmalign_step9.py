from Bio import SeqIO
with open('/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/retrieved_from_contigs/NR_CPA_sequences_contigs_hmmaligned_filtered_fl.fasta', 'w') as output:
    FL_dict={}
    for record in SeqIO.parse('/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/retrieved_from_contigs/CPA_sequences_vs_contigs_rerun_fl.fasta', 'fasta'):
        FL_dict[record.id] = record.seq
    for passed in SeqIO.parse('/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/retrieved_from_contigs/NR_CPA_sequences_contigs_hmmaligned_filtered.fasta', 'fasta'):
        sequence = str(FL_dict[passed.id])
        Line = '>' + passed.id + '\n' + sequence + '\n'
        output.write(Line)
