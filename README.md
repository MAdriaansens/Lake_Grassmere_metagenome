Step -1 (getting the DNA)
Get the DNA, the DNA was extracted using LiCl Phenol/Chloroform extractions.
33, 30.4, 30.3, 25, 17, 11, 5 and ocean salinity (w/v) were sequenced. 
DNA was then sequenced using NovoSeq. With technical duplicates for samples between 33-11. 

Step 0 (XBLAST)
Use (Diamond) xblast the raw reads against a pre-made Salt resistance DB.
Using scripts run_xblast.sh and parsed using Parse_xblast.py

Step 1-2 (Filter reads using Trimmomatic)
Run FastQC before trimming, then run Trimmomatic with NexteraPE-PE.fa, then perform FastQC again.
Ensure that the poly-Gtail is removed

Step3 (Assembly)
Since the strain heterogeneity is such an issue we ran multiple assemblies.
MegaHit, MetaSpades, Isolate Spades and Carefull Spades. 

Step4 (We size filter them, but this step was merged into mapping)
SeqTK was used to filter the scaffolds based on size (>500bp)

Step5 (Mapping the all the reads to the scaffolds)
The reads for each sample were mapped to all scaffolds > 2000bp, this increases the abudance data available and help with binning later down the line
Mapping was done using BBmap (minid=0.98)

Step6 (Binning)
Binning was done using both MaxBin and MetaBat.
Resulting in at least 8 versions (At the time of writing, before dRep).

Step7 (Quality assessment)
Since we wanted our bin dereplciation to be informed by other metrics aside from dRep, and since these metrice were usefull for downstream use/publcation we used the following tools.
1. CheckM2 (Completeness, Contamination, added benefit of translating nt into aa files)
2. GTDBtk Assess the initial taxonomic grouping of the bins
3. Aragorn, asses presence of tRNAs
4. Barrnap, assess presence of sRNAs
5. xblast/blastp vs the nt and aa files, with as db the salt protein database from step 0.

6. merging all this info into one excel sheet

Step 8 (bin dereplication)
Using dRep all the bins were dereplicated + Checkm was run for strain hetereogeneity info. 
