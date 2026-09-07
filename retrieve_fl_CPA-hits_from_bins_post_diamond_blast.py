import glob        
diamond_runs=glob.glob('/home/mad149/Metagenome_grassmere/Diamond/Diamond_blastp/Bins/*.tsv')
hit_cpas_and_their_bins = {}
for diamond in diamond_runs:
    count = 0
    hit_bin = diamond.split('/')[-1].split('_vs_')[0]
    sample=hit_bin.split('_')[-1].split('.')[0]
    with open(diamond, 'r') as infile:
        for line in infile:
            hit_cpas_and_their_bins
            hit_cpas_and_their_bins[hit_bin + '_CPA_count' + str(count)] = (sample, hit_bin, line.split('\t')[0]) 
            count = count + 1
        
interest_list =  []
with open('/home/mad149/Metagenome_grassmere/Best_assembly_bins.txt') as good_bins:
    for good_bin in good_bins:
        interest_list.append(good_bin.split('\n')[0])
sequence_dic={}
from Bio import SeqIO
all_bins = glob.glob('/home/mad149/Metagenome_grassmere/bins/Isolate/MetaBat/MetaBat_Isolate_spades_*/MetaBat_Isolate_spades_Sample*_checkm2/protein_files/*faa')
for entry in all_bins:
    if entry .split('/')[-1].split('.fa')[0] in interest_list:
        for record in SeqIO.parse('{}'.format(entry), 'fasta'):
            sequence_dic[record.id] = record.seq
with open('Retrieved_CPAseqs/CPA_sequences_vs_HQMQ_bins.fasta', 'w') as output:
    for key in hit_cpas_and_their_bins.keys():
        CPA_id=(hit_cpas_and_their_bins[key][-1])
        protein_id = key + '_' + CPA_id
        line = '>' + protein_id + '\n'  + str(sequence_dic[CPA_id]) + '\n' 
        output.write(line)
