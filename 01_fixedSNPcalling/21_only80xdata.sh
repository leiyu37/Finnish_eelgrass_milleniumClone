#!/bin/bash
# remove the 1000x data. use all the 80x results (24 modules) for analysis.

vcftools --vcf sm_add1000x_good.recode.vcf \
--remove-indv s8x \
--remove-indv s10x \
--remove-indv s12x \
--out sm_add1000x_80x \
--recode --recode-INFO-all


vcftools --vcf sm_add1000x_80x.recode.vcf \
--max-missing-count 4 \
--min-alleles 2 \
--max-alleles 2 \
--maf 0.01 \
--recode-INFO-all --recode --out sm_only80x

cat sm_only80x.recode.vcf | awk '/^LFYR/ {print}' | wc -l # 38831
