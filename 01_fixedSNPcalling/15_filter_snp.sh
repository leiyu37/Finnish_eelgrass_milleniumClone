#!/bin/bash

gatk --java-options "-Xmx96G" VariantFiltration \
   -R GCA_001185155.1_Zosma_marina.v.2.1_genomic.fna \
   -V sm_add1000x_snp.vcf \
   -O sm_add1000x_filter_snp.vcf \
   --filter-expression "MQ < 40.0" \
   --filter-name "MQ_filter" \
   --filter-expression "MQRankSum < -1.5" \
   --filter-name "MQRankSum_filter" \
   --filter-expression "FS > 10.0" \
   --filter-name "FS_filter" \
   --filter-expression "QD < 15.0" \
   --filter-name "QD_filter" \
   --filter-expression "DP > 8000.0" \
   --filter-name "DP_large"
