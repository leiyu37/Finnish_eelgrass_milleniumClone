#!/bin/bash
# index reference genome
# reference genome: https://www.ncbi.nlm.nih.gov/genome/?term=eelgrass
bwa index -p zm_v21 GCA_001185155.1_Zosma_marina.v.2.1_genomic.fna

samtools faidx GCA_001185155.1_Zosma_marina.v.2.1_genomic.fna

gatk --java-options "-Xmx96G" CreateSequenceDictionary \
-R GCA_001185155.1_Zosma_marina.v.2.1_genomic.fna \
-O GCA_001185155.1_Zosma_marina.v.2.1_genomic.dict
