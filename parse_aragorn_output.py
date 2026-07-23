import os
with open('/home/mad149/Metagenome_grassmere/Aragorn_output_noMetaSpades.tsv', 'w') as AO:
    header = 'bin' + '\t' + 'number_tRNAs' + '\t' + 'number_UniqAA_tRNAs' + '\n'
    AO.write(header)
    for Aragorn_output in os.listdir('/home/mad149/Metagenome_grassmere/Aragorn'):
        tRNA_list=[]
        if 'txt' in Aragorn_output:
            with open('/home/mad149/Metagenome_grassmere/Aragorn/{}'.format(Aragorn_output), 'r') as tRNAs:
                for tRNA in tRNAs:
                    tRNA_list.append(tRNA.split('\n')[0].split(' ')[-1])
            uniq_AA_tRNA = (len(set(tRNA_list)))
            total_tRNA =  len(tRNA_list)
            bin_name = (Aragorn_output.split('output_edit_')[1].split('.fa')[0])
            if 'fna' in bin_name:
                bin_name = bin_name.split('.fna')[0]
            line = bin_name + '\t' + str(total_tRNA) + '\t' + str(uniq_AA_tRNA) + '\n'
            AO.write(line)
