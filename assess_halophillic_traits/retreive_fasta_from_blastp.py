import glob
import os


for entry in glob.glob('/home/mad149/Metagenome_grassmere/HQ_MG_mags/homology_search/*/*blastp_protein_Database.tsv'):
    MAG_id = entry.split('/')[-1].split('_blastp')[0]
    path = entry.split('/' + MAG_id +'_blastp')[0]
    with open('{}/{}_blastp_protein_Database_protein_seq.faa'.format(path,MAG_id), 'w') as spittout:
        with open('{}'.format(entry), 'r') as output:
            for line in output:
                
    
                protein_id = '>MAG:' + MAG_id + '_genid:' + line.split('\t')[0] + '_protein_hit:' + line.split('\t')[1]
                protein_sequence = line.split('\t')[-1].split('\n')[0]
                
                combined = protein_id + '\n' + protein_sequence + '\n'
                spittout.write(combined)
