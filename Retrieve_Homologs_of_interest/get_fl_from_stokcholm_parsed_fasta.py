from Bio import SeqIO
FL_dict={}
for record in SeqIO.parse("/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/CPA_sequences_vs_HQMQ_bins.fasta", 'fasta'):
    FL_dict[record.id] = str(record.seq)


with open("/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/CPA_sequences_vs_HQMQ_bins_filtered_fl.fasta", "w") as outfile:
    for record in SeqIO.parse('/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/CPA_sequences_vs_HQMQ_bins_hmmaligned_filterd.fasta', 'fasta'):
        FL_sequence=(FL_dict[record.id])
        Line = '>' + record.id + '\n' + FL_sequence + '\n'
        outfile.write(Line)
