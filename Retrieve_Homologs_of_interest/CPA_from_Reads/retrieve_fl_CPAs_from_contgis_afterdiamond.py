from Bio import SeqIO
FL_dict={}
for record in SeqIO.parse("/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/CPA_sequences_vs_HQMQ_bins.fasta", 'fasta'):
    FL_dict[record.id] = str(record.seq)


with open("/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/CPA_sequences_vs_HQMQ_bins_filtered_fl.fasta", "w") as outfile:
    for record in SeqIO.parse('/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/CPA_sequences_vs_HQMQ_bins_hmmaligned_filterd.fasta', 'fasta'):
        FL_sequence=(FL_dict[record.id])
        Line = '>' + record.id + '\n' + FL_sequence + '\n'
        outfile.write(Line)
from Bio import SeqIO
import glob
FL_contigs_dict={}
for contig in glob.glob('/home/mad149/Metagenome_grassmere/Assembl_3/Meta_spades_isolate/Prodigal/*faa'):
    for record in SeqIO.parse(contig, 'fasta'):
        FL_contigs_dict[record.id] = str(record.seq)
import glob        
diamond_runs=glob.glob('/home/mad149/Metagenome_grassmere/Diamond/Diamond_blastp/Contigs/*.tsv')
hit_cpa = []
for diamond in diamond_runs:
    count = 0
    sample = diamond.split('/')[-1].split('_vs_')[0].split('_')[0]
    with open(diamond, 'r') as infile:
        for line in infile:
            Protein_id = line.split('\t')[0]
            hit_cpa.append(Protein_id)
with open('/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/retrieved_from_contigs/CPA_sequences_from_contigs_prokka_translated.fasta', 'w') as outfile:
    for cpa in hit_cpa:
        line = '>_contig_{}'.format(cpa) + '\n' + FL_contigs_dict[cpa] + '\n'
        outfile.write(line)
