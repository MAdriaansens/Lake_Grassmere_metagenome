import glob


with open('CPA_from_contigs_prefilter.fasta', 'w') as output:
    for blastp in glob.glob('Retrieve_Homologs_across-contigs/Diamond_blastp/*/*tsv'):
        bin_searched = blastp.split('/')[-1].split('_blastp_vs_protein')[0]
        #print(bin_searched)
        count  =0
        with open(blastp, 'r') as infile:
            for line in infile:
                if '_Protein' in line:
                        sequence=line.split('\n')[0].split('\t')[-1]
                        if len(sequence) > 262:                                  
                            title = '>' + (blastp.split('/')[-1].split('_blastp_vs_protein')[0]) + '_' + line.split('\t')[0] + '_CPA_{}_protein:'.format(count)+ line.split('\t')[1].split('Protein:')[-1]
                            if sequence.count('X') == 0:
                                fasta = title + '\n' + sequence + '\n'
                                count = count + 1
                            elif (len(sequence)/sequence.count('X')) < 0.2:
                                fasta = title + '\n' + sequence + '\n'
                                count = count + 1
                            output.write(fasta)
with open('TrkH_from_contigs_prefilter.fasta', 'w') as output:
    for blastp in glob.glob('Retrieve_Homologs_across-contigs/Diamond_blastp/*/*tsv'):
        bin_searched = blastp.split('/')[-1].split('_blastp_vs_protein')[0]
        #print(bin_searched)
        count  =0
        with open(blastp, 'r') as infile:
            for line in infile:
                if '_TrkH' in line:
                        sequence=line.split('\n')[0].split('\t')[-1]
                        if len(sequence) > 350:                                  
                            title = '>' + (blastp.split('/')[-1].split('_blastp_vs_protein')[0]) + '_' + line.split('\t')[0] + '_CPA_{}_protein:'.format(count)+ line.split('\t')[1].split('Protein:')[-1]
                            if sequence.count('X') == 0:
                                fasta = title + '\n' + sequence + '\n'
                                count = count + 1
                            elif (len(sequence)/sequence.count('X')) < 0.2:
                                fasta = title + '\n' + sequence + '\n'
                                count = count + 1
                            output.write(fasta)


with open('HPPase_from_contigs_prefilter.fasta', 'w') as output:
    for blastp in glob.glob('Retrieve_Homologs_across-contigs/Diamond_blastp/*/*tsv'):
        bin_searched = blastp.split('/')[-1].split('_blastp_vs_protein')[0]
        #print(bin_searched)
        count  =0
        with open(blastp, 'r') as infile:
            for line in infile:
                if 'H_PPase' in line:
                        sequence=line.split('\n')[0].split('\t')[-1]
                        if len(sequence) > 502:                                  
                            title = '>' + (blastp.split('/')[-1].split('_blastp_vs_protein')[0]) + '_' + line.split('\t')[0] + '_CPA_{}_protein:'.format(count)+ line.split('\t')[1].split('Protein:')[-1]
                            if sequence.count('X') == 0:
                                fasta = title + '\n' + sequence + '\n'
                                count = count + 1
                            elif (len(sequence)/sequence.count('X')) < 0.2:
                                fasta = title + '\n' + sequence + '\n'
                                count = count + 1
                            output.write(fasta)
