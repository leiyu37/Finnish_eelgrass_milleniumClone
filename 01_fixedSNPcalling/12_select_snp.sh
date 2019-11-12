#!/bin/bash


gatk --java-options "-Xmx96G" SelectVariants \
     -R GCA_001185155.1_Zosma_marina.v.2.1_genomic.fna \
     -V sm_add1000x_raw.vcf \
     --select-type-to-include SNP \
     -O sm_add1000x_snp.vcf
