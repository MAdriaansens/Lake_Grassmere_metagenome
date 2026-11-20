import subprocess
Read_samples = {'1':36423842, '2':36423842,'3':36423842,'4':36423842, '5':36423842, '6':36423842, '7':36423842,'8':36423842, '9':36423842, '10':36334532,'11':36423842,12:36423842, '13':36423842, '14':36423842}

Lengths = '/home/mad149/Metagenome_grassmere/HQ_MG_mags/HQ_MQ_mag_lengths.txt'
Bin_length_dict={}
with open(Lengths, 'r') as lengths:
    for length in lengths:
        MAG_id=(length.split('\t')[0])
        L = length.split('\t')[1].split('\n')[0]
        Bin_length_dict[MAG_id] = L
with open('Abundance_all_MAGs.tsv', 'w') as abundance:
    abundance.write('MAG_id' + '\t' + 'Abundance percentage' + '\n')
    for name_bin in Bin_length_dict.keys():
        if 'NCBI' in name_bin:
            pass
        else:
            sample_name = name_bin.split('.')[0].split('_')[3]
            result = subprocess.run(["awk", "{s+=$3} END{print s+0}", "/home/mad149/Metagenome_grassmere/Read_mapping_to_MAGs/bw_index_{}/Mapping/{}_vs_Sample_{}_idxstats.tsv".format(name_bin, name_bin, sample_name)],
                                    capture_output=True,
                                    text=True,
                                    check=True)
            total_reads_mapped = int(result.stdout.strip())
            Rel_abundance= (total_reads_mapped/Read_samples['3'])*100
            print(name_bin, Rel_abundance)
            abundance.write(name_bin + '\t' + str(Rel_abundance)+'\n')
