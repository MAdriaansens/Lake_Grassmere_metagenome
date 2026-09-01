from Bio import SeqIO

CPA_dict={}
for record in SeqIO.parse('/home/mad149/chapter_meta_analysis/Protein/fl/All_CPA_types.fasta', 'fasta'):
    if str(record.seq) not in CPA_dict:
        id_list = [record.id]
        CPA_dict[str(record.seq)] = id_list
    else:
        CPA_dict[str(record.seq)].append(record.id)

print(len(CPA_dict))
for record in SeqIO.parse('/home/mad149/Metagenome_grassmere/Retrieve_Homologs_across-contigs/MetaBat_isolate_postDrep_CPAs.fasta', 'fasta'):
    if str(record.seq) not in CPA_dict:
        id_list = [record.id]
        CPA_dict[str(record.seq)] = id_list
    else:
        CPA_dict[str(record.seq)].append(record.id)
print(len(CPA_dict))

for record in SeqIO.parse('/home/mad149/Metagenome_grassmere/Retrieve_Homologs_across-contigs/HMMalign/PF00999_CPA_vsCPA_contigs_hmmaligned.fasta', 'fasta'):
    if str(record.seq) not in CPA_dict:
        id_list = [record.id]
        CPA_dict[str(record.seq)] = id_list
    else:
        CPA_dict[str(record.seq)].append(record.id)
print(len(CPA_dict))

exclusive_contig = 0
in_bins = 0
GTDB_count = 0
for key in CPA_dict.keys():
    if 'Metaspades_isolate' in CPA_dict[key][0]:
        exclusive_contig = exclusive_contig + 1
    elif 'metabat2_isolate_spades' in CPA_dict[key][0]:
        in_bins = in_bins+1
    else:
        GTDB_count = GTDB_count + 1
print(exclusive_contig, in_bins, GTDB_count)


with open('/home/mad149/Metagenome_grassmere/NR_CPA_sequences_GTDB226_bins_contigs.fasta', 'w') as outfile:
    for key in CPA_dict.keys():
        fasta = '>' + CPA_dict[key][0] + '\n' + key + '\n'
        outfile.write(fasta)
