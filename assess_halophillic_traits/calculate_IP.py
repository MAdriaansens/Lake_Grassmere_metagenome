from Bio.SeqUtils.ProtParam import ProteinAnalysis as PA
import glob
import statistics
from Bio import SeqIO

for entry in glob.glob('/home/mad149/Metagenome_grassmere/HQ_MG_mags/*faa'):
    iep_list=[]
    for record in SeqIO.parse('{}'.format(entry), 'fasta'):
        protein=PA(record.seq)
        iep_list.append(protein.isoelectric_point())

        
    median = statistics.median(iep_list)
    average= statistics.mean(iep_list)
    print(entry, median, average)
