#!/bin/bash
# generate gvcf file for each sample
gatk --java-options "-Xmx96G" HaplotypeCaller \
-R GCA_001185155.1_Zosma_marina.v.2.1_genomic.fna \
-I H05087-L1_S1_L001_markdup.bam \
-ERC GVCF \
-O H05087-L1_S1_L001.g.vcf
