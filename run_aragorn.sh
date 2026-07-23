
module load ARAGORN/1.2.41-foss-2023a

for bin in bins/*/*/*/*.fna; do
    entry=$(basename "$bin")
    aragorn -t -o Aragorn/output_${entry}.txt $bin
    grep 'tRNA-' Aragorn/output_${entry}.txt | grep -o '^[^(]*' > Aragorn/output_edit_${entry}.txt
    rm Aragorn/output_${entry}.txt
done
