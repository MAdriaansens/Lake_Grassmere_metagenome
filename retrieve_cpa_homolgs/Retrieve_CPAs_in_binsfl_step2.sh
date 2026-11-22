

Best_hit_CPA_bins={}
with open('/home/mad149/Metagenome_grassmere/Retrieved_CPAseqs/retrieved_from_bins/CPA_sequences_vs_HQMQ_bins_rerun.fasta', 'w') as outfile:
    for blastp in glob.glob('/home/mad149/Metagenome_grassmere/Diamond/Diamond_blastp/Bins/metabat2_isolate_*_CPA.tsv'):
        print(blastp)
        with open(blastp, 'r') as parse:
                count = 0
                for line in parse:   
                    if '_Protein' in line:
                        sequence=line.split('\n')[0].split('\t')[-1]
                        if len(sequence) > 262:                                  
                            
                            title = '>' + (blastp.split('/')[-1].split('_vs_all_CPA.tsv')[0])+ '_CPA_count{}'.format(count) +'_' + line.split('\t')[0] + '_' + line.split('\t')[1].split('Protein:')[-1]

                            if sequence.count('X') == 0:
                                fasta = title + '\n' + sequence + '\n'
                                count = count + 1
                                outfile.write(fasta)
                            elif (len(sequence)/sequence.count('X')) < 0.2:
                                fasta = title + '\n' + sequence + '\n'
                                count = count + 1
                                outfile.write(fasta)
