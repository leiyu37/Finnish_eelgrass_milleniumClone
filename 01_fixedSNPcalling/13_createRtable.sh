#!/bin/bash

gatk --java-options "-Xmx96G" VariantsToTable \
   -R GCA_001185155.1_Zosma_marina.v.2.1_genomic.fna \
   -V sm_add1000x_snp.vcf \
   -O Rtable_add1000x_snp.txt \
   -F CHROM -F POS -F FILTER -F QD -F MQ -F FS -F SOR -F MQRankSum -F ReadPosRankSum -F DP
