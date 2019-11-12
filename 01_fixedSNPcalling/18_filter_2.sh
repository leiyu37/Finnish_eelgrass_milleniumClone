#/bin/bash
vcftools --vcf sm_vcffilter.recode.vcf \
--max-missing-count 4 \
--min-alleles 2 \
--max-alleles 2 \
--maf 0.01 \
--recode-INFO-all \
--recode \
--out sm_add1000x_good
