from Bio import SeqIO
import os

with open('barrnap_output_noMetaSpades.tsv', 'w') as barrnap:
    header = 'bin' +'\t' + 'are_all_sRNA_Present' + '\t' +'16sRNA_count' + '\t' + '23sRNA_count' + '\t' + '5sRNA_count' + '\n'
    barrnap.write(header)
    for file in os.listdir('barrnap'):
        RNA16s_count = 0
        RNA5s_count = 0
        RNA23s_count = 0 
        all_sRNAss_present = 'no'
        if 'fasta' in file:
            if os.stat('barrnap/{}'.format(file)).st_size == 0 :
                if '.fa_' in file:
                    bin_name = file.split('.fa_')[0]
                else:
                    bin_name = file.split('_rna')[0]
                line = bin_name + '\t' + all_sRNAss_present + '\t' +  str(RNA16s_count) + '\t' + str(RNA23s_count) + '\t' + str(RNA5s_count) + '\n'
                barrnap.write(line)
            else:
                for record in SeqIO.parse('barrnap/{}'.format(file), 'fasta'):
                    if '16S_rRNA' in record.id:
                        RNA16s_count +=1
                    elif  '23S_rRNA' in record.id:
                        RNA23s_count +=1
                    elif '5S_rRNA' in record.id:
                        RNA5s_count +=1
                    else:
                        print(record.id)
                if '.fa_' in file:
                    bin_name = file.split('.fa_')[0]
                else:
                    bin_name = file.split('_rna')[0]
                if (RNA16s_count > 0 and RNA23s_count > 0 and RNA5s_count > 0):
                    all_sRNAss_present = 'yes'
                else:
                    all_sRNAss_present = 'no'
                line = bin_name + '\t' + all_sRNAss_present + '\t' +  str(RNA16s_count) + '\t' + str(RNA23s_count) + '\t' + str(RNA5s_count) + '\n'
                barrnap.write(line)
