The first thing we did after bin assembly was take the bisn from the best assembly and binning combination with the most Medium (MQ) quality bins.
This was Metabat + Isolate Metaspades

Step1 run Diamond BlastP vs MetaBat_isolate bins
We then used the prodigal used by CheckM2 as a subject and the osmotic database as a query. 
(this gives us the chance to also pull other proteins)

Step2 Retrieve and check the FL sequences hit.
We retrieve the HPPase, TrkH, and CPA fl sequences. Then put HMMaligned these to their respective HMMs and used Parse_stockholm_fl.py.
This was done to retrieve the FL of sequences for whom the sequence matched with >70% of the HMM length. 

Step3 Run Prodigal on all contigs from Isolate Metaspades
We then ran prodigal on all contigs

Step4. 
We then ran a Diamond blastp search twice. Once with the sequences from the bins and one with the in house database.

Step5.
Again we 
