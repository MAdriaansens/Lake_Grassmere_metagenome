from Bio import SeqIO
with open('/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/retrieved_from_bins/PF00999_CPA_vsCPA_HQMQ_bins_hmmaligned_filtered_fl.fasta', 'w') as output:
    FL_dict={}
    for record in SeqIO.parse('/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/retrieved_from_bins/CPA_sequences_vs_HQMQ_bins_rerun.fasta', 'fasta'):
        FL_dict[record.id] = record.seq
    for passed in SeqIO.parse('/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/retrieved_from_bins/PF00999_CPA_vsCPA_HQMQ_bins_hmmaligned_filtered.fasta', 'fasta'):
        sequence = str(FL_dict[passed.id])
        Line = '>' + passed.id + '\n' + sequence + '\n'
        output.write(Line)
