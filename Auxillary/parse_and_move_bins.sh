for bin in bins/*/*/*/*.fna; do 
    base=$(basename "$bin" .fna)
    if grep -q "${base}" Archaea_bins_Medium_To_HQ.txt; then
        echo "${base} Found!"
        cp $bin input_dRep/
    else
        :
    fi
done
