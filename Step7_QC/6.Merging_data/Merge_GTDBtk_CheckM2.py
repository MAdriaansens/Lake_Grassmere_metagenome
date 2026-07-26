import pandas as pd
import glob

GTDBtk_file_list = glob.glob('bins/*/*/*/GTDBTK_output/*.tsv')

df_combined = pd.concat(
    (pd.read_csv(file, sep="\t") for file in GTDBtk_file_list), ignore_index=True
)

df_combined.to_csv("GTDBtk_combined_25juli.tsv", sep="\t", index=False)

Checkm2_file_list = glob.glob('bins/*/*/*/*/quality_report.tsv')
print(len(Checkm2_file_list))


df_combined = pd.concat(
    (pd.read_csv(file, sep="\t") for file in Checkm2_file_list), ignore_index=True
)

df_combined.to_csv("ChekcM2_combined_25juli.tsv", sep="\t", index=False)
