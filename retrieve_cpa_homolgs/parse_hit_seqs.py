
import os
import glob
import csv
from collections import Counter, defaultdict


# ============================================================
# 1. Load GTDB-Tk taxonomy
# ============================================================

GTDBtk_dict = {}

taxonomy_file = (
    '/home/mad149/Metagenome_grassmere/'
    'Suppl_Chapter_Four_STable4dot12.csv'
)

with open(taxonomy_file, 'r', newline='') as gtdb:
    reader = csv.reader(gtdb)

    for row in reader:
        if len(row) >= 2:
            GTDBtk_dict[row[0].strip()] = row[1].strip()


# ============================================================
# 2. Load CPA protein references from MAGs and contigs
# ============================================================

Best_hit_CPA_bins = {}


def load_cpa_hits(pattern, file_type):

    for blastp in glob.glob(pattern):

        print('Loading:', blastp)

        filename = os.path.basename(blastp)

        if file_type == 'MAG':
            prefix = filename.split('_vs_all_CPA.tsv')[0]

        else:
            prefix = filename.split(
                '_blastp_vs_protein_CPA.tsv'
            )[0]

        count = 0

        with open(blastp, 'r') as parse:

            for line in parse:

                fields = line.rstrip('\n').split('\t')

                if len(fields) < 3:
                    continue

                query_id = fields[0]
                tree_protein = fields[1]
                sequence = fields[-1]

                if '_Protein' not in line:
                    continue

                if len(sequence) <= 262:
                    continue

                # Retain sequences containing less than 20%
                # unidentified amino acids (X).

                x_fraction = sequence.count('X') / len(sequence)

                if x_fraction >= 0.2:
                    continue

                if file_type == 'MAG':

                    title = (
                        prefix +
                        '_CPA_count{}'.format(count) +
                        '_' + query_id +
                        '_Protein:' +
                        tree_protein.split('Protein:')[-1]
                    )

                else:

                    title = (
                        prefix +
                        '_contig_CPA_count{}'.format(count) +
                        '_' + query_id +
                        '_' + tree_protein.split('Protein:')[-1]
                    )

                Best_hit_CPA_bins[title] = tree_protein

                count += 1


# MAG CPA proteins

load_cpa_hits(
    '/home/mad149/Metagenome_grassmere/Diamond/'
    'Diamond_blastp/Bins/metabat2_isolate_*_CPA.tsv',
    'MAG'
)


# Contig CPA proteins

load_cpa_hits(
    '/home/mad149/Metagenome_grassmere/Diamond/'
    'Diamond_blastp/Contigs/*.tsv',
    'Contig'
)


print('Total CPA reference proteins:', len(Best_hit_CPA_bins))


# ============================================================
# 3. Function to find unambiguous best hits
# ============================================================

def process_alignment_files(files):

    # Each read stores:
    # [best_evalue, set_of_proteins_with_best_evalue]

    Best_hits = {}

    for filename in files:

        with open(filename, 'r') as infile:

            for line in infile:

                fields = line.rstrip('\n').split('\t')

                if len(fields) < 4:
                    continue

                read_id = fields[0]
                hit_protein = fields[1]

                try:
                    e_value = float(fields[3])
                except ValueError:
                    continue

                if read_id not in Best_hits:

                    Best_hits[read_id] = [
                        e_value,
                        {hit_protein}
                    ]

                else:

                    current_best = Best_hits[read_id][0]

                    if e_value < current_best:

                        # A better hit replaces previous hits.
                        # Previous ambiguity is also resolved.

                        Best_hits[read_id] = [
                            e_value,
                            {hit_protein}
                        ]

                    elif e_value == current_best:

                        # Different proteins with identical
                        # best E-values are ambiguous.

                        Best_hits[read_id][1].add(hit_protein)

    # Exclude reads with multiple equally good protein hits.

    Protein_counts = Counter()

    for best_evalue, proteins in Best_hits.values():

        if len(proteins) == 1:

            Protein_counts.update(proteins)

    return Protein_counts


# ============================================================
# 4. Process all 14 samples
# ============================================================

All_proteins = set()

Sample_protein_counts = {}

for number in range(1, 15):

    files = [
        '/home/mad149/Metagenome_grassmere/'
        'output_xblast_NRCPA/'
        'Z37TGN_{}_sample_{}_R1_vs_NRCPA_DB.m8'.format(
            number, number
        ),

        '/home/mad149/Metagenome_grassmere/'
        'output_xblast_NRCPA/'
        'Z37TGN_{}_sample_{}_R2_vs_NRCPA_DB.m8'.format(
            number, number
        )
    ]

    Protein_counts = process_alignment_files(files)

    Sample_protein_counts[number] = Protein_counts

    unique_proteins = set(Protein_counts.keys())

    All_proteins.update(unique_proteins)

    print(
        'Sample {}: {} unique proteins'.format(
            number,
            len(unique_proteins)
        )
    )


print(
    'Total unique proteins across all samples:',
    len(All_proteins)
)


# ============================================================
# 5. Generate taxonomy-annotated protein names
# ============================================================

GTDBtk_name = {}


def get_tree_protein_name(unique_protein):

    # Proteins not originating from MAGs or contigs
    # retain their original protein names.

    if 'NODE' not in unique_protein:

        return unique_protein

    # MAG proteins: annotate with GTDB-Tk taxonomy.

    if 'metabat2_isolate' in unique_protein:

        if unique_protein in GTDBtk_name:

            return GTDBtk_name[unique_protein]

        MAG_id = unique_protein.split('_CPA_count')[0]

        GTDBtk_tax = GTDBtk_dict.get(
            MAG_id,
            'UNKNOWN_TAXONOMY'
        )

        try:
            CPA_count = (
                unique_protein.split('_CPA_count')[1]
                .split('_NODE')[0]
            )
        except IndexError:
            CPA_count = 'UNKNOWN'

        if 'Uncharacterized_family' in unique_protein:

            subfamily = unique_protein.split(
                'Uncharacterized_family', 1
            )[1]

            subfamily = 'Uncharacterized_family' + subfamily

        else:

            subfamily = unique_protein.split('_')[-1]

        new_title = (
            MAG_id +
            '_tax:' + GTDBtk_tax +
            '_CPA_count' + CPA_count +
            '_Protein:' + subfamily
        )

        GTDBtk_name[unique_protein] = new_title

        return new_title

    # Contig proteins: retrieve their original tree protein name.

    return Best_hit_CPA_bins.get(
        unique_protein,
        unique_protein
    )


# ============================================================
# 6. Write final protein counts per sample
# ============================================================

output_file = (
    '/home/mad149/Metagenome_grassmere/'
    'treeCPAs_hit_per_sample.tsv'
)

# Sort proteins to ensure reproducible output ordering.

All_proteins = sorted(All_proteins)

# Generate protein names once rather than once per sample.

Protein_tree_names = {
    protein: get_tree_protein_name(protein)
    for protein in All_proteins
}


with open(output_file, 'w') as out:

    header = (
        'protein_hit\t'
        'tree_protein_name\t'
        'count_reads_mapped\t'
        'sample\n'
    )

    out.write(header)

    for number in range(1, 15):

        Protein_counts = Sample_protein_counts[number]

        for unique_protein in All_proteins:

            tree_protein_name = Protein_tree_names[
                unique_protein
            ]

            count = Protein_counts.get(
                unique_protein,
                0
            )

            out.write(
                unique_protein + '\t' +
                tree_protein_name + '\t' +
                str(count) + '\t' +
                str(number) + '\n'
            )

        print('Finished sample {}'.format(number))


print('Finished writing:', output_file)
